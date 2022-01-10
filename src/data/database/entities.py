from datetime import datetime
from inflector import Inflector
from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, Boolean, DateTime
from sqlalchemy.ext.declarative import declared_attr

from src.data.database.core import Base
from src.utils.utils import datetime_utc_now


class XEntity(object):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(True), default=datetime.utcnow)
    updated_at = Column(DateTime(True), default=datetime.utcnow)

    def __init__(self) -> None:
        super().__init__()
        self.created_at = datetime_utc_now()
        self.updated_at = datetime_utc_now()

    @declared_attr
    def __singleentity__(cls):
        classname = cls.__name__
        inflector = Inflector()
        
        return inflector.underscore(classname)

    @declared_attr
    def __pluralentity__(cls):
        label: str
        label = cls.__singleentity__

        base: str = None
        suffix: str = None

        if label.endswith('y'):
            base = label[:-1]
            suffix = 'ies'
        else:
            base = label
            suffix = 's'
        
        return '{}{}'.format(base, suffix)

    @declared_attr
    def __tablename__(cls):
        return cls.__pluralentity__



class PlatformEntity(object):
    platform_id = Column(BigInteger)


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


class InstagramHashtag(Base, XEntity, PlatformEntity):
    name = Column(String)
    media_count = Column(BigInteger)


class InstagramHashtagEpoch(Base, XEntity):
    instagram_hashtag_id = Column(Integer, ForeignKey(InstagramHashtag.id))
    media_count = Column(BigInteger)


class InstagramUser(Base, XEntity, PlatformEntity):
    username = Column(String)
    followers = Column(Integer)
    private = Column(Boolean)
    verified = Column(Boolean)
    full_name = Column(String)
    is_x_bot = Column(Boolean)


class InstagramUserEpoch(Base, XEntity):
    instagram_user_id = Column(Integer, ForeignKey(InstagramUser.id))
    username = Column(String)
    followers = Column(Integer)
    private = Column(Boolean)
    

class InstagramPost(Base, XEntity, PlatformEntity):
    pass


class InstagramPostEpoch(Base, XEntity):
    pass


class InstagramComment(Base, XEntity, PlatformEntity):
    pass


class AgentTask(Base, XEntity):
    specialty = Column(String)
    name = Column(String)
    args = Column(String)


class XProcess(Base, XEntity):
    pid = Column(Integer)
    name = Column(String)
    is_open = Column(Boolean)
