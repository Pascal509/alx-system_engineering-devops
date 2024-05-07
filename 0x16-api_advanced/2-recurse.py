#!/usr/bin/python3
"""
Module to recursively fetch the titles of all hot articles
for a specified subreddit using Reddit's API.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API for all hot articles of a
    subreddit and returns their titles.

    Args:
    subreddit (str): The subreddit to query.
    hot_list (list, optional): Accumulator list to store article titles.
    after (str, optional): Paginator identifier for the next page of articles.

    Returns:
    list: List of titles of hot articles or None if subreddit is invalid.
    """
    # Base URL for the subreddit's hot posts in JSON format
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    # Set up headers to include a custom User-Agent
    headers = {'User-Agent': 'custom-user-agent'}
    # Include the 'after' parameter if provided for pagination
    params = {'limit': 100, 'after': after}
    # Make the request to the Reddit API
    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
            )
        if response.status_code != 200:
            return None
        # Parse JSON data from the response
        data = response.json()
        # Check if data contains 'data' key and has posts
        if 'data' not in data or 'children' not in data['data']:
            return None
        # Extract article titles and update the hot_list
        posts = data['data']['children']
        hot_list.extend([post['data']['title'] for post in posts])
        # Check if there is a next page using the 'after' key in data
        after = data['data'].get('after', None)
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except requests.RequestException:
        return None
