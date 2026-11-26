import socket
PORT = 3132

def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    sock.bind(("0.0.0.0", PORT))
    sock.listen()

    print("Waiting")

    conn, address = sock.accept()

    print("Connected:", address)

    data = bytearray()

    while True:

        chack = conn.recv(1024)

        if not chack:
            break

        data.extend(chack)

    print("Received:", data.decode("utf-8")) 
    conn.close()
    sock.close()


def client():
    ip = input("Server IP: ")
    message = input("Message: ")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((ip, PORT))

    sock.sendall(message.encode("utf-8")) 

    sock.close()

    print("Message sent")


def main():
    print("1 Server")
    print("2 Client")

    choice = input("Choose: ")

    if choice == "1":
        server()

    elif choice == "2":
        client()

main()