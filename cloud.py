# -*- coding: utf-8 -*-
"""
Wordcloud

Created on Tue Aug  2 20:05:52 2022

@author: Arthur Vinson

Taking the datasets /my-dataset construct a WordCloud from the submission
titles, the self-text and comments 

Basic ideas from 
https://www.analyticsvidhya.com/blog/2021/05/how-to-build-word-cloud-in-python/

"""

import pandas as pd
import numpy as np
from os import path
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

year = 2020
subreddit = 'Pathfinder2e'
text = ""

base = './my-dataset/'
dirpath = base + str(year)

subredditdirpath = dirpath + '/' + subreddit

submissions_csv_path = str(year) + '-' + subreddit + '-submissions.csv'

full_path = subredditdirpath + '/' + submissions_csv_path

print(full_path)

stopwords = set(STOPWORDS)

# load in the dataframe

df = pd.read_csv(full_path, index_col=0)

# first 5 rows of the dataset

print(df.head())

text = " ".join(selftext for stuff in df.selftext)

wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# Clean out stop words and [removed] posts

# #Importing Libraries
# import pandas as pd
# import matplotlib.pyplot as plt
# %matplotlib inline
# from wordcloud import WordCloud
# #Importing Dataset
# df = pd.read_csv("android-games.csv")
# #Checking the Data
# df.head()
# #Checking for NaN values
# df.isna().sum()
# #Removing NaN Values
# #df.dropna(inplace = True)
# #Creating the text variable
# text = " ".join(cat.split()[1] for cat in df.category)
# # Creating word_cloud with text as argument in .generate() method
# word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
# # Display the generated Word Cloud
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()

# #Importing Libraries

# import pandas as pd

# import matplotlib.pyplot as plt

# %matplotlib inline

# from wordcloud import WordCloud

# #Importing Dataset

# df = pd.read_csv("1.csv")

# #Checking the Data

# df.head()

# #Creating the text variable

# text2 = " ".join(title for title in df.title)

# # Creating word_cloud with text as argument in .generate() method

# word_cloud2 = WordCloud(collocations = False, background_color = 'white').generate(text2)

# # Display the generated Word Cloud

# plt.imshow(word_cloud2, interpolation='bilinear')

# plt.axis("off")

# plt.show()