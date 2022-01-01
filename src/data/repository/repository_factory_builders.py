"""
Functions:
- Get All
- Get By Id
- Get All By Attribute
- Save
- Save All
- Update By Id
- Update All By Ids (TODO)
- Delete By Id (TODO)
- Delete All By Ids (TODO)
"""

from typing import Any
from src.data.database.entities import XEntity
from src.data.database.utils import build_session, convert_entity_to_dict
from sqlalchemy import column


"""get_all_by_attr"""


def build_get_all_by_attr_fn_name(entity: type[XEntity]):
    label = entity.__pluralentity__
    name = 'get_all_{}_by_attr'.format(label)
    
    return name


def build_get_all_by_attr_fn(entity: type[XEntity]):

    def fn(attr: str, val: Any | list[Any]):
        session = build_session()

        criteria = None

        if type(val) is list:
            criteria = column(attr).in_(val)
        else:
            criteria = column(attr) == val

        query = session.query(entity).filter(criteria)
        result = query.all()

        session.commit()
        session.expunge_all()
        session.close()

        return result
    
    return fn


"""get_by_id"""


def build_get_by_id_fn_name(entity: type[XEntity]):
    label = entity.__singleentity__
    name = 'get_{}_by_id'.format(label)

    return name


def build_get_by_id_fn(entity: type[XEntity]):

    def fn(id: int):
        session = build_session()

        query = session.query(entity)
        result = query.get(id)

        session.commit()
        session.expunge_all()
        session.close()

        return result

    return fn


"""get_all_by_ids"""


def build_get_all_by_ids_fn_name(entity: type[XEntity]):
    label = entity.__pluralentity__
    name = 'get_all_{}_by_ids'.format(label)

    return name


def build_get_all_by_ids_fn(entity: type[XEntity]):
    
    def fn(ids: list[int]):
        session = build_session()

        query = session \
            .query(entity) \
            .filter(entity.id.in_(ids))
        result = query.all()

        session.commit()
        session.expunge_all()
        session.close()

        return result
    
    return fn


"""save"""


def build_save_fn_name(entity: type[XEntity]):
    label = entity.__singleentity__
    name = 'save_{}'.format(label)

    return name

def build_save_fn(entity: type[XEntity]):

    def fn(instance: XEntity):
        session = build_session()
        
        session.add(instance)

        session.commit()
        session.refresh(instance)
        session.expunge_all()
        session.close()

        return instance

    return fn


"""save_all"""


def build_save_all_fn_name(entity: type[XEntity]):
    label = entity.__pluralentity__
    name = 'save_all_{}'.format(label)

    return name


def build_save_all_fn(entity: type[XEntity]):

    def fn(instances: list[XEntity]):
        session = build_session()

        session.add_all(instances)

        session.commit()

        for instance in instances:
            session.refresh(instance)
        
        session.expunge_all()
        session.close()
    
        return instances
    
    return fn


"""update_by_id"""


def build_update_by_id_fn_name(entity: type[XEntity]):
    label = entity.__singleentity__
    name = 'update_{}_by_id'.format(label)

    return name


def build_update_by_id_fn(entity: type[XEntity]):
    
    def fn(instance: list[XEntity]):
        session = build_session()
        entity_as_dict = convert_entity_to_dict(instance)

        session \
            .query(type(entity)) \
            .filter(type(entity).id == entity.id) \
            .update(entity_as_dict)
        
        session.commit()

    return fn


"""update_all_by_id"""

"""delete_by_id""" 

"""delete_all_by_id"""
