# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 23:30:20 2022

data_retrieve.py

Retrieve text from the dataset 

@author: Arthur Vinson 


"""

import pandas as pd
import fnmatch
import os

from textblob import TextBlob

import nltk
from nltk.corpus import stopwords


# Construct the path to the dataset folder

year = 2020
subreddit = 'Pathfinder2e'
text = ""
comment_text = pd.DataFrame() # empty DataFrame

base = './my-dataset/'
dirpath = base + str(year)

subredditdirpath = dirpath + '/' + subreddit

submissions_csv_path = str(year) + '-' + subreddit + '-submissions.csv'

full_path = subredditdirpath + '/' + submissions_csv_path

print(full_path)

# load csv

# loads the column with post titles into variable 'title_text'
title_text = pd.read_csv(full_path, usecols = ['title'] )

# loads column with body text into variable 'text'
self_text = pd.read_csv(full_path, usecols = ['selftext'] )

# drop rows with '[removed]' or '[deleted]' strings as values
# (this removes NaN entries too - not sure why)
self_text = self_text[self_text['selftext'].str.contains("\[deleted\]|\[removed\]") == False]


## loads comment text 

# go through each csv file in the path
for filename in os.listdir(subredditdirpath):
    # if filename contains/ends with 'comments'
    if fnmatch.fnmatch(filename, '*comments.csv'):

        comment_csv_filename = subredditdirpath + '/' + filename
        # append column with comment text into variable comment_text
        
        # print(comment_csv_filename)
        
        comment_temp = pd.read_csv(comment_csv_filename, usecols = ['comment_body'])
        
        comment_text = pd.concat([comment_text, comment_temp])
        


# reset indexes
title_text = title_text.reset_index(drop=True)

self_text = self_text.reset_index(drop=True)

comment_text = comment_text.reset_index(drop=True)

# print(title_text)

# print(self_text)

# print(comment_text)


stop_words = set(stopwords.words('english'))

# Need to add custom stop words or a dictionary of ttrpg jargon



input_text = comment_text['comment_body'][7]

print(input_text)

blob_object = TextBlob(input_text)

print(" Word Tokenize :\n", blob_object.words)


print("\n Sentence Tokenize :\n", blob_object.sentences)


print(blob_object.sentiment)


# textblox analysis
# for i in comment_text.index:
#     input_text = comment_text['comment_body'][i]

#     analysis = TextBlob(input_text).sentiment
    
#     print(analysis)





# find the average textblob analysis
# find vader info