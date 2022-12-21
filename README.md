
# Reddit Scraper and Sentiment Analysis

Sentiment Analysis project for self-learning and for fun. Reddit data is scraped, run through Textblob and Vader analysis and then visualized.




## Methodology

### First steps
Before creating the dataset, you will need a Reddit account in order to use the Praw library needed to scrape information from the subreddit of choice. In addition, you'll need the proper authentication tokens outlined [here](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps).

You will also need to make a `my-dataset` folder in your working directory, creating the folders `datafiles`, `imagefiles` and `textfiles` within it.

### Create Dataset
With those steps out of the way, run the following Python scripts in order to create the dataset.

- `datacompile.py` - scrapes indicated subreddit for indicated year (adjustable directly in script)

- `data_retrieve.py` - compiles raw data for indicated subreddit and year (adjusted directly in script) into csv for analysis

### Analyze dataset
After the dataset has been compiled, run the scripts to analyze the data and turn it into a visualizations.

- `analyze.py` - generates a scatterplot from Textblob analysis, saves it to imagedata (subreddit and year adjusted in script directly)
 
- `analyze2.py` - generates wordclouds and bar charts from Vader sentiment analysis

- `cloud.py` - generates a wordcloud from total scraping

The included Jupyter notebook `Reddit Scraping Project` combines the functionality of analyze.py, analyze2.py and cloud.py and can be run on its own in lieu of them.

### Limitations
- Partially completed subreddits in a folder will cause `datacompile.py` to skip over them entirely (it won't fill them up)

- Need to specify the year and subreddit for each script.
## Future Plans

- Create directory structure from code

- Refactor code with better use of functions, loops and vectorization

- Better use of object-oriented programming principles

- Add ability to specify a time range 

- Better show what's going on when the code is running, allow pausing and restarting

- More informative, possibly interactive visualizations

## Screenshots
[(https://github.com/ArthurVinson/Reddit-Scraper/blob/main/my-dataset/imagefiles/Pathfinder2e-2019.png)]



## 🚀 About Me
I'm aspiring to enter into the data science, data engineering and machine learning fields. 

After some needed encouragement and some gentle nudging by thoughtful friends, I returned to college in 2017, completing a degree in physics a few years later. During that time, a good professor introduced me to the realm of machine learning and data science. Wanting to take advantage of this new cultural change, I resolved to learn what I could about these growing fields for myself. It’s been slow going with plenty of hiccups and detours in the way, but I’m still working hard on bettering myself, increasing my skillsets, and making my way to be the most robust data scientist I can be. 

