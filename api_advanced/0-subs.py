#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and
returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit,
        or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/126.0.0.0 Safari/537.36')
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        return response.json().get('data', {}).get('subscribers', 0)
    except Exception:
        return 0


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
