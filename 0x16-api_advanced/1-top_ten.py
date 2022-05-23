#!/usr/bin/python3
""" Print the titles of the first 10 hot posts listed for a given subreddit """
from requests import get, request


def top_ten(subreddit):
    """ Returns the tittles of the first 10 hot posts """
    URL = "https://www.reddit.com/r/{}/.json?limit=10".format(subreddit)
    r = get(URL, headers={'user-agent': 'MyAPI/0.0.1'})
    if r.status_code == 200:
        data = r.json()
        posts = data['data']['children']
        for title in posts[:10]:
            print(title['data']['title'])
    else:
        print(None)
