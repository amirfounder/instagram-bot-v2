from sqlalchemy.engine import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import registry
from sqlalchemy.orm.session import sessionmaker, Session as TSession

mapper_registry = registry()

MetaData = mapper_registry.metadata
Base = mapper_registry.generate_base()

CONNECTION_STRING = 'postgresql://postgres:root@localhost:5432/x'

engine: Engine
engine = create_engine(CONNECTION_STRING, echo=True, future=True, connect_args={'options': '-c timezone=utc'})
Session: TSession
Session = sessionmaker(bind=engine)


def build_session() -> TSession:
    return Session()


def commit_session(session: TSession):
    session.commit()


def convert_entity_to_dict(entity):
    entity_dict = {}
    entity_columns = [x.name for x in list(entity.__table__.columns)]
    for column in entity_columns:
        column_value = getattr(entity, column, None)
        if column_value is not None:
            entity_dict[column] = column_value
    return entity_dict
