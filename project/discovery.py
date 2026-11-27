import socket
import json
import time

from peers import update_peer, remove_expired

UDP_PORT = 3133
BROADCAST = "255.255.255.255"
INTERVAL = 5


def broadcast(sock, peer_id, name, tcp_port):
    packet = {
        "app": "LocalPeer",
        "id": peer_id,
        "name": name,
        "port": tcp_port
    }

    data = json.dumps(packet).encode("utf-8")
    sock.sendto(data, (BROADCAST, UDP_PORT))


def discovery_loop(sock, stop, peer_id, name, tcp_port, peers, lock):
    next_scan = 0

    while not stop.is_set():
        remove_expired(peers, lock)

        if time.monotonic() >= next_scan:
            try:
                broadcast(sock, peer_id, name, tcp_port)
            except OSError as error:
                print("Broadcast error:", error)

            next_scan = time.monotonic() + INTERVAL

        try:
            data, address = sock.recvfrom(4096)
        except socket.timeout:
            continue
        except OSError as error:
            print("Discovery error:", error)
            break

        try:
            packet = json.loads(data.decode("utf-8"))
        except (ValueError, RecursionError):
            continue

        if not isinstance(packet, dict) or packet.get("app") != "LocalPeer":
            continue

        other_id = packet.get("id")
        other_name = packet.get("name")
        port = packet.get("port")

        if not isinstance(other_id, str) or len(other_id) != 32 or other_id == peer_id:
            continue

        if not isinstance(other_name, str) or not 1 <= len(other_name) <= 32:
            continue

        if not other_name.isprintable() or type(port) is not int or not 1 <= port <= 65535:
            continue

        update_peer(peers, lock, other_id, other_name, address[0], port)
