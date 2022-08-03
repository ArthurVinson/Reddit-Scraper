# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 00:16:03 2022

@author: Arthur Vinson

Attribute Find - Used to determine the available attribute of a PRAW Object

"""

import praw
import pprint

reddit = praw.Reddit(
    client_id='LK_PUjO05BqFSg', 
    client_secret='FuE_G7UhRkvIsVNurMuo0VMO3J85ug', 
    user_agent='scraper project',
    check_for_async=False)


# assume you have a praw.Reddit instance bound to variable `reddit`

# =============================================================================
# test = [
#         'e977b', # u/judewriley
#         '2riuy', # r/reformed
#         '', # submission
#         '' # comment 
#         ]
# 
# =============================================================================
for entry in test:
    
    submission = reddit.submission(entry)
    print(submission.title)  # to make it non-lazy
    pprint.pprint(vars(submission))

