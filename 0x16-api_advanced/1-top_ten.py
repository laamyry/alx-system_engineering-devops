#!/usr/bin/python3
'''Top Ten'''
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers={"User-Agent": "MyRedditApp/1.0"})
    if response.status_code != 200:
        print(None)
        return
    else:
        data = response.json()
        for m in range(10):
            print(data["data"]["children"][m]['data']['title'])
        return
