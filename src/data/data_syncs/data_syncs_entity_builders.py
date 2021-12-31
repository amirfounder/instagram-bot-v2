from src.data.database.entities import InstagramUser, InstagramPost, InstagramHashtag


def build_instagram_user_to_save(user_as_dict: dict, timestamp: str):
    user = InstagramUser()
    user.ig_id = user_as_dict['pk']
    user.username = user_as_dict['username']
    user.full_name = user_as_dict['full_name']
    user.private = user_as_dict['is_private']
    user.verified = user_as_dict['is_verified']
    user.timestamp_logged = timestamp
    user.timestamp_updated = timestamp
    return user


def build_instagram_user_to_update(user: InstagramUser, user_as_dict: dict, timestamp: str):
    user.timestamp_updated = timestamp
    return user


def build_instagram_post_to_update(post: InstagramPost, post_as_dict: dict, timestamp: str):
    pass


def build_instagram_post_to_save(post_as_dict: dict, timestamp: str):
    pass


def build_instagram_hashtag_to_save(hashtag_as_dict: dict, timestamp: str):
    pass


def build_instagram_hashtag_to_update(hashtag: InstagramHashtag, hashtag_as_dict: dict, timestamp: str):
    pass