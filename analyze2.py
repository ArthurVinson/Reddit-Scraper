# -*- coding: utf-8 -*-
"""

Analyze 2

Created on Wed Dec 14 14:51:35 2022

@author: Arthur Vinson

Take the text-data files and make graphs with information

inspired by https://levelup.gitconnected.com/reddit-sentiment-analysis-with-python-c13062b862f6

"""

# imports

import pandas as pd
import emoji
import re

import en_core_web_sm
import spacy

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from nltk import FreqDist


# variable declaration

basedir = './my-dataset/textfiles/'
# subreddit = ['CallofCthulhu','MouseGuard','Pathfinder_RPG','Pathfinder2e','shadowrun']
# year = ['2019', '2020', '2021']

subreddit = 'CallofCthulhu'
year = '2019'

"""
for subr in subreddit:
    for yr in year:
        filename = basedir + subr + '-' + yr + '.csv'
        print(filename)
"""

filename = basedir + subreddit + '-' + year + '.csv'

df = pd.read_csv(filename, usecols=['0'])

df.rename(columns={'0':'text'}, inplace=True)

textlist = df.text.values.tolist()

clean = textlist

clean = [str(i) for i in clean]

clean = ' , '.join(clean)

# remove emoji
clean = emoji.demojize(clean)

# remove urls
clean = re.sub(r'http?\S+', '', clean)

# tokenize and clean
tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|http\S+')
clean = tokenizer.tokenize(clean)

# lower case

clean = [word.lower() for word in clean]

# remove stopwords

nlp = en_core_web_sm.load()

all_stopwords = nlp.Defaults.stop_words

clean = [word for word in clean if not word in all_stopwords]

# lemmatizing

lemmatizer = WordNetLemmatizer()

clean2 = ([lemmatizer.lemmatize(w) for w in clean])

## Sentiment Analysis

sia = SIA()
results = []

for sentences in clean:
    pol_score = sia.polarity_scores(sentences)
    pol_score['words'] = sentences
    results.append(pol_score)

pd.set_option('display.max_columns', None, 'max_colwidth', None)
dataf = pd.DataFrame.from_records(results)

dataf['label'] = 0

dataf.loc[dataf['compound'] > 0.10, 'label'] = 1
dataf.loc[dataf['compound'] < -0.10, 'label'] = -1
print(dataf.head())