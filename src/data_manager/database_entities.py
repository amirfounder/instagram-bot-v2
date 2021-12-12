from src.data_manager.database_utils import Base
from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger


class Bot(Base):
  __tablename__ = 'bots'

  id = Column(Integer, primary_key=True)
  first_name = Column(String)
  last_name = Column(String)
  gender = Column(String)
  birthday = Column(String)
  username = Column(String)
  password = Column(String)


class BotAccount(Base):
  __tablename__ = 'bot_accounts'

  id = Column(Integer, primary_key=True)
  bot_id = Column(Integer, ForeignKey(Bot.id))
  username = Column(String)
  password = Column(String)


class InstagramHashtag(Base):
  __tablename__ = 'instagram_hashtags'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  media_count = Column(BigInteger)
