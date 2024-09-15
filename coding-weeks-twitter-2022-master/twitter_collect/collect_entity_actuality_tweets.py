import twitter_connection_setup
import tweepy
from credentials import BEARER_TOKEN
from pathlib import Path


def get_candidate_queries(num_candidate, file_path, type):
    """
    Fonctionnalité 3, étape 1
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    try:
        if type == "keywords":
            f = open(
                Path(file_path)/f"keywords_candidate_{num_candidate}.txt", 'r', encoding="utf-8")
            queries = f.readlines()  # queries contient la liste des mots-clés
            for i in range(0, len(queries)):
                if queries[i][-1] == '\n':
                    queries[i] = queries[i][:-1]  # on enlève 'n'
            return queries

        elif type == "hashtags":
            f = open(
                Path(file_path)/f"hashtags_candidate_{num_candidate}.txt", 'r', encoding="utf-8")
            queries = f.readlines()  # queries contient la liste des hashtags
            for i in range(0, len(queries)):
                if queries[i][-1] == '\n':
                    queries[i] = queries[i][:-1]
                # on rajoute '#' en début de mot en on enlève '\n'
                queries[i] = "#" + queries[i]
            return queries  # on renvoie la liste des hashtags

        else:
            print("Errer : mauvais argument 'type'")
            return None

    except IOError:
        print("Erreur : fichier introuvable")


# F3E2


def search(q):  # Donne les résultats d'une recherche pour la quérie q
    connexion = tweepy.Client(BEARER_TOKEN)
    tweets = connexion.search_recent_tweets(
        q, tweet_fields=['created_at', 'entities', 'author_id'])
    return tweets.data  # on renvoie la liste des tweets


# Donne les résultats pour une liste de queries
# renvoie une liste de réponses aux requêtes
def get_tweets_from_candidates_search_queries(queries):
    list_tweets = [search(q) for q in queries]
    return list_tweets
