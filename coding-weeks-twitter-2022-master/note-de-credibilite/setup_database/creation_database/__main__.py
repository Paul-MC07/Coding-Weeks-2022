from extraction_functions import *
from tweet_storage import *

query_filter = "lang:en -is:retweet" #sélectionne que des tweets en anglais et pas les retweets
tweets_1 = search("Ukraine "+query_filter)
tweets_2 = search("Ukraine war "+query_filter)
tweets_3 = search("Ukraine zelensky "+query_filter)
tweets_4 = search("Ukraine putin "+query_filter)
#sélection des mots clés recherchés dans les tweets 

tweets = tweets_1 + tweets_2 + tweets_3 + tweets_4

store_tweets(tweets, "data/tweets_collection.json") #stock dans tweets_collection
