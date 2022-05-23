#!/usr/bin/python3
""" Returns a list containing the titles of all hot
        articles for a given subreddit """
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """ Recursively """
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = get(URL, params={"after": after}, headers={"User-agent": "holbie"})
    if r.status_code == 200:
        data = data.json()
        posts = data['data']['children']
        after = data['data']['after']
        if after is not None:
            hot_list.append(posts[0]['data']['title'])
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
