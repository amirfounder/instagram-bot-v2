from src.data.repository.repository_factory import \
    build_all_entity_repository_fns as _build_all_entity_repository_fns


global_namespace = globals()
_build_all_entity_repository_fns(global_namespace)
