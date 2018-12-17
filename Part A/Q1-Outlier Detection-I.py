#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 02:10:57 2018

@author: acggs
"""

import pandas as pd
from pandas import DataFrame
from scipy.stats import zscore


tags=pd.read_csv('data/tags.csv')


cols = list(tags.columns)
cols.remove('movieId')
cols.remove('timestamp')
cols.remove('tag')
tags[cols]

user_freq = tags['userId'].value_counts()

userID=pd.DataFrame(user_freq)

userID.apply(zscore)

tag_freq = tags['tag'].value_counts()

TAGS=pd.DataFrame(tag_freq)

TAGS.apply(zscore)