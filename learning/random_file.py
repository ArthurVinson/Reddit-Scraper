# -*- coding: utf-8 -*-
"""
random_file.py

Random File Picker - for a given directory, select a random file (csv) and
 load it into memory as a dictionary.

Created on Sat Aug  6 23:24:55 2022

@author: Arthur Vinson
"""

import os
import random

# build the file path to the folder

base = './my-dataset/'
year = 2020
subreddit = 'Pathfinder2e'
text = ""

dirpath = base + str(year)

subreddit_dirpath = dirpath + '/' + subreddit


file_list = (os.listdir(subreddit_dirpath))

file = random.choice(file_list)

print(file_list)
print(file)


# year = 2020
# subreddit = 'Pathfinder2e'
# text = ""

# base = './my-dataset/'
# dirpath = base + str(year)

# subredditdirpath = dirpath + '/' + subreddit

# submissions_csv_path = str(year) + '-' + subreddit + '-submissions.csv'

# full_path = subredditdirpath + '/' + submissions_csv_path

# print(full_path)
