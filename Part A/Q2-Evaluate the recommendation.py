#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 03:30:55 2018

@author: acggs
"""

import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt





ratings=pd.read_csv('data/ratings.csv')

user_freq = ratings['userId'].value_counts()
movie_freq = ratings['movieId'].value_counts()
ratings_freq = ratings.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)

dummy=pd.read_csv('data/recommendation.data')


dummy_freq = ratings.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)



#Root Mean Square Error
rms = sqrt(mean_squared_error(ratings_freq, dummy_freq))