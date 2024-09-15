import tweepy
from credentials import BEARER_TOKEN

client = tweepy.Client(BEARER_TOKEN)

user_id = 1976143068             #ici c'est le id de macron

response = client.get_users_tweets(user_id)
for tweet in response.data:
    print(tweet.id)
    print(tweet.text)