from math import ceil
from .frequence_mots import epuration
from .prediction_v1 import prediction
import json
from pathlib import Path


def reliability1(L):
    n = len(L)
    tr = ceil(n*0.8)
    liste_training = L[:tr]
    F = epuration(liste_training)
    a = 0  # la variable qui va contenir la somme des valeures absolues des différences entre la valeure de notre base de données et la vraie valeure
    for i in range(tr, n):
        k = prediction(F, L[i])
        if L[i]["fake_news"]:  # Selon notre échelle de prédiction, la valeure de v est -1 si le tweet est fake et 1 s'il est vrai
            v = -1
        else:
            v = 1
        a = a + abs(k-v)
    # On renvoit la moyenne des différences en valeure absolue entre la vraie valeure et la valeure prédite
    return (a/(n-tr))

# Si on trouve <1, c'est déjà bien parce que ça voudra dire qu'en moyenne on est du bon coté.


def reliability2(L):
    n = len(L)
    tr = ceil(n*0.8)
    liste_training = L[:tr]
    F = epuration(liste_training)
    bonnes_predictions = 0  # nombre de bonnes prédiction
    for i in range(tr, n):
        if L[i]["fake_news"]:
            # On considère que la prédiction est bonne pour un fake si la prédiction donne <-0.1
            if prediction(F, L[i]) < 0:
                bonnes_predictions = bonnes_predictions+1
        else:
            # On considère que la prédiction est bonne pour un vrai si la prédiction donne >0.1
            if prediction(F, L[i]) >= 0:
                bonnes_predictions = bonnes_predictions+1
    return (bonnes_predictions/(n-tr))  # On renvoit le nombre de fois

# La on aimerais au moins plus de 50% de réussite


def reliability3(L):
    n = len(L)
    tr = ceil(n*0.8)
    liste_training = L[:tr]
    F = epuration(liste_training)
    bonnes_predictions = 0  # nombre de bonnes prédiction
    # donne le nombre de prédictions de valeure absolue supérieure à 0.1
    nombre_prédictions = 0
    for i in range(tr, n):
        if prediction(F, L[i]) > 0.01 or prediction(F, L[i]) < -0.01:
            nombre_prédictions = nombre_prédictions + 1
            if L[i]["fake_news"] and prediction(F, L[i]) < -0.01:
                bonnes_predictions = bonnes_predictions + 1
            elif not L[i]["fake_news"] and prediction(F, L[i]) > 0.01:
                bonnes_predictions = bonnes_predictions + 1
    # On renvoit le nombre de fois
    return (bonnes_predictions/nombre_prédictions, nombre_prédictions/(n-tr))

# Ce test est pour les prédictions plus assurées, qui devraient etre plus sures. On espère donc un assez bon score


fp = open(Path("data/tweets_collection.json"), 'r', encoding="utf-8")
tweets_database = json.load(fp)
print(reliability1(tweets_database))
print(reliability2(tweets_database))
print(reliability3(tweets_database))
