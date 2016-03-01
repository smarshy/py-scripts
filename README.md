# Miscellaneous Python Scripts

A collection of some scripts I just happened to write for fun. Usage details are present in the scripts. Many of these interact with an API:

### movie_search.py

You can search for any movie/TV show using keywords and an optional page number. Uses the [Open Movie Database API](http://omdbapi.com)

### rhyming_word.py

Give it a word and it shall find all the rhyming words for you. Uses the [Wordnik API](https://wordnik.com/)

### review_sentiment

Contains nykaa_review.py - a script which analyses sentiments based on recently published reviews for a particular product page on [nykaa](http://nykaa.com)
I have put together a list of positive and negative words by surveying the website reviews as well as by referring to general such available lists

### quora_analysis.py 

Uses python package for quora to fetch user stats and perform a simple activity analysis

### zip.py

Uses [zippopotam API](http://www.zippopotam.us/) location details based on zipcode and country code

## Github scripts

The following directly interact with [github API](https://developer.github.com/v3/) to fetch data.

### py_git.py

Presents an analysis of pull requests and issues for entered username

### list_contributions.py

Presents a list of links to contributed PRs and Issues for entered username

### list_contributions_repo.py

Presents a filtered list of links to contributed PRs and Issues for a user as per entered repository details

### git_language.py

Presents an analysis of languages vs repository count for entered username

### repo_stats.py

Get your commit frequency on different days of the week over a period of one month