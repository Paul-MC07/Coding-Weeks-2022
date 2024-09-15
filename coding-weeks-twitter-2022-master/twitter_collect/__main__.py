from collect_entity_tweet_activity import get_retweets_of_candidate
from collect_entity_actuality_tweets import get_candidate_queries, search, get_tweets_from_candidates_search_queries
import tweepy
from credentials import BEARER_TOKEN
from tweet_collection import *

client = tweepy.Client(BEARER_TOKEN)


def collect(id, file_path):
    queriesk = get_candidate_queries(id, file_path, "keywords")
    queriesh = get_candidate_queries(id, file_path, "hashtags")
    tweets_keywords = get_tweets_from_candidates_search_queries(queriesk)
    tweets_hashtags = get_tweets_from_candidates_search_queries(queriesh)
    retweets = get_retweets_of_candidate(id)
    return {"tweets_k": tweets_keywords, "tweets_h": tweets_hashtags, "rt": retweets}


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
