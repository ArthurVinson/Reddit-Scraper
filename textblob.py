# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 20:58:44 2021

@author: arthu
"""

# Textblob Tutorial here

from textblob import TextBlob


blob = TextBlob("Analytics Vidhya is a great platform to learn data science. \n It helps community through blogs, hackathons, discussions,etc.")

# for np in blob.noun_phrases:
#     print(np)
    
    
# for words, tag in blob.tags:
#     print (words, tag)
    
print (blob.sentences[1].words[1])

print (blob.sentences[1].words[1].singularize())


