from src.data_manager.database_entities import Bot, BotAccount, InstagramHashtag, InstagramPost, InstagramUser, XEntity
from src.data_manager.database_utils import build_session


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
    get_by_multiple_ids_name, get_by_multiple_ids_fn = build_get_by_multiple_ids_fn(entity)

    add_to_namespace(get_by_id_name, get_by_id_fn, namespace)
    add_to_namespace(get_by_multiple_ids_name, get_by_multiple_ids_fn, namespace)


def build_get_by_id_fn(entity: type[XEntity]):
    fn_label = entity.__singleentity__

    def fn(id: int):
        session = build_session()

        result = session \
            .query(entity) \
            .get(id)

        session.commit()
        session.close()

        return result

    name = 'get_{}_by_id'.format(fn_label)
    return name, fn


def build_get_by_multiple_ids_fn(entity: type[XEntity]):
    fn_label = entity.__pluralentity__
    
    def fn(ids: list[int]):
        session = build_session()

        query = session \
            .query(entity) \
            .filter(entity.id.in_(ids))
        result = query.all()

        session.commit()
        session.close()

        return result
    
    name = 'get_{}_by_multiple_ids'.format(fn_label)
    return name, fn

