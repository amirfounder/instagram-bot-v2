from sqlalchemy import Column, Integer, String
from src.data_manager.src.database import Base


class Bot(Base):
  __tablename__ = 'bots'

  id = Column(Integer, primary_key=True)
  first_name = Column(String)
  last_name = Column(String)
  gender = Column(String)
  birthday = Column(String)
  username = Column(String)
  password = Column(String)