from sqlalchemy.sql.sqltypes import Boolean
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


class InstagramUser(Base):
    __tablename__ = 'instagram_user'

    id = Column(Integer, primary_key=True)
    ig_id = Column(BigInteger, unique=True, nullable=False)
    username = Column(String)
    followers = Column(Integer)
    private = Column(Boolean)
    verified = Column(Boolean)
    full_name = Column(String)
    timestamp_logged = Column(String)
    timestamp_updated = Column(String)


class InstagramPost(Base):
    __tablename__ = 'instagram_post'

    id = Column(Integer, primary_key=True)
