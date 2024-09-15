from textblob import TextBlob
from math import floor
from collect_replies import replies
from collect_replies import liste_replies


# liste_rp une liste, et liste_rp[i] une liste de reply au tweet L[i], donc en gros une liste de dictionnaires avec chaque dictionnaire étant un reply
def polarity_replies(L):
    liste_rp = liste_replies(L)
    for i in range(len(liste_rp)):
        if liste_rp[i] == []:
            L[i]["polarity_replies"] = None
        else:
            a = 0  # Somme des valeures absolues des polarités des replies
            for reply in liste_rp[i]:
                rp = TextBlob(reply["text"])
                sentiment = rp.sentiment
                polarity = sentiment[0]
                a = a + abs(polarity)
            # Moyenne des valeure absolue des polarités des réponses
            avg_polarity = a/len(liste_rp[i])
            # J'ajoute au dictionnaire de la base de données avg_polarity
            L[i]["polarity_replies"] = avg_polarity
    return L


def tweets_with_replies(L):
    K = polarity_replies(L)
    liste_tweets_with_rp = []
    for tweet in K:
        if tweet["polarity_replies"] != None:
            liste_tweets_with_rp.append(tweet)
    return liste_tweets_with_rp


def frequency_pol_replies(L):
    liste_tweets = tweets_with_replies(L)
    F = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
         [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], ]
    for tweet in liste_tweets:
        k = floor(tweet["polarity_replies"]*10)
        # F[i][1] nombre de faux tweets ayant une avg_polarity entre i/10 et (i/10 + 0.1)
        if tweet["fake_news"]:
            F[k][1] = F[k][1] + 1
        # F[i][0] nombre de vrais tweets ayant une avg_polarity entre i/10 et (i/10 + 0.1)
        else:
            F[k][0] = F[k][0] + 1
    return F
