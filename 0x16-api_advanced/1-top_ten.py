#!/usr/bin/python3
"""
Module to fetch and print the titles of the first 10 hot
posts of a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API for the titles of the top 10 hot
    posts of a subreddit.

    Args:
    subreddit (str): The subreddit to query.

    """
    # URL for the subreddit's hot posts in JSON format
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    # Set up headers to include a custom User-Agent
    headers = {'User-Agent': 'custom-user-agent'}
    # Make the request to the Reddit API
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Raises an exception for HTTP error codes if any
        response.raise_for_status()
        # Parse JSON data from the response
        data = response.json()
        # Check JSON response have the expected 'data' and 'children' keys
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        # Handles any request errors, including HTTPError,
        # and print None if error occurs
        print(None)
