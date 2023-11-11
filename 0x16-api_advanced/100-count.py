#!/usr/bin/python3
'''Count it!'''
import requests


def count_words(subreddit, word_list, f_list=[], after=None):
    user_agent = {"User-Agent": "med_laamyry"}
    url = f"http://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    psts = requests.get(url, headers=user_agent)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if psts.status_code == 200:
        psts = psts.json()["data"]
        af = psts["after"]
        psts = psts["children"]
        for post in psts:
            title = post["data"]["title"].lower()
            for word in title.split(" "):
                if word in word_list:
                    f_list.append(word)
        if af is not None:
            count_words(subreddit, word_list, f_list, af)
        else:
            result = {}
            for word in f_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print(f"{key}: {value}")
    else:
        return
