from typing import Callable
from src.data.database.entities import *
from src.data.repository.repository_factory_builders import *


def add_fn_to_global_namespace(name: str, value: Callable, namespace: dict) -> None:
    namespace[name] = value


def build_all_entity_repository_fns(namespace: dict) -> None:
    all_entities = [
        AgentTask,
        Bot,
        BotAccount,
        InstagramHashtag,
        InstagramUser,
        InstagramPost,
        InstagramComment,
        ProgramProcess,
    ]
    
    for entity in all_entities:
        build_entity_repository_fns(entity, namespace)


def build_entity_repository_fns(entity: type[XEntity], namespace: dict) -> None:

    name = build_get_by_id_fn_name(entity)
    fn = build_get_by_id_fn(entity)
    add_fn_to_global_namespace(name, fn, namespace)

    name = build_get_all_by_ids_fn_name(entity)
    fn = build_get_all_by_ids_fn(entity)
    add_fn_to_global_namespace(name, fn, namespace)

    name = build_get_all_by_column_fn_name(entity)
    fn = build_get_all_by_column_fn(entity)
    add_fn_to_global_namespace(name, fn, namespace)

    name = build_save_fn_name(entity)
    fn = build_save_fn()
    add_fn_to_global_namespace(name, fn, namespace)

    name = build_save_all_fn_name(entity)
    fn = build_save_all_fn()
    add_fn_to_global_namespace(name, fn, namespace)

    name = build_update_fn_name(entity)
    fn = build_update_fn(entity)
    add_fn_to_global_namespace(name, fn, namespace)
