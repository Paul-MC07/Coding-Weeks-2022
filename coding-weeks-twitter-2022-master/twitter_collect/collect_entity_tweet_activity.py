import tweepy
from credentials import BEARER_TOKEN

client = tweepy.Client(BEARER_TOKEN)

# F3E4


def get_retweets_of_candidate(num_candidate):
    # j'obtient la liste des tweets récents de la personne
    response = client.get_users_tweets(
        num_candidate, tweet_fields='created_at')
    return response[0]
