from src.data_manager.src.database import Base
from sqlalchemy import Column, Integer


class Hashtag_1(Base):
  __tablename__ = 'hashtags_1'

  id = Column(Integer, primary_key=True)
