#!/usr/bin/python3


import requests


def number_of_subscribers(subreddit):
    if subreddit:

        url = "https://www.reddit.com/{}/".format(subreddit)
        headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/ahmed_s)"
        }
        responed = requests.get(url, headers=headers, allow_redirects=False)
        results = responed.json().get("data")
        return results.get("subscribers")
    else:
        return 0
