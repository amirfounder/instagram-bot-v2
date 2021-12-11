from sqlalchemy.sql.sqltypes import Integer
from src.data_manager.src.database import Base
from sqlalchemy import Column, Integer


class Account(Base):
  __tablename__ = 'accounts'

  id = Column(Integer, primary_key=True)