import time

PEER_TIMEOUT = 15


def update_peer(peers, lock, peer_id, name, ip, port):
    lock.acquire()
    try:
        peers[peer_id] = (name, ip, port, time.monotonic())
    finally:
        lock.release()


def remove_expired(peers, lock):
    lock.acquire()
    try:
        now = time.monotonic()
        expired = []

        for peer_id, (_, _, _, last_seen) in peers.items():
            if now - last_seen >= PEER_TIMEOUT:
                expired.append(peer_id)

        for peer_id in expired:
            del peers[peer_id]
    finally:
        lock.release()


def get_peers(peers, lock):
    remove_expired(peers, lock)
    lock.acquire()
    try:
        participants = []
        for name, ip, port, last_seen in peers.values():
            participants.append((name, ip, port))
        return participants
    finally:
        lock.release()
