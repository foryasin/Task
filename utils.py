import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
import redis

# We get the url
r = requests.get("https://securityforeveryone.com/")
soup = BeautifulSoup(r.content, features="html.parser")

# We get the words within paragraphs
text_p = [''.join(s.findAll(text=True)) for s in soup.findAll('p')]
c_p = Counter((x.strip(punctuation).lower() for y in text_p for x in y.split()))


# We sum the two counter and get a list with words count from most to less common
total = c_p


def count_total():
    print(f"Total word count --> {sum(total.values())}")


def count_each_word(word: str):
    dict_for_redis = {}

    for word, number in total.most_common(len(total)):
        dict_for_redis[word] = number
        
    redis_key = redis.Redis()
    redis_key.mset(dict_for_redis)  # msetnx --> if you don't want to overwrite existing values.
    print(redis_key)






