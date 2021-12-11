from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from src.data_manager.src.database import Base
from src.data_manager.src.database.entities import Bot


class Account(Base):
  __tablename__ = 'accounts'

  id = Column(Integer, primary_key=True)
  bot_id = Column(Integer, ForeignKey(Bot.id))
  username = Column(String)
  password = Column(String)