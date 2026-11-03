#!/usr/bin/python3
"""Recursively count keywords in the hot post titles of a subreddit."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print the sorted count of each keyword found in hot post titles."""
    if counts is None:
        counts = {w.lower(): 0 for w in word_list}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/alu_student)"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data", {})
        for post in data.get("children", []):
            title = post.get("data", {}).get("title", "")
            for token in title.lower().split():
                if token in counts:
                    counts[token] += 1
        after = data.get("after")
        if after is not None:
            return count_words(subreddit, word_list, after, counts)
    lowered = [w.lower() for w in word_list]
    results = [(w, c * lowered.count(w)) for w, c in counts.items() if c > 0]
    for word, count in sorted(results, key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(word, count))
