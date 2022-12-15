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


year = 2021
subreddit = 'Pathfinder_RPG'
text = ""

base = './my-dataset/textfiles'

full_path = base + '/' + subreddit + '-' + str(year) + '.csv'

print(full_path)



# load in the dataframe

df = pd.read_csv(full_path)[['0']]

df.rename(columns={"0":"selftext"}, inplace=True)

# dataframe to one large string variable
text = " ".join(cat.split()[0] for cat in df.selftext)

stopwords = set(STOPWORDS)

stopwords.add('deleted')
stopwords.add('removed')

wordcloud = WordCloud(stopwords=stopwords).generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

cloud_filename = './my-dataset/datafiles' + '/' + subreddit + '-' + str(year) + '-wordcloud.png' 

wordcloud.to_file(cloud_filename)

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