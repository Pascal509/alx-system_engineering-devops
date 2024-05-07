#!/usr/bin/python3
"""
Module to fetch the number of subscribers for a specified
subreddit using Reddit's API.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for the number of subscribers to a subreddit.

    Args:
    subreddit (str): The subreddit to query.

    Returns:
    int: The number of subscribers to the subreddit, or 0 if
    the subreddit is invalid.
    """
    # URL for the subreddit's about page in JSON format
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    # Set up headers to include a custom User-Agent
    headers = {'User-Agent': 'custom-user-agent'}
    # Make the request to the Reddit API
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raises an exception for HTTP error codes
        # Parse JSON data from the response
        data = response.json()
        # Check if the JSON response contains the expected 'data' key
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0  # No subscriber data found
    except requests.RequestException:
        return 0  # Handles any request errors, including HTTPError
