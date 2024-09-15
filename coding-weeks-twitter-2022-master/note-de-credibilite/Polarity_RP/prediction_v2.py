from math import floor
from textblob import TextBlob
from collect_replies import replies
from collect_replies import liste_replies
from polarity import frequency_pol_replies
from collect_replies import search


def prediction(F, tweet):  # F les fréquences des polarités moyennes des réponses et id l'identifiant du tweet
    liste_rp = search("in_reply_to_tweet_id:"+tweet["id"])
    if liste_rp == []:
        return None
    else:
        a = 0  # Somme des valeures absolues des polarités des replies
        for reply in liste_rp:
            rp = TextBlob(reply["text"])
            sentiment = rp.sentiment
            polarity = sentiment[0]
            a = a + abs(polarity)
        avg_polarity = a/len(liste_rp)
        k = floor(avg_polarity*10)
        vrais_tweets = 0  # Nombre de vrais tweets
        faux_tweets = 0  # Nombre de faux tweets
        vrais_tweets_proches = 0  # Vrai tweets proches en avg_polarité du tweet en question
        faux_tweets_proches = 0  # Faux tweets proches en avg_polarité du tweet en question
        for i in range(len(F)):
            vrais_tweets = vrais_tweets + F[i][0]
            faux_tweets = faux_tweets + F[i][1]
            if k-1 <= i and k+1 >= i:
                vrais_tweets_proches = vrais_tweets_proches + F[i][0]
                faux_tweets_proches = faux_tweets_proches + F[i][1]
        return ((vrais_tweets_proches/vrais_tweets) - (faux_tweets_proches/faux_tweets))
