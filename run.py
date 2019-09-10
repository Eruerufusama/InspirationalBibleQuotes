import sys
from random import randint
from time import time, sleep
from bot import bot
from pre_processing import select_quote, get_img, json_to_dict
from image_processing import put_quote_on_wallpaper
from tweet_processing import create_header
import logger
# import requests # pip install requests

if __name__ == '__main__':
    # Starts timer
    start = time()

    # Load settings
    settings = json_to_dict("./resources/settings.json")

    # Selects a verse from the bible
    verse, verse_index = select_quote()

    # Retrieves an image.
    get_img(settings)

    # Processes bible-verse onto image.
    put_quote_on_wallpaper('./resources/photo_of_the_day.jpg', verse, settings)

    # Creates tweet-header
    tweet, header_index = create_header()

    # Uploads image and tweet-header to twitter
    bot(tweet)

    # Writes debug-info to log-file
    logger.log(verse_index, header_index)

    # Stops timer
    end = time()
    total = end - start
    print(f'Time spent: {total}')

    # The program sleeps for x amount of seconds
