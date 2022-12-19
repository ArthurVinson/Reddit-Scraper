# -*- coding: utf-8 -*-
"""
Sentiment Analyzer

Created on Sun Aug 28 22:51:42 2022

@author: Arthur Vinson

Inspired by https://levelup.gitconnected.com/simple-nlp-in-python-2cb3243239d3



"""

from textblob import TextBlob

# Input Text

input_text = '''I am a life long Star Wars fan and this was the first time I came out disappointed. And I am not picky, I was mostly happy even with the last two movies, but this one is the worst Star Wars movie yet.'''

# Creating a textblob object an assigning the sentiment property

analysis = TextBlob(input_text).sentiment
print(analysis)


# retrieve from textfiles



# then work magic


