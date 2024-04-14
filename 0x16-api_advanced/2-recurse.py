import requests

def recurse(subreddit, hot_list=None, after=None):
    """Recursively retrieve the titles of all hot articles for a given subreddit."""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditApp/1.0.0 (by /u/MyUsername)"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for non-200 status codes
        data = response.json().get("data", {})
        children = data.get("children", [])

        for child in children:
            title = child.get("data", {}).get("title")
            hot_list.append(title)

        after = data.get("after")

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list if hot_list else None

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

# Test the function
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
