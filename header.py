from functions import open_json

import numpy.random as numpy
from random import randint
import sys

class Header:
    '''

    Creates an empty header-object for the twitter-object to use.

    To create the header, run the 'create'-method associated with this object.

    '''

    def __init__(self):
        self.load_settings()
        self.evaluate_settings()


    def create(self):
      # DOCUMENTATION
        '''

        Creates a randomly generated header-string to post.

        '''

      # LOGIC
        self.select_header()
        self.emojify_header()
        self.merge()

    def merge(self):
      # DOCUMENTATION
        '''

        Merges the header with any potential hashtags.

        '''

      # LOGIC
        self.header = self.header_with_emojis + self.hashtag


    def select_header(self):
      # DOUMENTATIOn
        '''

        Randomly selects a header from a source-file.

        '''

      # LOGIC
        with open(self.header_source) as header:
            headers = header.read().split("\n\n")
            i = randint(0, len(headers) - 1)

            self.plain_header = headers[i]


    def emojify_header(self):
      # DOCUMENTATION
        '''

        Takes the header, fills it with emojis, and stores it in the object's 'header_with_emojis'.

        '''

      # LOGIC
        # Splits the words in the twitter-header.
        words = self.plain_header.split()

        # Places emojis inn between words, and appends emojis before and after.
        remaining_chars = self.max_chars - len(''.join(words)) - (self.meme_amp * 2) - len(self.hashtag)
        avg = remaining_chars / (len(words))

        self.emojis = list(self.emojis_dict.keys())
        self.probabilities = list(self.emojis_dict.values())

        emoji_prefix = self.create_prefix_or_suffix()
        emoji_suffix = self.create_prefix_or_suffix()

        if avg < 1:
            self.header_with_emojis = emoji_prefix + self.plain_header + emoji_suffix
        else:
            emojified_message = self.smash_emojis_between_words(words, avg)
            self.header_with_emojis = emoji_prefix + emojified_message + emoji_suffix


    def smash_emojis_between_words(self, words, avg):
      # DOCUMENTATION
        '''

        Selects random emojis based on weightings and smashes them between words.

        '''

      # LOGIC
        emojified_message = ''

        for i, word in enumerate(words, 1):
            emojified_message += word

            if i == len(words):
                break

            for i in range(randint(1, int(avg) if avg < 5 else 5)):
                emojified_message += ''.join(numpy.choice(self.emojis, size=1, p=self.probabilities))

        return emojified_message

    def create_prefix_or_suffix(self):
      # DOCUMENTATIOn
        '''

        returns an amount of random emojis based on weightnings.

        '''

      # LOGIC
        return ''.join(numpy.choice(self.emojis, size=self.meme_amp, p=self.probabilities))

    def evaluate_settings(self):
      # DOCUMENTATION
        '''

        Makes sure the settings are valid.

        '''

      # LOGIC
        pass

    def load_settings(self, filepath=None):
      # DOCUMENTATION
        '''

        Loads the settings into object-properties.

        '''

      # EVALUATE ARGS
        if filepath == None:
            filepath = "/resources/settings.json"

      # LOGIC
        settings = open_json(filepath)

        self.hashtag = ""
        self.header = ""
        self.emojis_dict = open_json(settings["tweet"]["emojis"]["source"])
        self.meme_amp = settings["tweet"]["emojis"]["amplitude"]
        self.header_source = sys.path[0] + settings["tweet"]["text"]["source"]
        self.max_chars = settings["tweet"]["text"]["max chars"]