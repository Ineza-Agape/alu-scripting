#!/usr/bin/python3
"""
This module contains functions for processing data from Reddit API.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Fetches the number of subscribers for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit (without '/r/').

    Returns:
    - int: Number of subscribers of the subreddit.
           Returns 0 if there's an error or the subreddit doesn't exist.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "myRedditApp/0.0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        else:
            return 0

    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
