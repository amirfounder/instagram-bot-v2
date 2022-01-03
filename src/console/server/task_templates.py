research_hashtags_task_template = {
    'name': 'Research Hashtags',
    'description': 'TBD',
    'platform': 'instagram',
    'user_args': [
        {
            'label': 'Seed:',
            'description': 'The starting hashtag to build network around',
            'type': 'text',
            'placeholder': None
        },
        {
            'label': 'Account to use',
            'description': 'The bot account to be logged into',
            'type': 'text',
            'placeholder': None
        }
    ],
}

research_top_posts_task_template = {
    'name': 'Research Top Posts',
    'description': 'For every account, select account market. Find other accounts with \
        same market and approximate follower range. Save results in "InstagramTopPosts" table.',
    'platform': 'instagram',
    'user_args': [
        {
            'label': 'Niches(s)',
            'description': 'Accounts to find top posts FOR. Default = all that have no content scheduled',
            'type': 'text',
            'placeholder': None
        }
    ]
}

engage_with_comments = {}
engage_with_followers = {}
