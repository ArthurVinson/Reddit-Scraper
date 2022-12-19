# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 21:53:05 2021

@author: Arthur Vinson
"""

# Tutorial from https://www.learndatasci.com/tutorials/sentiment-analysis-reddit-headlines-pythons-nltk/

from IPython import display
import math
from pprint import pprint
import pandas as pd
import numpy as np
import nltk
import matplotlib.pyplot as plt
import seaborn as sns

from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords

sns.set(style='darkgrid', context='talk', palette='Dark2')

tokenizer = RegexpTokenizer(r'\w+')
stop_words = stopwords.words('english')

def process_text(headlines):
    tokens = []
    for line in headlines:
        toks = tokenizer.tokenize(line)
        toks = [t.lower() for t in toks if t.lower() not in stop_words]
        tokens.extend(toks)
    
    return tokens

import praw

# create a reddit instance
reddit = praw.Reddit(client_id='LK_PUjO05BqFSg', client_secret='FuE_G7UhRkvIsVNurMuo0VMO3J85ug', user_agent='scraper project')

# define a subreddit
subr = 'Reformed'

# defining a set for headlines, so to not get deplicates when running multiple times

headlines = set()


# iterate through subreddit

for submission in reddit.subreddit(subr).new(limit=None):
    headlines.add(submission.title)
    display.clear_output()
#    print(len(headlines))
    
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA ()
results = []

for line in headlines:
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = line
    results.append(pol_score)
    
pprint(results[:3], width=100)

df = pd.DataFrame.from_records(results)
df.head()

df['label'] = 0
df.loc[df['compound'] > 0.2, 'label'] = 1
df.loc[df['compound'] < -0.2, 'label'] = -1
df.head()

df2 = df[['headline','label']]
df2.to_csv('reddit_headlines_labels.csv', mode='a', encoding='utf-8', index=False)

print("Positive headlines:\n")
pprint(list(df[df['label'] == 1].headline)[:5], width=200)

print("Negative headlines:\n")
pprint(list(df[df['label'] == -1].headline)[:5], width=200)
     
     
# Check how many total positives and negatives in this dataset

print(df.label.value_counts())
print(df.label.value_counts(normalize=True) * 100)

#plot a bar chart of results

fig, ax = plt.subplots(figsize=(8, 8))

counts = df.label.value_counts(normalize=True) * 100

sns.barplot(x=counts.index, y=counts, ax=ax)

ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
ax.set_ylabel("Percentage")

plt.show()

# grab positively labeled headlines - get the most common words in those headlines

pos_lines = list(df[df.label == 1].headline)

pos_tokens = process_text(pos_lines)
pos_freq = nltk.FreqDist(pos_tokens)

print(pos_freq.most_common(20))

y_val = [x[1] for x in pos_freq.most_common()]

fig = plt.figure(figsize=(10,5))
plt.plot(y_val)

plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Word Frequency Distribution (Positive)")
plt.show()

neg_lines = list(df2[df2.label == -1].headline)

neg_tokens = process_text(neg_lines)
neg_freq = nltk.FreqDist(neg_tokens)

print(neg_freq.most_common(20))

y_val = [x[1] for x in neg_freq.most_common()]

fig = plt.figure(figsize=(10,5))
plt.plot(y_val)

plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Word Frequency Distribution (Negative)")
plt.show()
