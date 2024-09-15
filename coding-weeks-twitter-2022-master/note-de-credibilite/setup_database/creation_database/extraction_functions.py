import tweepy
from credentials import BEARER_TOKEN


def search(q):  # Donne les résultats d'une recherche pour la quérie q
    client = tweepy.Client(BEARER_TOKEN)  # initialisation de la connexion
    tweets = client.search_recent_tweets(
        q, max_results=100, expansions=['referenced_tweets.id'])  # recherche de 100 tweets #avoir le tweet en entier quand ils sont retweetés
    # une boucle pour mettre le texte en entier pour les retweets, gestion des retweets
    for i in range(len(tweets.data)):
        tweet_data = tweets.data[i].data
        if "referenced_tweets" in tweet_data and tweet_data["referenced_tweets"][0]["type"] == "retweeted":
            response = client.get_tweet(
                tweet_data["referenced_tweets"][0]["id"]) 
            original_tweet = response[0]
            tweet_data["text"] = original_tweet.text #récupère le texte des tweets originaux
        tweets.data[i].data = tweet_data
    return tweets.data  # on renvoie la liste des tweets

