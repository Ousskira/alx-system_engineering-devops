#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""

import requests

def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers)

    try:
        data = response.json()
    except ValueError:
        return 0

    # Check if the subreddit exists
    if response.status_code != 200 or 'data' not in data or 'subscribers' not in data['data']:
        return 0

    return data['data']['subscribers']
