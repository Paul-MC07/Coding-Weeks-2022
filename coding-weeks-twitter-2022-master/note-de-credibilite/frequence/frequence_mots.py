import pandas as pd


def rmduplicates(L):  # Petite fonction pour enlever les doublons dans une liste L
    a = 0
    liste = []
    for i in range(len(L)):
        a = 0
        for j in range(i+1, len(L)):
            if L[i] == L[j]:
                a = a+1
        if a == 0:
            liste.append(L[i])
    return liste


def frequence(L):  # L est la liste de tweets et de les tweets sous forme de dictionnaire
    F = {}  # Dictionnaire avec comme clés les mots et
    for d in L:
        text = d["text"].replace(",", "")
        text = text.replace(";", "")
        text = text.replace("?", " question")
        text = text.replace(".", "")
        text = text.replace("!", " exclamation")
        text = text.replace("[", "")
        text = text.replace("]", "")
        text = text.replace('"', "")
        text = text.lower()
        mots = text.split()
        # liste est la liste de mots dans le tweet donc liste[i] est un mot du tweet
        listemots = rmduplicates(mots)
        for i in range(len(listemots)):  # liste qui ajoute 1 à la féquence du mot
            if listemots[i] in F:
                if d["fake_news"]:  # Si c'est fake
                    F[listemots[i]][1] = F[listemots[i]][1] + 1
                else:  # Si c'est vrai
                    F[listemots[i]][0] = F[listemots[i]][0] + 1
            else:
                if d["fake_news"]:  # Si c'est fake
                    F[listemots[i]] = [0, 1]
                else:  # Si c'est vrai
                    F[listemots[i]] = [1, 0]
    return F


def epuration(L):
    F = frequence(L)
    n = len(L)
    Tchao = []
    for mot in F:
        if (F[mot][0]/n < 0.08 and F[mot][1]/n < 0.08) or (F[mot][0]/n > 0.8 and F[mot][1]/n > 0.8):
            Tchao.append(mot)
    for mot in Tchao:
        F.pop(mot)
    return F


def frequence_finale(L):
    F = pd.DataFrame(epuration(L))
    return F
