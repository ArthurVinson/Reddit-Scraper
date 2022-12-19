# -*- coding: utf-8 -*-
"""
Data Cleaning for NLP

https://towardsdatascience.com/nlp-in-python-data-cleaning-6313a404a470

Created on Fri May 27 11:05:51 2022

@author: Arthur Vinson
"""

import os

directory = '.\my-dataset'
cleaned_directory = '.\my-dataset-cleaned'

# if it doesn't exist already, create 'my-dataset-cleaned' directory

# loop through csv in directory


# Functions 

# Create Folder Structure - making a folder structure for the cleaned datasets
#  that mimic the structure for the main datasets
def create_folder_structure(src, dst):
    # first we get the absolute path of the source folder
    src = os.path.abspath(src)
    
    # making a variable having the index till whichsrc string has folder and
    # a path separator
    src_prefix = len(src) + len(os.path.sep)
    
    # making the destination folder
    os.makedirs(dst)
    
    # doing os walk in the source folder
    for root, dirs, files in os.walk(src):
        for dirname in dirs:
            # dst has destination folder, root[src_prefix:] give us relative
            # path from source folder and dirname has folder names
            dirpath = os.path.join(dst, root[src_prefix:], dirname)
            
            # making the path which we made by joining all of the above
            os.mkdir(dirpath)
            
create_folder_structure(directory, cleaned_directory)



path ='.\my-dataset'

# print("Folder Structure")
# for root, dirs, files in os.walk(path):
#     for i in files:
        
# create file: csvfilename_cleaned

# load in submissions csv into a data frame

# loop through rows

# take a look at the selftext column, if Null, (deleted) or (removed), delete 
# the row

# clear out the punct

# clear out stopwords


# take the selftext - 
