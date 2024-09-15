from __main__ import collect
from tweet_collection import *
import tweepy

tweets = [tweepy.Tweet(
    {"text": "un premier tweet intéressant d'exemple sur Macron", "id": 1, "created_at": "2022-01-30T15:32:55.0Z"}),
    tweepy.Tweet(
    {"text": "un deuxième tweet sur la guerre en #Ukraine",
        "id": 2, "created_at": "2022-01-31T11:15:28.0Z"}
)]
# store_tweets(collect(1976143068, "CandidateData/")
# ["tweets_k"], "CandidateData/saved_tweets.json")
store_tweets(collect(1976143068, "CandidateData/")
             ["tweets_k"][0], "CandidateData/saved_tweets.json")
