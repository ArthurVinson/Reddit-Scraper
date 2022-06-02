# -*- coding: utf-8 -*-
"""
Data Cleaning for NLP

https://towardsdatascience.com/nlp-in-python-data-cleaning-6313a404a470

Created on Fri May 27 11:05:51 2022

@author: Arthur Vinson
"""

import os
import pandas as pd

path = '.\my-dataset'


# loop through csv in directory

for root, dirs, files in os.walk(path):
    for i in files:

        basename, ext = os.path.splitext(i)
        
        # create file: csvfilename_cleaned
        # basename + '_cleaned' + '.csv' 
        
        df = pd.read_csv(i)
        
        print(df.head(1))
        
        
        
        # load in submissions csv into a data frame



# loop through rows

# take a look at the selftext column, if Null, (deleted) or (removed), delete 
# the row

# clear out the punct

# clear out stopwords


# take the selftext - 
