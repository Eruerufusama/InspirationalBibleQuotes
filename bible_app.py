# pics: https://picsum.photos/ - https://picsum.photos/200/300
# bible: https://api.imgflip.com/get_memes


'''

tokens.py

- Søk picsum for bilde
- Søk bible quotes
- Use pillow to put quote over image
- Make twitter/discord bot to post pic
- ???
- Profit
'''

# get_biblequote()
# get_image()
# generate_meme()
# post_twitter

import random
import requests


def select_quote():
    with open('bible_verses.txt') as bible:
        b = bible.read().split('\n\n')
        verse = random.choice(b)
        verse = verse[verse.find(' ') + 1:]
        print(verse)


select_quote()
