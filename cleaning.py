# -*- coding: utf-8 -*-
"""
Data Cleaning for NLP

https://towardsdatascience.com/nlp-in-python-data-cleaning-6313a404a470

Created on Fri May 27 11:05:51 2022

@author: Arthur Vinson

Inspired by https://levelup.gitconnected.com/reddit-sentiment-analysis-with-python-c13062b862f6
"""

# imports


import cleantext
import pandas as pd
import re
import emoji
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords

# load up text csv

year = 2020
subreddit = 'Pathfinder2e'

base = './my-dataset/'
textdir = base + 'textfiles'

text_filename_path = textdir + '/' + subreddit + '-' + str(year) + '.csv'

stop = stopwords.words('english')


data = pd.read_csv(text_filename_path)[['0']]

# rename column '0' to 'text'

data.rename(columns={'0':'text'}, inplace=True)

# create new column in data DF named 'tb sentiment', fill it with the TextBlob sentiment analysis of the 'text' column

data['tb sentiment'] = data['text'].apply(lambda raw: TextBlob(raw).sentiment)

data['tb polarity'] = data['text'].apply(lambda raw: TextBlob(raw).polarity)

data['tb subjectivity'] = data['text'].apply(lambda raw: TextBlob(raw).subjectivity)


tot

# sentiment is just a two floats.






# # convert list 'text' to string object

# list1 = text

# list1 = [str(i) for i in list1] # map to a list of strings

# raw = ' , '.join(list1)  #join all the strings separated by a comma

# # remove emojis

# string_emojiless = emoji.demojize(raw)


# # remove urls

# no_urls = re.sub(r'http?\S+', '', string_emojiless)

# # remove linebreaks

# no_linebreaks = no_urls.replace('\n', '')

# # lower case

# lower_case = no_linebreaks.lower()

# # remove stopword

# blob = TextBlob(lower_case)



# # tokenize

# #text_obj = TextBlob(clean_text)

# #words_obj = blob.words

# sentence_obj = blob.sentences


# # remove stopwords

# # text_obj2 = [x for x in text_obj if x not in stop]


# # normalize words via lemmatizing




# # print(text_obj.sentiment)
# # print(text_obj.sentiment_assessments)


# # visualize word counts

# frequency = text_obj.word_counts.items()

# items_arg = text_obj.word_counts.items()

# items = [item for item in frequency if item[0] not in nltk.corpus.stopwords.words('english')]

