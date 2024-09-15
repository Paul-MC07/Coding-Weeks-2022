import json
from pathlib import Path


# fonction qui permettra d’évaluer à la chaîne les tweets
def evaluate(stored_tweets_filepath, starting_index):
    path_tweets = Path(stored_tweets_filepath)
    # on transforme le JSON en dataframe pandas
    file_read = open(path_tweets, 'r', encoding="utf-8")
    tweets_list = json.load(file_read)  # on charge le JSON dans tweets_list
    for i in range(starting_index, len(tweets_list)):  # on parcourt tweets_list
        tweet = tweets_list[i]
        reponse = 'a'
        if "fake_news" not in tweet:  # si on a pas déjà évalué ce tweet
            while reponse not in ['y', 'n', 'q']:
                reponse = input("Tweet ID : " + str(tweet["id"]) + "\n\nTexte du tweet : " +
                                tweet["text"] + "\n\nCe tweet relaie-t-il une fake news (y/n/q) ?\n")
                if reponse == 'q':
                    break  # on quitte le programme
                elif reponse == 'y':  # c’est une fake news
                    tweet["fake_news"] = True
                elif reponse == 'n':  # ce n’est pas une fake news
                    tweet["fake_news"] = False
        if reponse == 'q':  # on quitte le programme
            break
        tweets_list[i] = tweet
    file = open(path_tweets, 'w', encoding="utf-8")
    json.dump(tweets_list, file, ensure_ascii=False)
