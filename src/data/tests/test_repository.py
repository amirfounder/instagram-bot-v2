from src.data.repository.repository import get_instagram_user_by_id, get_instagram_users_by_ids
from src.data.database.entities import InstagramUser

def test_get_by_id():

    x = get_instagram_user_by_id(1)

    assert type(x) is InstagramUser
    assert x.id == 1


def test_get_all_by_id():

    x = get_instagram_users_by_ids([1, 2, 3])

    assert type(x) is list
    assert type(x[0]) is InstagramUser
    assert type(x[1]) is InstagramUser
    assert type(x[2]) is InstagramUser
    assert x[0].id == 1
    assert x[1].id == 2
    assert x[2].id == 3

