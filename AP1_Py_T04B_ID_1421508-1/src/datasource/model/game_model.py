from sqlalchemy import Column, String, JSON, Integer
from datasource.database import Base


class GameModel(Base):
    __tablename__ = 'games'
    
    id = Column(String, primary_key=True)
    board = Column(JSON, nullable=False)
    state = Column(String, nullable=False)
    player_x_id = Column(String, nullable=True)
    player_o_id = Column(String, nullable=True)
    current_turn = Column(Integer, nullable=True)
    game_type = Column(String, nullable=False)
    last_board = Column(JSON, nullable=True)