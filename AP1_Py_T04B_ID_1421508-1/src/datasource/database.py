from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
SessionLocal = sessionmaker()


def init_db(engine):
    from datasource.model.user_model import UserModel
    from datasource.model.game_model import GameModel
    Base.metadata.create_all(bind=engine)