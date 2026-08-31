import threading


class GameStorage:
    
    def __init__(self):
        self._storage = {}
        self._lock = threading.Lock()
    
    def save(self, game_id, game_data):
        with self._lock:
            self._storage[game_id] = game_data
    
    def get(self, game_id):
        with self._lock:
            return self._storage.get(game_id)
    
    def contains(self, game_id):
        with self._lock:
            return game_id in self._storage