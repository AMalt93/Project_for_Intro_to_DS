import json
from pandas.io.json import json_normalize
import pandas as pd
import sys
from countminsketch import CountMinSketch
from sklearn.metrics import mean_squared_error, mean_absolute_error

import matplotlib.pyplot as plt


def data_sketching(stream, sketch):
    tag_counter = {}
    for hashtags in data['entities.hashtags']:
    
        hashtag = json_normalize(hashtags)
        if hashtags!=[]:
            for index, hashtag_text in hashtag.iterrows():
                if hashtag_text['text'].lower() in tag_counter:
                    tag_counter[hashtag_text['text'].lower()]+=1
                else:
                    tag_counter[hashtag_text['text'].lower()]=1
                sketch.add(hashtag_text['text'].lower())
    print('size of counter =',sys.getsizeof(tag_counter))
    print('size of sketch =',sys.getsizeof(sketch.tables))

    tag_count_df = pd.DataFrame(list(tag_counter.items()), columns=['tag','count']) 
    tag_count_df.to_csv("data/tag-counter.csv", sep=',',index=False)

    sketch_list = []
    for key in tag_counter:
        sketch_list.append(sketch[key])

    tag_count_df['countmin']=sketch_list
    return tag_count_df





def metrics_and_plotting(tag_count_df):
    mean_ratio = (tag_count_df['countmin']/tag_count_df['count']).mean()

    rmse = mean_squared_error(tag_count_df['count'], tag_count_df['countmin'])
    mae = mean_absolute_error(tag_count_df['count'], tag_count_df['countmin'])
    
    print('mean_ratio =', mean_ratio)
    print('rmse = ', rmse)
    print('mae = ', mae)
    
    actual_count = tag_count_df['count'].sort_values(ascending=False).reset_index(drop=True)
    
    count_min_sketch = tag_count_df['countmin'].sort_values(ascending=False).reset_index(drop=True)
    
    plt.title('Plot 1')
    plt.plot(actual_count, linewidth=5, label="Actual Count")
    plt.plot(count_min_sketch,color='red', label="Count-Min Sketch")
    plt.legend()
    plt.show()
    plt.gcf().clear()
    
    plt.title('Plot with log scaling')
    plt.plot(actual_count, linewidth=5, label="Actual Count")
    plt.plot(count_min_sketch,color='red', label="Count-Min Sketch")
    plt.yscale('log')
    plt.legend()
    plt.show()
    

tweets = []
for line in open('data/tweets.json.1', 'r', encoding='latin-1'):
    tweets.append(json.loads(line))
data=json_normalize(tweets)

choices = [(100000,10),
           (10000,10),
           (1000,10),
           (1000, 100),
           (1000, 5)]

for i in choices:
    sketch = CountMinSketch(i[0], i[1] )
    print('\nData for CountMinSketch(',i[0],',',i[1],')\n')
    tag_count_df = data_sketching(data,sketch)
    metrics_and_plotting(tag_count_df)

#sketch = CountMinSketch(10000, 10)
#
#tag_count_df = data_sketching(data,sketch)
#metrics_and_plotting(tag_count_df)


