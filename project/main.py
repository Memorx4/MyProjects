import socket
import threading

from network import server, client

TCP_PORT = int(input("Enter local port: "))

def command_loop():

    print("Commands: send, exit")

    while True:

        command = input("LocalPeer > ").strip().lower()

        if command == "send":

            ip = input("Enter peer IP: ")
            port = int(input("Enter peer port: "))
            message = input("Enter message: ")

            client(ip, port, message)

        elif command == "exit":
            break
        else:
            print("Unknown command")

def main():

    stop = threading.Event() #синх потоков 
 
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        tcp.bind(("0.0.0.0", TCP_PORT))
        tcp.listen()
        tcp.settimeout(0.5) # огран accept если я писал exit  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                            # в главном потоке он почему то продолжал ждать подключения # опытным путем во время join у меня все зависало
        tcp_thread = threading.Thread(target=server, args=(tcp, stop))
                            # запуск второго потока
        tcp_thread.start()

        try:
            print("LocalPeer started. TCP:", TCP_PORT)

            command_loop()
        finally:
            stop.set()
            tcp_thread.join() # ждет завершения, без добавления в главном потоке закрывался
                              # а второй непонятно что делал, !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    except OSError as error:
        print("Network error:", error)

    finally:
        tcp.close()

    print("Program stopped")

main()