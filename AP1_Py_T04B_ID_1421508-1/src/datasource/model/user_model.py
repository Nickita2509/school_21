from sqlalchemy import Column, String
from datasource.database import Base


class UserModel(Base):
    __tablename__ = 'users'
    
    id = Column(String, primary_key=True)
    login = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)