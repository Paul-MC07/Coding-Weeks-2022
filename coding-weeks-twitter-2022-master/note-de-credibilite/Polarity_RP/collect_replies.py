import tweepy
from credentials import BEARER_TOKEN


def conversion_tweet_dict(L):
    return [tweet.data for tweet in L]


def search(q):  # Donne les résultats d'une recherche pour la quérie q
    # initialisation de la connexion
    client = tweepy.Client(BEARER_TOKEN, wait_on_rate_limit=True)
    tweets = client.search_recent_tweets(
        q, max_results=100, expansions=['referenced_tweets.id'])  # recherche de 100 tweets
    # une boucle pour mettre le texte en entier pour les retweets
    if tweets.data == None:
        return []
    for i in range(len(tweets.data)):
        tweet_data = tweets.data[i].data
        if "referenced_tweets" in tweet_data and tweet_data["referenced_tweets"][0]["type"] == "retweeted":
            response = client.get_tweet(
                tweet_data["referenced_tweets"][0]["id"])
            original_tweet = response[0]
            tweet_data["text"] = original_tweet.text
        tweets.data[i].data = tweet_data
    return conversion_tweet_dict(tweets.data)  # on renvoie la liste des tweets


def replies(tweet):
    reply = search("in_reply_to_tweet_id:"+tweet["id"])
    return reply


def liste_replies(L):  # A partir de la liste L de tweets je vais faire une liste de liste de replies, avec la sous-liste i étant les reply pour le tweet i
    liste_rp = []
    for tweet in L:
        rp = replies(tweet)
        liste_rp.append(rp)
    return liste_rp
