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

import seaborn as sns
import matplotlib.pyplot as plt

from wordcloud import WordCloud

import plotly.express as px
import plotly.io as io

io.renderers.default = 'svg'
# variable declaration

basedir = './my-dataset/imagefiles/'
# subreddit = ['CallofCthulhu','MouseGuard','Pathfinder_RPG','Pathfinder2e','shadowrun']
# year = ['2019', '2020', '2021']

subreddit = 'MouseGuard'
year = '2021'

"""
for subr in subreddit:
    for yr in year:
        filename = basedir + subr + '-' + yr + '.csv'
        print(filename)
"""

filename = './my-dataset/textfiles/' + subreddit + '-' + year + '.csv'

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

# label counts for each word

print(dataf.label.value_counts())

# representation of word sentiment

fig, ax = plt.subplots(figsize=(8,8))
counts = dataf.label.value_counts(normalize=True) * 100

sns.barplot(x=counts.index, y=counts, ax=ax)

ax.set_xticklabels(['Negative','Neutral', 'Positive'])
ax.set_ylabel("Percentage")

chart_name = basedir + subreddit + '-' + year + '-chart.png'
plt.savefig(chart_name) #save to file

plt.show()

df_pos_neg = dataf.loc[dataf['label'] != 0]

print(df_pos_neg.label.value_counts())

fig, ax = plt.subplots(figsize=(8,8))

counts = df_pos_neg.label.value_counts(normalize=True) * 100

sns.barplot(x=counts.index, y=counts, ax=ax)

ax.set_xticklabels(['Negative','Positive'])
ax.set_ylabel("Percentage")

pos_neg_chart_name = basedir + subreddit + '-' + year + '-percentchart.png'
plt.savefig(pos_neg_chart_name)

plt.show()

###

positive_words = list(dataf.loc[dataf['label'] == 1].words)


pos_frequency = FreqDist(positive_words)
pos_freq = pos_frequency.most_common(20)

print(pos_freq)

negative_words = list(dataf.loc[dataf['label'] == -1].words)

neg_frequency = FreqDist(negative_words)
neg_freq = neg_frequency.most_common(20)

print(neg_freq)

# Wordcloud redux

Pos_words = pd.DataFrame(positive_words, columns = ['text'])  # 1 column dataframe of positive words
Pos_words_string = " ".join(cat.split()[0] for cat in Pos_words.text) # covert to string

Neg_words = pd.DataFrame(negative_words, columns = ['text']) # 1 column dataframe of negative words
Neg_words_string = " ".join(cat.split()[0] for cat in Neg_words.text) # covert to string

# create and generate a word cloud image
wordcloud_positive = WordCloud(background_color='white').generate(Pos_words_string)
wordcloud_negative = WordCloud().generate(Neg_words_string)

# Display postive wordcloud
plt.imshow(wordcloud_positive, interpolation='bilinear')
plt.axis("off")
plt.show()

# Display negative wordcloud
plt.imshow(wordcloud_negative, interpolation='bilinear')
plt.axis("off")
plt.show()

# save wordclouds to file

pos_cloud_name = basedir + subreddit + '-' + year + '-cloud-positive.png'
neg_cloud_name = basedir + subreddit + '-' + year + '-cloud-negative.png'

wordcloud_positive.to_file(pos_cloud_name)
wordcloud_negative.to_file(neg_cloud_name)

# Bar Chart of Most Common Positive Words by Count

pos_freq_df = pd.DataFrame(pos_freq)
pos_freq_df = pos_freq_df.rename(columns = {0: 'Bar Graph of Frequent Words', 1: 'Count'}, inplace = False)

fig = px.bar(pos_freq_df, x= 'Bar Graph of Frequent Words', y = 'Count', title = 'Commonly Used Positive Words by Count')
fig.show()

pos_freq_filename = basedir + subreddit + '-' + year + '-positive-frequency.png'
fig.write_image(pos_freq_filename)

neg_freq_df = pd.DataFrame(neg_freq)
neg_freq_df = neg_freq_df.rename(columns = {0: 'Bar Graph of Frequent Words', 1: 'Count'}, inplace = False)

fig = px.bar(neg_freq_df, x= 'Bar Graph of Frequent Words', y = 'Count', title = 'Commonly Used Negative Words by Count')

fig.show()

neg_freq_filename = basedir + subreddit + '-' + year + '-negative-frequency.png'
fig.write_image(neg_freq_filename)