#!/usr/bin/python3
""" Returns a list containing the titles of all hot
        articles for a given subreddit """
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """ Recursively """
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = get(URL, params={'after': after}, headers={'User-agent': 'MyAPI'})
    if r.status_code == 200:
        data = r.json()
        posts = data['data']['children']
        after = data['data']['after']
        for title in posts:
            hot_list.append(title['data']['title'])
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
