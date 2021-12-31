from typing import Any
from src.data_manager.database_entities import XEntity
from src.data_manager.database_utils import build_session
from sqlalchemy import column


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

        session.commit()
        session.expunge_all()
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

        session.commit()
        session.expunge_all()
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

        session.commit()
        session.expunge_all()
        session.close()

        return result
    
    name = 'get_{}_by_ids'.format(fn_label)
    return name, fn


def build_save_fn(entity: type[XEntity]):
    fn_label = entity.__singleentity__

    def fn(instance: XEntity):
        session = build_session()
        
        session.add(instance)

        session.commit()
        session.refresh(instance)
        session.expunge_all()
        session.close()

        return instance

    name = 'save_{}'.format(fn_label)
    return name, fn


def build_save_all_fn(entity: type[XEntity]):
    fn_label = entity.__pluralentity__

    def fn(instances: list[XEntity]):
        session = build_session()

        session.add_all()

        session.commit()

        for instance in instances:
            session.refresh(instance)
        
        session.expunge_all()
        session.close()
    
        return instances
    
    name = 'save_all_{}'.format(fn_label)
    return name, fn

