import json
from pathlib import Path


# stocke une liste de tweets dans le fichier indiqué par filename (fichier JSON)
def store_tweets(tweets, filename):
    f = open(Path(filename), 'w', encoding="utf-8")
    l = [{k: tweet.data[k] for k in tweet.data if k in [
        "text", "author_id", "id", "entities", "created_at"]} for tweet in tweets]
    json.dump(l, f, ensure_ascii=False)
    f.close()
