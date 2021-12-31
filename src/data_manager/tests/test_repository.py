from src.data_manager.repository import get_instagram_user_by_id

def test_lol():

    x = get_instagram_user_by_id(1)
    assert x is not None