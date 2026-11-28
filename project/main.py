import socket
import threading
import uuid

from network import server, client
from peers import get_peers
from discovery import UDP_PORT, broadcast, discovery_loop

# Проверка порта
def read_port(prompt):
    port = int(input(prompt))
    if not 1 <= port <= 65535: 
        raise ValueError("Invalid port")
    return port

# Вывод списка активных груш
def show_peers(peers, lock):
    participants = get_peers(peers, lock)
    if not participants:
        print("No peers found")
    for number, (name, ip, port) in enumerate(participants, 1):
        print(number, name, ip, port)

    return participants

# Обработка команд 
def command_loop(udp, peer_id, name, tcp_port, peers, lock):
    print("Commands: peers, scan, send, sendpeer, exit")
    while True:
        command = input("LocalPeer > ").strip().lower()
        try:
            if command == "peers":
                show_peers(peers, lock)

            elif command == "scan":
                broadcast(udp, peer_id, name, tcp_port)
                print("Announcement sent")

            elif command == "send":
                ip = input("Enter peer IP: ").strip()
                port = read_port("Enter peer port: ")
                message = input("Enter message: ")
                client(ip, port, message, name)

            # Отправка участнику из списка
            elif command == "sendpeer":
                participants = show_peers(peers, lock)
                if not participants:
                    continue

                number = int(input("Choose peer number: "))
                if not 1 <= number <= len(participants):
                    print("Invalid peer number")
                    continue

                other_name, ip, port = participants[number - 1]
                message = input("Enter message: ")
                client(ip, port, message, name)

            elif command == "exit":
                break

            else:
                print("Unknown command")

        except ValueError:
            print("Invalid input")
        except OSError as error:
            print("Network error:", error)

def main():
    # Общие данные и сигнал остановки потоков
    stop = threading.Event()
    peers = {} # имя адрес TCP и обновление !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    lock = threading.Lock() # опытным путем было выяснено что udp и tcp могут ругаться друг с другом
    peer_id = uuid.uuid4().hex 
    
    tcp = None
    udp = None
    threads = []

    try:
        name = input("Enter your name: ").strip()
        if not 1 <= len(name) <= 32 or not name.isprintable():
            print("Must contain 1 to 32 printable symbols")
        tcp_port = read_port("Enter local TCP port: ")

        # TCP
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.bind(("0.0.0.0", tcp_port))
        tcp.listen()
        tcp.settimeout(0.5) #accept ложил программу, поэтому пришлось в нетворке поставить огран

        # UDP
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        udp.bind(("0.0.0.0", UDP_PORT))
        udp.settimeout(0.5)

        # Потоки приёма поиска груш
        tcp_thread = threading.Thread(target=server, args=(tcp, stop))
        udp_thread = threading.Thread(target=discovery_loop,args=(udp, stop, peer_id, name, tcp_port, peers, lock))
        
        tcp_thread.start()
        threads.append(tcp_thread)
        udp_thread.start()
        threads.append(udp_thread)

        print("LocalPeer started. TCP:", tcp_port, "UDP:", UDP_PORT)
        command_loop(udp, peer_id, name, tcp_port, peers, lock)

    except (KeyboardInterrupt, EOFError):
        pass
    except (OSError, ValueError) as error:
        print("Error:", error)
    finally:
        stop.set()
        for thread in threads:
            thread.join()

        if tcp is not None:
            tcp.close()
        if udp is not None:
            udp.close()
    print("STOPPED")

if __name__ == "__main__":
    main()
