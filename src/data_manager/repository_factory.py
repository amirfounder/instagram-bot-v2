from typing import Any

from sqlalchemy.sql.expression import select
from src.data_manager.database_entities import Bot, BotAccount, InstagramHashtag, InstagramPost, InstagramUser, XEntity
from src.data_manager.database_utils import build_session
from sqlalchemy import column


def add_to_namespace(name, value, namespace):
    namespace[name] = value


def build_all_entity_repository_fns(namespace):
    all_entities = [
        Bot,
        BotAccount,
        InstagramHashtag,
        InstagramPost,
        InstagramUser
    ]
    
    for entity in all_entities:
        build_single_entity_repository_fns(entity, namespace)


def build_single_entity_repository_fns(entity: type[XEntity], namespace):
    get_by_id_name, get_by_id_fn = build_get_by_id_fn(entity)
    add_to_namespace(
        get_by_id_name,
        get_by_id_fn,
        namespace
    )

    get_by_ids_name, get_by_ids_fn = build_get_by_ids_fn(entity)
    add_to_namespace(
        get_by_ids_name,
        get_by_ids_fn,
        namespace
    )

    get_by_attr_name, get_by_attr_fn = build_get_by_attr_fn(entity)
    add_to_namespace(
        get_by_attr_name,
        get_by_attr_fn,
        namespace
    )


def build_get_by_attr_fn(entity: type[XEntity]):
    fn_label = entity.__pluralentity__

    def fn(attr: str, val: Any | list[Any]):
        session = build_session()

        criteria = None

        if type(val) is list:
            criteria = column(attr).in_(val)
        else:
            criteria = column(attr) == val

        query = session \
            .query(entity) \
            .filter(criteria)
        result = query.all()

        session.expunge_all()
        session.commit()
        session.close()

        return result
    
    name = 'get_{}_by_attr'.format(fn_label)
    return name, fn

def build_get_by_id_fn(entity: type[XEntity]):
    fn_label = entity.__singleentity__

    def fn(id: int):
        session = build_session()

        query = session.query(entity)
        result = query.get(id)

        session.expunge_all()
        session.commit()
        session.close()

        return result

    name = 'get_{}_by_id'.format(fn_label)
    return name, fn


def build_get_by_ids_fn(entity: type[XEntity]):
    fn_label = entity.__pluralentity__
    
    def fn(ids: list[int]):
        session = build_session()

        query = session \
            .query(entity) \
            .filter(entity.id.in_(ids))
        result = query.all()

        session.expunge_all()
        session.commit()
        session.close()

        return result
    
    name = 'get_{}_by_ids'.format(fn_label)
    return name, fn

