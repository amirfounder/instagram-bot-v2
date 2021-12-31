from src.data_manager.database_entities import *
from src.data_manager.repository_factory_fns import *


def add_fn_to_global_namespace(name: str, value: function, namespace: dict):
    namespace[name] = value


def build_all_entity_repository_fns(namespace: dict):
    all_entities = [
        Bot,
        BotAccount,
        InstagramHashtag,
        InstagramPost,
        InstagramUser
    ]
    
    for entity in all_entities:
        build_single_entity_repository_fns(entity, namespace)


def build_single_entity_repository_fns(entity: type[XEntity], namespace: dict):
    get_by_id_name, get_by_id_fn = build_get_by_id_fn(entity)
    add_fn_to_global_namespace(
        get_by_id_name,
        get_by_id_fn,
        namespace
    )

    get_by_ids_name, get_by_ids_fn = build_get_by_ids_fn(entity)
    add_fn_to_global_namespace(
        get_by_ids_name,
        get_by_ids_fn,
        namespace
    )

    get_by_attr_name, get_by_attr_fn = build_get_by_attr_fn(entity)
    add_fn_to_global_namespace(
        get_by_attr_name,
        get_by_attr_fn,
        namespace
    )

    save_name, save_fn = build_save_fn(entity)
    add_fn_to_global_namespace(
        save_name,
        save_fn,
        namespace
    )

    save_all_name, save_all_fn = build_save_all_fn(entity)
    add_fn_to_global_namespace(
        save_all_name,
        save_all_fn,
        namespace
    )
