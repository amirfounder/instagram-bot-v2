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

        elif label.endswith('s'):
            base = label
            suffix = 'es'
        
        else:
            base = label
            suffix = 's'
        
        return '{}{}'.format(base, suffix)

    @declared_attr
    def __tablename__(cls):
        return cls.__pluralentity__


class SeedableEntity(object):
    used_as_seed = Column(Boolean)


class PlatformEntity(object):
    platform_id = Column(BigInteger)


class Bot(XEntity, Base):
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    birthday = Column(String)
    username = Column(String)
    password = Column(String)


class BotAccount(XEntity, Base):
    bot_id = Column(Integer, ForeignKey(Bot.id))
    username = Column(String)
    password = Column(String)


class InstagramHashtag(XEntity, Base, PlatformEntity, SeedableEntity):
    name = Column(String)
    media_count = Column(BigInteger)


class InstagramHashtagEpoch(XEntity, Base):
    instagram_hashtag_id = Column(Integer, ForeignKey(InstagramHashtag.id))
    media_count = Column(BigInteger)


class InstagramUser(XEntity, Base, PlatformEntity, SeedableEntity):
    username = Column(String)
    followers = Column(Integer)
    private = Column(Boolean)
    verified = Column(Boolean)
    full_name = Column(String)
    is_x_bot = Column(Boolean)


class InstagramUserEpoch(XEntity, Base):
    instagram_user_id = Column(Integer, ForeignKey(InstagramUser.id))
    username = Column(String)
    followers = Column(Integer)
    private = Column(Boolean)
    

class InstagramPost(XEntity, Base, PlatformEntity):
    pass


class InstagramPostEpoch(XEntity, Base):
    pass


class InstagramComment(XEntity, Base, PlatformEntity):
    pass


class AgentTask(XEntity, Base):
    name = Column(String)
    args = Column(String)
    status = Column(String)


class AppProcess(XEntity, Base):
    def __init__(self):
        super().__init__()

    pid = Column(Integer)
    name = Column(String)
    is_running = Column(Boolean)


class AppProgram(XEntity, Base):
    name = Column(String)
    status = Column(String)
