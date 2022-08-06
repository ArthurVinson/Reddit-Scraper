# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 23:30:20 2022

data_retrieve.py

Retrieve text from the dataset 

@author: Arthur Vinson 


"""
# Construct the path to the dataset folder

year = 2020
subreddit = 'Pathfinder2e'
text = ""

base = './my-dataset/'
dirpath = base + str(year)

subredditdirpath = dirpath + '/' + subreddit

submissions_csv_path = str(year) + '-' + subreddit + '-submissions.csv'

full_path = subredditdirpath + '/' + submissions_csv_path

print(full_path)


# retrieve the text in the dataset and compile it into a single string


# load the text here