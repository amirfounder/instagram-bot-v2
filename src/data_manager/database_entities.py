from src.data_manager.database_utils import Base
from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, Boolean
from sqlalchemy.ext.declarative import declared_attr
from inflector import Inflector


class XEntity(object):
    infl = Inflector()

    @declared_attr
    def __singleentity__(cls):
        inflector = Inflector()
        return inflector.underscore(cls.__name__)
    
    @declared_attr
    def __pluralentity__(cls):
        return '{}s'.format(cls.__singleentity__)

    @declared_attr
    def __tablename__(cls):
        return cls.__pluralentity__
    
    id = Column(Integer, primary_key=True)


class Bot(Base, XEntity):
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    birthday = Column(String)
    username = Column(String)
    password = Column(String)


class BotAccount(Base, XEntity):
    bot_id = Column(Integer, ForeignKey(Bot.id))
    username = Column(String)
    password = Column(String)


class InstagramHashtag(Base, XEntity):
    name = Column(String)
    media_count = Column(BigInteger)


class InstagramUser(Base, XEntity):
    ig_id = Column(BigInteger, unique=True, nullable=False)
    username = Column(String)
    followers = Column(Integer)
    private = Column(Boolean)
    verified = Column(Boolean)
    full_name = Column(String)
    timestamp_logged = Column(String)
    timestamp_updated = Column(String)
    is_x_bot = Column(Boolean)


class InstagramPost(Base, XEntity):
    pass


class InstagramComment(Base, XEntity):
    pass
