import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from datasource.database import SessionLocal
from datasource.repository.user_repository import UserRepository
from datasource.repository.game_repository import GameRepository

from domain.service.user_service_impl import UserServiceImpl
from domain.service.game_service_impl import GameServiceImpl
from domain.service.auth_service_impl import AuthServiceImpl

from web.auth.authenticator import UserAuthenticator


DB_URL = os.environ.get("DB_URL", "postgresql://nikita@localhost:5432/tictactoe")


class Container:
    def __init__(self):
        self.engine = create_engine(DB_URL)
        SessionLocal.configure(bind=self.engine)
        
        self._user_repository = UserRepository(SessionLocal)
        self._game_repository = GameRepository(SessionLocal)
        
        self._user_service = UserServiceImpl(self._user_repository)
        self._game_service = GameServiceImpl(self._game_repository)
        self._auth_service = AuthServiceImpl(self._user_service)
        
        self._authenticator = UserAuthenticator(self._auth_service)
    
    @property
    def user_repository(self):
        return self._user_repository
    
    @property
    def game_repository(self):
        return self._game_repository
    
    @property
    def user_service(self):
        return self._user_service
    
    @property
    def game_service(self):
        return self._game_service
    
    @property
    def auth_service(self):
        return self._auth_service
    
    @property
    def authenticator(self):
        return self._authenticator