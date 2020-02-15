"""
pre-processing of tweets
"""
import re
import emoji
from nltk.tokenize import TweetTokenizer

class Twitter:
    """
    change a string of raw text into an array of int
    """
    def __init__(self, string, max_length_dictionary=None, max_length_tweet=None):
        self.string = string
        self.max_length_dictionary = max_length_dictionary
        self.max_length_tweet = max_length_tweet
        self.final_text = None
        self.tokens = None
        self.indexes = None

    def clean_text(self):
        """
        remove urls and unnecessary tokens
        """
        #remove link
        pattern1 = re.compile(r'https://[A-Za-z0-9.,\/\'-:_\"@!&#…\n]+')
        text_without_link = pattern1.sub('', self.string)  
        #remove emoji
        text_without_link_and_emoji = emoji.get_emoji_regexp().sub(u'', text_without_link)
        text_without_link_and_emoji = text_without_link_and_emoji.replace('\n', ' ')
        #remove hashtag
        pattern2 = re.compile(r'RT @[\w_]+: ')
        cleaned_text = pattern2.sub('', text_without_link_and_emoji)
        #remove punctuation marks
        pattern3 = re.compile(r'[^A-Za-z0-9\']')
        self.final_text = pattern3.sub(' ', cleaned_text)
        return self.final_text

    def tokenize_text(self):
        """
        change text into tokens
        """
        tknzr = TweetTokenizer()
        self.tokens = tknzr.tokenize(self.final_text)
        return self.tokens


    def replace_token_with_index(self):
        """
        replace token with index
        """
        # load embedding dictionary
        emb_dict = {}
        glove = open('glove.twitter.27B.25d.txt')
        i = 1
        for line in glove:
            values = line.split()
            word = values[0]
            if word.isalpha(): # only load english words
                emb_dict[word] = i
                i += 1
            if self.max_length_dictionary and i > self.max_length_dictionary:
                break
        glove.close()
        indexes = []
        for token in self.tokens:
            token = token.lower()
            if emb_dict.get(token):
                index = emb_dict[token]
                indexes.append(index)
        self.indexes = indexes
        return self.indexes

    def pad_sequence(self):
        """
        pad indexes with 0 until max length
        """
        if self.max_length_tweet:
            while len(self.indexes) < self.max_length_tweet:
                self.indexes.append(0)
            if len(self.indexes) > self.max_length_tweet:
                self.indexes = self.indexes[:15]
        return self.indexes
