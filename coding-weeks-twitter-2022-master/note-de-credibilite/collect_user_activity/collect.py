import tweepy

from credentials import BEARER_TOKEN_JO

client = tweepy.Client(BEARER_TOKEN_JO)


def search(q):  # Donne les résultats d'une recherche pour la quérie q
    client = tweepy.Client(BEARER_TOKEN_JO)  # initialisation de la connexion
    tweets = client.search_recent_tweets(
        q, max_results=100, expansions=['referenced_tweets.id'])  # recherche de 100 tweets
    # une boucle pour mettre le texte en entier pour les retweets
    if tweets.data == None:
        return None
    for i in range(len(tweets.data)):
        tweet_data = tweets.data[i].data
        if "referenced_tweets" in tweet_data and tweet_data["referenced_tweets"][0]["type"] == "retweeted":
            response = client.get_tweet(
                tweet_data["referenced_tweets"][0]["id"])
            original_tweet = response[0]
            tweet_data["text"] = original_tweet.text
        tweets.data[i].data = tweet_data
    return tweets.data  # on renvoie la liste des tweets


def collect_tweets(username):  # collecte les tweets de l’utilisateur
    return search("Ukraine -is:retweet from:"+username)


def collect_rt(username):  # collecte les retweets de l’utilisateur
    return search("Ukraine is:retweet from:"+username)


def collect_liked_tweets(username):  # collecte les tweets likés par
    user = client.get_user(username=username).data
    user_id = user.id
    tweets = client.get_liked_tweets(user_id).data
    final_tweets = []
    if tweets == [] or tweets == None:
        return None
    for tweet in tweets:
        if "Ukraine" in tweet.text or "ukraine" in tweet.text:  # on filtre pour garder les tweets sur l’Ukraine
            final_tweets.append(tweet)
    if final_tweets == []:  # liste vide
        return None
    return final_tweets
