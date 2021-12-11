from sqlalchemy import Column, Integer, String

from src.data_manager.src.database import Base


class Bot_1(Base):
  __tablename__ = 'bots_1'

  id = Column(Integer, primary_key=True)
  first_name = Column(String(50))
  last_name = Column(String(50))
  gender = Column(String(6))
  birthday = Column(String(10))
  username = Column(String(100))
  password = Column(String(50))