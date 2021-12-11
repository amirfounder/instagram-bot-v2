from src.data_manager.src.database import Base
from sqlalchemy import Column, Integer


class Hashtag(Base):
  __tablename__ = 'hashtags'

  id = Column(Integer, primary_key=True)
