# A Pre-processing Python Library

This repo contains **a Python library** to perform preprocessing for a sentiment analysis task with a CNN + embedding model.

**Required Input**: a string of raw text

**Optional Inputs**: maximum length of dictionary, maximum length of a tweet 

**Output**: a list of indices

<br>
<br>

**Four Main Methods:**
1. *clean_text*<br>
   Remove URLs and unnecessary tokens in a tweet
   
2. *tokenize_text*<br>
   Convert a string into an array of tokens using *TweetTonkenizer* from nltk
   
3. *replace_token_with_index*<br>
   Replace each token by its index in the twitter GloVe embedding dictionary

4. *pad_sequence*<br>
   Pad a list of indices with 0 until a maximum length



**Files**
* `twitter.py`: code for library
* `twitter_test.py`: code for unit testing
* `glove.twitter.27B.25d.index`: twitter GloVe embedding dictionary from https://github.com/stanfordnlp/GloVe
* `.travis.yml`: for Travis CI

