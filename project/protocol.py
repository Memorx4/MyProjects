import json

# Размер заголовка и ограничения на текст и JSON
HEADER_SIZE = 4
MAX_MESSAGE = 16384
MAX_FRAME = 131072
# Проверка структуры и содержимого сообщения
def check_message(packet):
    if not isinstance(packet, dict) or packet.get("type") != "message":
        raise ValueError("Unknown message type")

    sender = packet.get("sender")
    text = packet.get("text")

    if not isinstance(sender, str) or not 1 <= len(sender) <= 32:
        raise ValueError("Invalid sender name")
    if not sender.isprintable():
        raise ValueError("Invalid sender name")
    if not isinstance(text, str) or not 1 <= len(text.encode("utf-8")) <= MAX_MESSAGE:
        raise ValueError("Message must contain 1 to 16384 bytes")


# Формирование JSON-сообщения для TCP
def send_message(sock, name, message):
    packet = {
        "type": "message",
        "sender": name,
        "text": message
    }
    check_message(packet)
    data = json.dumps(packet, ensure_ascii=False).encode("utf-8")

    if len(data) > MAX_FRAME:
        raise ValueError("Frame too large")

    # Добавляем длину JSON в виде 4 байтов (big endian)
    header = len(data).to_bytes(HEADER_SIZE, "big")
    sock.sendall(header + data)


# Чтение строго заданного количества байтов
def recv_exact(sock, size, stop):
    data = bytearray()

    while len(data) < size:
        if stop.is_set():
            raise InterruptedError("Program stopping")

        # Читаем не больше оставшегося количества байтов
        chunk = sock.recv(min(4096, size - len(data)))
        if not chunk:
            raise ValueError("Connection closed before complete frame")
        data.extend(chunk)

    return data


# Сначала читаем заголовок, затем JSON указанной длины
def receive_message(sock, stop):
    header = recv_exact(sock, HEADER_SIZE, stop)
    size = int.from_bytes(header, "big")

    if not 1 <= size <= MAX_FRAME:
        raise ValueError("Invalid frame size")

    data = recv_exact(sock, size, stop)
    packet = json.loads(data.decode("utf-8"))
    check_message(packet)
    return packet
