#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditApp/1.0.0 (by /u/MyUsername)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an error for non-200 status codes
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return 0
