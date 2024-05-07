#!/usr/bin/python3
"""
Module to count words appearing in titles of hot
posts in a specified subreddit.
"""
import requests
import re
from collections import Counter


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively fetch titles of hot posts from subreddit and
    count occurrences of each keyword.

    Args:
    subreddit (str): Subreddit name to query.
    word_list (list): List of words to count occurrences of.
    after (str, optional): Paginator token for next set of posts.
    counts (Counter, optional): Accumulator for word counts across
    recursive calls.

    Prints:
    Words and their counts in specified format if posts are found
    and subreddit is valid.
    """
    if counts is None:
        counts = Counter()
        word_list = [word.lower() for word in word_list]
    # Base URL for the subreddit's hot posts in JSON format
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    # Set up headers to include a custom User-Agent
    headers = {'User-Agent': 'custom-user-agent'}
    params = {'limit': 100, 'after': after}
    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
            )
        if response.status_code != 200:
            return  # Do nothing if invalid subreddit
        data = response.json()
        posts = data['data']['children']
        after = data['data']['after']
        # Process titles, count occurrences of each keyword
        for post in posts:
            title = post['data']['title'].lower()
            # Split title into words
            words_in_title = re.findall(r'\b\w+\b', title)
            counts.update(word for word in words_in_title if word in word_list)
        if after is not None:
            count_words(subreddit, word_list, after, counts)
        elif counts:
            sorted_counts = sorted(
                counts.items(),
                key=lambda item: (-item[1], item[0])
                )
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")
    except requests.RequestException:
        pass
