from datasource.model.game_storage import GameStorage
from datasource.repository.game_repository import GameRepository
from domain.service.game_service_impl import GameServiceImpl


class Container:
    
    def __init__(self):
        self._storage = GameStorage()
        self._repository = GameRepository(self._storage)
        self._service = GameServiceImpl(self._repository)
    
    @property
    def storage(self):
        return self._storage
    
    @property
    def repository(self):
        return self._repository
    
    @property
    def service(self):
        return self._service