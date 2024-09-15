import collect_user_activity.collect as clt
import json
from pathlib import Path
from frequence.frequence_mots import frequence_finale
from frequence.prediction_v1 import pourcentage_fake


def conversion_tweets_dicts(tweets_list):
    if tweets_list == None or tweets_list == []:
        return None
    return [tweet.data for tweet in tweets_list]


def notation(username, filepath_database):
    user_tweets_response = clt.collect_tweets(username)
    user_tweets = conversion_tweets_dicts(user_tweets_response)
    user_retweets = conversion_tweets_dicts(clt.collect_rt(username))
    user_liked_tweets = conversion_tweets_dicts(
        clt.collect_liked_tweets(username))

    fp = open(Path(filepath_database), 'r', encoding="utf-8")
    tweets_database = json.load(fp)

    dict_frequences = frequence_finale(tweets_database)
    pourcentage_tweets = pourcentage_fake(dict_frequences, user_tweets)
    pourcentage_retweets = pourcentage_fake(dict_frequences, user_retweets)
    pourcentage_likes = pourcentage_fake(dict_frequences, user_liked_tweets)

    denominateur = 0
    numerateur = 0
    note_tweets = None
    note_retweets = None
    note_likes = None
    if pourcentage_tweets != None:
        denominateur += 0.5
        numerateur += 0.5*(1-pourcentage_tweets)
        note_tweets = (1-pourcentage_tweets)*5
    if pourcentage_retweets != None:
        denominateur += 0.3
        numerateur += 0.3*(1-pourcentage_retweets)
        note_retweets = (1-pourcentage_retweets)*3
    if pourcentage_likes != None:
        denominateur += 0.2
        numerateur += 0.2*(1-pourcentage_likes)
        note_likes = (1-pourcentage_likes)*2

    if denominateur == 0:
        return (None, None, None, None)
    return (10*numerateur/denominateur, note_tweets, note_retweets, note_likes)


def afficher_note():
    username = input("Username : ")
    (note_finale, note_tweets, note_rt, note_likes) = notation(
        username, "data/tweets_collection.json")
    print("Note totale : " + str(note_finale) + "/10")
    print("Note tweets : " + str(note_tweets) + "/5")
    print("Note retweets : " + str(note_rt) + "/3")
    print("Note likes : " + str(note_likes) + "/2")


afficher_note()
