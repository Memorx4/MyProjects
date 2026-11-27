import socket

from protocol import MAX_MESSAGE, send_message, receive_message


def server(sock, stop):
    while not stop.is_set():
        try:
            conn, address = sock.accept()
        except socket.timeout:
            continue
        except OSError as error:
            if not stop.is_set():
                print("Accept error:", error)
            break

        try:
            conn.settimeout(2)
            packet = receive_message(conn, stop)

            if not stop.is_set():
                print("\nReceived from", packet["sender"], address, ":", packet["text"])

        except (OSError, ValueError, RecursionError) as error:
            if not stop.is_set():
                print("Receive error:", error)
        finally:
            conn.close()


def client(ip, port, message, name):
    data = message.encode("utf-8")
    if not data or len(data) > MAX_MESSAGE:
        print("Message must contain 1 to 16384 bytes")
        return

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.settimeout(5)
        sock.connect((ip, port))
        send_message(sock, name, message)
        print("Message sent")
    except (OSError, ValueError) as error:
        print("Send error:", error)
    finally:
        sock.close()
