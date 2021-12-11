from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey

from src.data_manager.src.database import Base
from src.data_manager.src.database.entities.Account import Account


class Bot(Base):
  __tablename__ = 'bots'

  id = Column(Integer, primary_key=True)
  first_name = Column(String)
  last_name = Column(String)
  gender = Column(String)
  birthday = Column(String)
  username = Column(String)
  password = Column(String)