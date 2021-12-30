from src.data_manager.database_entities import Bot, BotAccount, InstagramHashtag, InstagramPost, InstagramUser, XEntity
from src.data_manager.database_utils import build_session



def add_to_namespace(name, value, namespace=globals()):
    pass


def build_all_entity_repository_fns():
    all_entities = [
        Bot,
        BotAccount,
        InstagramHashtag,
        InstagramPost,
        InstagramUser
    ]
    
    for entity in all_entities:
        build_single_entity_repository_fns(entity)


def build_single_entity_repository_fns(entity: type[XEntity]):
    single_label = entity.__singleentity__
    plural_label = entity.__pluralentity__

    get_by_id_fn = build_get_by_id_fn(entity)
    get_by_id_name = 'get_{}_.by_id'.format(single_label)
    add_to_namespace(get_by_id_name, get_by_id_fn)


def build_get_by_id_fn(entity: type[XEntity]):
    
    def get_by_id_fn(id: int):
        session = build_session()
        session.query(entity).get(id)

    return get_by_id_fn


def build_get_by_multiple_ids_fn():
    pass
    add_to_namespace('get_by_multiple_ids', None)


def build_get_by_attr_fn():
    pass
    add_to_namespace('get_by_attr', None)


build_all_entity_repository_fns()

