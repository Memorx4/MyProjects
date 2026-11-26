import socket
import json
import time

UDP_PORT = 8000
BROADCAST = "255.255.255.255"
INTERVAL = 5

def make_packet(kind, peer_id, name, tcp_port):
    packet = {
        "app": "LocalPeer",
        "type": kind,
        "id": peer_id,
        "name": name,
        "tcp_port": tcp_port
    }
    return json.dumps(packet).encode("utf-8")


def broadcast(sock, peer_id, name, tcp_port):
    packet = make_packet("DISCOVER", peer_id, name, tcp_port)
    sock.sendto(packet, (BROADCAST, UDP_PORT))


def discovery_loop(sock, stop, peer_id, name, tcp_port, peers, lock):
    last_scan = None

    while not stop.is_set():
        now = time.monotonic()
        if last_scan is None or now - last_scan >= INTERVAL:
            try:
                broadcast(sock, peer_id, name, tcp_port)
            except OSError as error:
                print("Broadcast error:", error)
            last_scan = now

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

        kind = packet.get("type")
        other_id = packet.get("id")
        other_name = packet.get("name")
        port = packet.get("tcp_port")

        if kind not in ("DISCOVER", "ANNOUNCE") or other_id == peer_id:
            continue
        if not isinstance(other_id, str) or not 1 <= len(other_id) <= 64:
            continue
        if not isinstance(other_name, str) or not 1 <= len(other_name) <= 32:
            continue
        if not other_name.isprintable() or type(port) is not int or not 1 <= port <= 65535:
            continue

        lock.acquire()
        try:
            peers[other_id] = {"name": other_name, "ip": address[0], "port": port}
        finally:
            lock.release()

        if kind == "DISCOVER":
            reply = make_packet("ANNOUNCE", peer_id, name, tcp_port)
            try:
                sock.sendto(reply, address)
            except OSError as error:
                print("Reply error:", error)
