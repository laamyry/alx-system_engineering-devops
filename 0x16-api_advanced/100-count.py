#!/usr/bin/python3
'''Count it!'''
import requests


def count_words(subreddit, word_list, instances={}, after="", counter=0):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "med_laamyry"}
    params = {"after": after, "counter": counter, "limit": 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code != 200:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    counter += results.get("dist")
    for m in results.get("children"):
        title = m.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print(f"{k}: {v}") for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, counter)
