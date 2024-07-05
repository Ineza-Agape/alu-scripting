#!/usr/bin/python3

"""
Script that Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests
def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'myRedditApp/0.0.1' }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    except Exception as error:
        print(None)
