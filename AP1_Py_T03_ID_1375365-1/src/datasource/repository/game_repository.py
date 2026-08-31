class GameRepository:
    
    def __init__(self, storage):
        self.storage = storage
    
    def save(self, game):
        self.storage.save(game.game_id, game.to_dict())
    
    def get(self, game_id):
        return self.storage.get(game_id)
    
    def contains(self, game_id):
        return self.storage.contains(game_id)