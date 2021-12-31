from src.data.database import setup_database
from src.data.repository.repository_factory import build_all_entity_repository_fns


def lol():
    pass


def test_build_all_entities():

    setup_database()
    build_all_entity_repository_fns(globals())

    assert 'get_instagram_user_by_id' in globals()
