from .frequence_mots import rmduplicates


def prediction(F, tweet):  # F est le dictionnaire des fréquences pour chaque mot et tweet le dictionnaire correspondant à un tweet
    mots = tweet["text"].split()
    listemots = rmduplicates(mots)
    s = 0
    f = 0  # nombre de mots dans des tweets faux
    t = 0  # pareil pour les tweets vrais
    for mot in F:
        # t est la somme de nombre de mots dans les tweets vrais répertoriés dans F
        t = F[mot][0] + t
        # f est la somme de nombre de mots dans les tweets faux répertoriés dans F
        f = F[mot][1] + f
    for mot in listemots:
        if mot in F:
            # j'ajoute la fréquence de ce mot dans les tweets vrais et je soustrait la féquence de ce mot dans les faux tweets
            s = s + (F[mot][0]/t) - (F[mot][1]/f)
    return (s)  # renvoie la proba que le tweet soit vrai


def pourcentage_fake(F, liste_tweet):
    nbre_fake = 0
    if liste_tweet == [] or liste_tweet == None:
        return None
    for tweet in liste_tweet:
        if prediction(F, tweet) <= 0:
            nbre_fake += 1  # compte le nombre de fake news presentes dans la liste de tweets proposée
    # renvoie le pourcentage de fake news d'un utilisateur
    return nbre_fake/len(liste_tweet)
