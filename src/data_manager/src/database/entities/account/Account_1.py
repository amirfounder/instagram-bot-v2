from sqlalchemy.sql.sqltypes import Integer
from src.data_manager.src.database import Base
from sqlalchemy import Column, Integer


class Account_1(Base):
  __tablename__ = 'accounts_1'

  id = Column(Integer, primary_key=True)