# All-Aboard-the-Karachi-Load-Shedding-Blame-Train

Using data from Twitter to determine if we can tell if Karachi Electric will be blamed for load shedding in Karachi, Pakistan based on other tweets also blaming other entities. This is a follow-on project to the project found in https://github.com/deshanahan/Karachi-Load-Shedding-Blame-Train.

# Overview

This program seeks to use tweets about load shedding in Karachi, Pakistan to determine what entity is receiving the most blame for the persistent electricity issues the citizens of Karachi have been facing. After determining this, the program will train logistic regression, decision tree, and random forest models and use model selection techniques to determine if we can predict blames against Karachi Electric, the entity that is most blamed for load shedding in Karachi, Pakistan based on the same tweeters blaming other entities. This is a project for my Introduction to Data Science class at the University of Maryland Baltimore County, where I have been tasked to use webscraping or an API to gather data, conduct an exploratory data analysis, train regression models, use model selection techniques to find the best performing model, and develop an informed conclusion about a topic of my choice with the help of data. I have used the python-twitter API, which is a python wrapper for the Twitter API. Please see the [python-twitter API documentation](https://python-twitter.readthedocs.io/en/latest/index.html) if you wish to know more about how the searches work.

# Goals

The goals for this project include training a model that performs better than the dummy model of True to False ratio of the entity with the most blames or finding the best model out of the models that were trained. My learning goals in this project include exploring python libraries like pandas, including visualization tools, learning how to apply an API to collect data, learning how to train regression models and how to perform model selection, and gaining experience handling a real-world problem with a python program.

# Motivation & Background

I had the opportunity to attend the Defense Language Institute, where I learned the language and culture of Pakistan for approximately two years. It was here where I first heard about the problem of load shedding in Pakistan.

The ability to go about our daily lives without needing to worry about access to gas or electricity is, perhaps, the most ubiquitous concept in our society. What would you do if your access to power was consistently in question? What if your access to power was cut off for more than 12 hours at a time? Load shedding has become the way-of-life in Karachi, Pakistan, a city of over [16 million people](https://worldpopulationreview.com/world-cities/karachi-population).

[In-fighting](https://www.geo.tv/latest/309461-karachi-load-shedding-goes-beyond-12-hours-as-k-electric-ssgc-spar-over-gas-supply) between gas and electricity providers has yielded two candidates, Karachi Electric and SSGC, who are being blamed for the energy crisis in Karachi, even as supply shortages expected this winter in Karachi will only worsen the conditions.

Using social media to determine who is being blamed for load shedding in Karachi, Pakistan has been done on a small scale [in the past](https://www.linkedin.com/pulse/curious-case-k-electric-jamat-e-islami-karachites-aamir-abbasi-cipr-/)

This program could offer politicians and public relations teams in Pakistan a systematic way to evaluate where they stand in the Karachi load shedding blame game.
Table of Contents

Code: There are two data files which you must be aware of:

Karachi_LS_Tweeters

karachi_ls.csv

Both of which can be found in the [repository's project folder](https://github.com/deshanahan/All-Aboard-the-Karachi-Load-Shedding-Blame-Train/tree/main/Project)

Report: A detailed technical notebook containing an overview of the code may be found on the [repository's home page](https://github.com/deshanahan/Karachi-Load-Shedding-Blame-Train).

# Software Requirements

This program uses:

python version 3.8.3

ipython version 7.16.1

jupyter version 1.0.0

jupyter_client version 6.1.6

jupyter_console version 6.1.0

jupyter core version 4.6.3

Twitter API keys from an imported module contained in a .gitignore file

datetime python built-in module

twitter (Twitter API Python wrapper) version 1.18.0

pandas version 1.0.5

numpy version 1.18.5

scikit learn version 0.23.1

# Data

The dataset is designed to be continuously used and will change based on the number of tweets about Karachi load shedding in the past week. The captured dataset in the csv files provided on the repository home page are:

Karachi_LS_Tweeters - rows = 8 (blamed entities) columns = 47 (tweeters)

karachi_ls.csv - rows = 8 (blamed entities) columns = 59 (tweeters)

After combining the csv files with the new search and removing duplicate tweeters, the search used in the project contains 8 rows of blamed entities and 74 tweeters.

Limitations:

The Twitter API requires authentication through a series of API keys.

The Twitter API allows for: a maximum of 100 tweets pulled per search pulling historical tweets of up to one week

All searches in the program utilize the maximum amount of pulls and history that Twitter allows.
