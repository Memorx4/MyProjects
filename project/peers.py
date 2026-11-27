import time

# Время неактивности участника в секундах
PEER_TIMEOUT = 15


# Добавление или обновление записи под блокировкой
def update_peer(peers, lock, peer_id, name, ip, port):
    lock.acquire()
    try:
        peers[peer_id] = (name, ip, port, time.monotonic())
    finally:
        lock.release()


# Удаление участников, от которых давно нет объявлений
def remove_expired(peers, lock):
    lock.acquire()
    try:
        now = time.monotonic()
        expired = []

        for peer_id, (_, _, _, last_seen) in peers.items():
            if now - last_seen >= PEER_TIMEOUT:
                expired.append(peer_id)

        # Удаляем записи после обхода словаря
        for peer_id in expired:
            del peers[peer_id]
    finally:
        lock.release()


# Получение отдельного списка активных участников
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
