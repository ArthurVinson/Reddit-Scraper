# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 20:55:13 2022

Sentiment Analysis of Reddit Headlines

@author: Arthur Vinson
"""

import pandas as pd

# grab the headlines from reddit || load csv of reddit scrapings
# analyze the headlines, find the average (sum of VALUE)/(# of VALUES)

df = pd.read_csv('file.csv')

for row in df.index:
    print(f'Row {row}')
