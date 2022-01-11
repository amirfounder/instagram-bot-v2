'''
Functions:
- Get All
- Get By Id
- Get All By Column
- Save
- Save All
- Update
- Update All (TODO)
- Delete By Id (TODO)
- Delete All By Ids (TODO)
'''

from typing import Any
from src.data.database.entities import XEntity
from src.data.database.utils import build_session, convert_entity_to_dict
from sqlalchemy import column
from datetime import datetime

from src.utils.utils import build_datetimestamp


'''get_by_id'''


def build_get_by_id_fn_name(entity: type[XEntity]):
    label = entity.__singleentity__
    name = 'get_{}_by_id'.format(label)

    return name


def build_get_by_id_fn(entity: type[XEntity]):

    def fn(id: int):
        session = build_session()

        query = session.query(entity)
        result = query.get(id)

        session.expunge_all()
        session.close()

        return result

    return fn


'''get_all_by_ids'''


def build_get_all_by_ids_fn_name(entity: type[XEntity]):
    label = entity.__pluralentity__
    name = 'get_all_{}_by_ids'.format(label)

    return name


def build_get_all_by_ids_fn(entity: type[XEntity]):
    
    def fn(ids: list[int]):
        session = build_session()

        result = session \
            .query(entity) \
            .filter(entity.id.in_(ids)) \
            .all()

        session.expunge_all()
        session.close()

        return result
    
    return fn


'''get_all_by_column'''


def build_get_all_by_column_fn_name(entity: type[XEntity]):
    label = entity.__pluralentity__
    name = 'get_all_{}_by_column'.format(label)
    
    return name


def build_get_all_by_column_fn(entity: type[XEntity]):

    def fn(column_name: str, val: Any | list[Any]):
        session = build_session()
        criteria = None

        attributes = dir(entity)
        if column_name not in attributes:
            return []

        if type(val) is list:
            criteria = column(column_name).in_(val)
        else:
            criteria = column(column_name) == val

        result = session \
            .query(entity) \
            .filter(criteria) \
            .all()

        session.expunge_all()
        session.close()

        return result
    
    return fn


'''get_all_after_datetimestamp'''


def build_get_all_after_timestamp_fn_name(entity: type[XEntity]):
    label = entity.__pluralentity__
    name = 'get_all_{}_after_timestamp'.format(label)

    return name


def build_get_all_after_datetimestamp_fn(entity: type[XEntity]):
    
    def fn(datetimestamp: datetime):

        session = build_session()


'''save'''


def build_save_fn_name(entity: type[XEntity]):
    label = entity.__singleentity__
    name = 'save_{}'.format(label)

    return name

def build_save_fn():

    def fn(instance: XEntity):
        session = build_session()
        
        session.add(instance)

        session.commit()
        session.refresh(instance)
        session.expunge_all()
        session.close()

        return instance

    return fn


'''save_all'''


def build_save_all_fn_name(entity: type[XEntity]):
    label = entity.__pluralentity__
    name = 'save_all_{}'.format(label)

    return name


def build_save_all_fn():

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


'''update'''


def build_update_fn_name(entity: type[XEntity]):
    label = entity.__singleentity__
    name = 'update_{}'.format(label)

    return name


def build_update_fn(entity: type[XEntity]):
    
    def fn(instance: XEntity):
        session = build_session()
        instance.updated_at = build_datetimestamp()
        entity_as_dict = convert_entity_to_dict(instance)
        

        session \
            .query(entity) \
            .filter(entity.id == instance.id) \
            .update(entity_as_dict)
        
        session.commit()

    return fn


'''update_all'''

'''delete_by_id''' 

'''delete_all_by_id'''
