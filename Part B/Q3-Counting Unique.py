import json
from pandas.io.json import json_normalize
import pandas as pd
import hyperloglog

tweets = []
for line in open('data/tweets.json.1', 'r', encoding='latin-1'):
    tweets.append(json.loads(line))
print('before data')
data=json_normalize(tweets)

count_hasht = hyperloglog.HyperLogLog(0.01) #ERROR MARGIN

for hashtags in data['entities.hashtags']:
    
    hashtag = json_normalize(hashtags)
    if hashtags!=[]:
        for index, hashtag_text in hashtag.iterrows():
            count_hasht.add(hashtag_text['text'].lower().encode("utf-8"))

print ('The HyperLogLog contains ',len(count_hasht),' unique items for error margin 0.01')

count_hasht = hyperloglog.HyperLogLog(0.1) #ERROR MARGIN

for hashtags in data['entities.hashtags']:
    
    hashtag = json_normalize(hashtags)
    if hashtags!=[]:
        for index, hashtag_text in hashtag.iterrows():
            count_hasht.add(hashtag_text['text'].lower().encode("utf-8"))

print ('The HyperLogLog contains ',len(count_hasht),' unique items for error margin 0.1')