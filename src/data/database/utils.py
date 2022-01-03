from src.data.database.core import Session
from src.data.database.entities import XEntity

from sqlalchemy.orm.session import Session as TSession


def build_session() -> TSession:
    return Session()


def commit_session(session: TSession) -> None:
    session.commit()


def convert_entity_to_dict(entity) -> XEntity:
    entity_dict = {}
    entity_columns = [x.name for x in list(entity.__table__.columns)]
    for column in entity_columns:
        column_value = getattr(entity, column, None)
        if column_value is not None:
            entity_dict[column] = column_value
    return entity_dict


def convert_dict_to_entity(entity: XEntity) -> dict:
    pass
