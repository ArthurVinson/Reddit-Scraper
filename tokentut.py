# -*- coding: utf-8 -*-
"""
Tokenizing Tutorial

https://www.learndatasci.com/tutorials/sentiment-analysis-reddit-headlines-pythons-nltk/

Created on Tue Feb 16 23:07:23 2021

@author: Arthur Vinson
"""

from nltk.tokenize import word_tokenize, RegexpTokenizer

example = "This is an example sentence! However, it isn't a very informative one"

tokenizer = RegexpTokenizer((r'\w+'))

print(tokenizer.tokenize(example))

print(word_tokenize(example, language='english'))

# simple list of stopwords

from nltk.corpus import stopwords

stop_words = stopwords.words('english')

print(stop_words[:20])

