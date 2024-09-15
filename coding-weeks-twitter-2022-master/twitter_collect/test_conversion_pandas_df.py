from api_search_tweets import collect
from pytest import *
import json


def test_collect():
    tweets = collect()
    data = transform_to_dataframe(tweets)
    assert 'tweet_textual_content' in data.columns
