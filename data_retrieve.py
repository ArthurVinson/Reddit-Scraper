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

# Construct the path to the dataset folder

year = 2020
subreddit = 'Pathfinder2e'
comment_text = pd.DataFrame() # empty DataFrame

base = './my-dataset/'
dirpath = base + str(year)

subredditdirpath = dirpath + '/' + subreddit

submissions_csv_path = str(year) + '-' + subreddit + '-submissions.csv'

full_path = subredditdirpath + '/' + submissions_csv_path

print(full_path)

# load csv
data = pd.read_csv(full_path)

# # loads the column with post titles into list 'title_text'
# title_text = data['title'].values.tolist()

# # loads column with body text into variable 'self_text'
# self_text = data['selftext'].values.tolist()

# loads the column with post titles into variable 'title_text'
title_df = pd.read_csv(full_path, usecols = ['title'] )

# loads column with body text into variable 'text'
self_df = pd.read_csv(full_path, usecols = ['selftext'] )

# drop rows with '[removed]' or '[deleted]' strings as values
# (this removes NaN entries too - not sure why)
self_df = self_df[self_df['selftext'].str.contains("\[deleted\]|\[removed\]") == False]

# convert dataframes to list

self_text = list(self_df.values.flatten())
title_text = list(title_df.values.flatten())

## loads comment text 

comment_text = []

# go through each csv file in the path
for filename in os.listdir(subredditdirpath):
    # if filename contains/ends with 'comments'
    if fnmatch.fnmatch(filename, '*comments.csv'):
        comment_csv_filename = subredditdirpath + '/' + filename    #variable containing the filename path

        # print(comment_csv_filename)
        # load the csv 
        data = pd.read_csv(comment_csv_filename)

        # convert the column 'comment_body' to a list
        cb = list(data['comment_body'].values.flatten())

        # append to list comment_text
        comment_text.extend(cb)

# create list 'text' to hold entire body of text

text = [] # intialize list

# append lists title_text, self_text and comment_text
text.extend(title_text)
text.extend(self_text)
text.extend(comment_text)


## convert list 'text' to ./my_dataset/textfiles/[subreddit]-[year]-text.csv for later processing

# build the filename as a variable

textdir = base + 'textfiles'

text_filename_path = textdir + '/' + subreddit + '-' + str(year) + '.csv'

# convert list 'text' to dataframe 'text_df'
text_df = pd.DataFrame(text)

print(text_filename_path)

if not os.path.exists(textdir):
    os.makedirs(textdir)


# convert dataframe to csv for later retrieval
text_df.to_csv(text_filename_path)

