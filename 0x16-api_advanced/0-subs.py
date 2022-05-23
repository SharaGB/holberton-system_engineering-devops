#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
from requests import get


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers """
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = get(URL, headers={'User-Agent': 'MyAPI'})
    if r.status_code == 200:
        data = r.json()
        return data['data']["subscribers"]
    else:
        return 0
