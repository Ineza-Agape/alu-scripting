#!/usr/bin/python3
"""
script that returns the number of subscribers (not active users, total subscribers) for a given subreddit
"""


def number_of_subscribers(subreddit):
    import requests
    req = requests.get("https://api.reddit.com/r/{}/about.json"
                       .format(subreddit),
                       headers={"User-Agent": "MyRedditBot/0.0.1"})
    req = req.json()
    try:
        return req["data"]["subscribers"]
    except Exception as error:
        return 0
