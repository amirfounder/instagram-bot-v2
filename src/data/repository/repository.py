from src.data.repository.repository_factory import \
    build_all_entity_repository_fns as _build_all_entity_repository_fns


def get_all_program_processes(): pass
def get_all_program_processes_by_column(): pass

global_namespace = globals()
_build_all_entity_repository_fns(global_namespace)
