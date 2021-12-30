from sqlalchemy.engine import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import registry
from sqlalchemy.orm.session import sessionmaker, Session as TSession

mapper_registry = registry()
MetaData = mapper_registry.metadata
Base = mapper_registry.generate_base()

CONNECTION_STRING = 'postgresql://postgres:root@localhost:5432/x'

engine: Engine = create_engine(CONNECTION_STRING, echo=True, future=True)
Session = sessionmaker(bind=engine)

def build_session() -> TSession:
    return Session()
