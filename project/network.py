import socket

MAX_MESSAGE = 16384

def server(sock, stop):
    while not stop.is_set():
        try:
            conn, address = sock.accept()
        except socket.timeout:
            continue

        try:
            conn.settimeout(2)
            data = bytearray()

            while not stop.is_set():
                chunk = conn.recv(1024)
                if not chunk:
                    break
                data.extend(chunk)
                if len(data) > MAX_MESSAGE:
                    raise ValueError("Message too large")

            if not stop.is_set() and data:
                print("\nReceived from", address, ":", data.decode("utf-8"))

        except (OSError, ValueError) as error:
            print("Receive error:", error)
        finally:
            conn.close()

def client(ip, port, message):
    data = message.encode("utf-8")
    if not data or len(data) > MAX_MESSAGE:
        print("Message must contain 1 to 16384 bytes")
        return

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.settimeout(5)
        sock.connect((ip, port))
        sock.sendall(data)
        print("Message sent")
    except OSError as error:
        print("Send error:", error)
    finally:
        sock.close()
