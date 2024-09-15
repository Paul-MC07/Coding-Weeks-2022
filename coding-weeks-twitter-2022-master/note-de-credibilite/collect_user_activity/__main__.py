import tweepy
from collect import *


def collect_user(username):
    tweets_user = collect_tweets(username)
    rt_user = collect_rt(username)
    liked_tweets = collect_liked_tweets(username)
    return (tweets_user, rt_user, liked_tweets)
