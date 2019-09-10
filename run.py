from random import randint
from time import time, sleep
from bot import bot
from pre_processing import select_quote, get_img, json_to_dict
from image_processing import put_quote_on_wallpaper
from tweet_processing import create_header
import logger
# import requests # pip install requests

if __name__ == '__main__':
    settings = json_to_dict("./resources/settings.json")
    start = time()
    verse, verse_index = select_quote()
    get_img(settings)
    put_quote_on_wallpaper('./resources/photo_of_the_day.jpg', verse, settings)
    tweet, header_index = create_header()
    # ----- Upload img to twitter ----- #
    bot(tweet)
    logger.log(verse_index, header_index)
    end = time()
    total = end - start
    print(f'Time spent: {total}')
