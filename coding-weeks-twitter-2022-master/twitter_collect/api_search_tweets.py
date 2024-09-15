import twitter_connection_setup
from credentials import BEARER_TOKEN
import tweepy


def collect():
    connexion = tweepy.Client(BEARER_TOKEN)
    tweets = connexion.search_recent_tweets(
        "Emmanuel Macron")
    for tweet in tweets[0]:
        print(tweet.text)
    return tweets[0]
