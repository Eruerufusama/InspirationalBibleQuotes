from time import sleep
from bot import bot
from image_processing import put_quote_on_wallpaper
from tweet_processing import create_header
from pre_processing import select_quote, get_img
# import requests # pip install requests

if __name__ == '__main__':
    while True:
        verse = select_quote()
        get_img()
        put_quote_on_wallpaper('photo_of_the_day.jpg', verse)

        tweet = create_header()
        # ----- Upload img to twitter ----- #
        bot(tweet)
        sleep(3600)
