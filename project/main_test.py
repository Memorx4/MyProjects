import socket
import threading
import uuid

from network import server, client
from discover_test import UDP_PORT, broadcast, discovery_loop

TCP_PORT = 8000

def show_peers(peers, lock):
    lock.acquire()
    try:
        found = list(peers.values())
    finally:
        lock.release()

    if not found:
        print("No peers found. Try scan.")
    else:
        for number, peer in enumerate(found, 1):
            print(number, peer["name"], peer["ip"], peer["port"])
    return found

def command_loop(udp, peer_id, name, port, peers, lock):
    print("Commands: peers, scan, send, exit")

    while True:
        command = input("LocalPeer > ").strip().lower()

        if command == "peers":
            show_peers(peers, lock)

        elif command == "scan":
            broadcast(udp, peer_id, name, port)
            print("Searching... Use peers to see the results.")

        elif command == "send":
            found = show_peers(peers, lock)
            if not found:
                continue
            try:
                number = int(input("Choose peer number: "))
            except ValueError:
                print("Invalid number")
                continue
            if not 1 <= number <= len(found):
                print("Invalid number")
                continue
            peer = found[number - 1]
            message = input("Enter message: ")
            client(peer["ip"], peer["port"], message)

        elif command == "exit":
            break
        else:
            print("Unknown command")


def main():
    name = input("Enter your name: ").strip()
    if not 1 <= len(name) <= 32 or not name.isprintable():
        print("Invalid name")
        return

    peer_id = uuid.uuid4().hex
    peers = {}
    lock = threading.Lock()
    stop = threading.Event()
    threads = []

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        tcp.bind(("0.0.0.0", TCP_PORT))
        tcp.listen()
        tcp.settimeout(0.5)

        udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        udp.bind(("0.0.0.0", UDP_PORT))
        udp.settimeout(0.5)

        tcp_thread = threading.Thread(target=server, args=(tcp, stop))
        udp_thread = threading.Thread(
            target=discovery_loop,
            args=(udp, stop, peer_id, name, TCP_PORT, peers, lock)
        )
        tcp_thread.start()
        threads.append(tcp_thread)
        udp_thread.start()
        threads.append(udp_thread)

        print("LocalPeer started. TCP:", TCP_PORT, "UDP:", UDP_PORT)
        command_loop(udp, peer_id, name, TCP_PORT, peers, lock)

    except (KeyboardInterrupt, EOFError):
        pass
    except OSError as error:
        print("Network error:", error)
    finally:
        stop.set()
        for thread in threads:
            thread.join()
        udp.close()
        tcp.close()

    print("Program stopped")


main()
