import sys
import os
from random import randint
from time import time, sleep
from bot import bot
from pre_processing import select_quote, get_img, json_to_dict
from image_processing import put_quote_on_wallpaper
from tweet_processing import create_header
import logger

if __name__ == '__main__':
  # Starts timer
  start = time()

  # Load settings
  settings = json_to_dict("/resources/settings.json")

  # Selects a verse from the bible
  verse, verse_index = select_quote()

  # Retrieves an image.
  pic_num = get_img(settings)

  # Processes bible-verse onto image.
  put_quote_on_wallpaper(sys.path[0] + '/resources/photo_of_the_day.jpg', verse, settings)

  # Creates tweet-header
  tweet, header_index = create_header(settings)

  # Uploads image and tweet-header to twitter
  success = bot(tweet)

  # Stops timer
  end = time()
  time_spent = float("{0:.3f}".format(end - start))

  # Writes debug-info to log-file
  logger.log(success, verse_index, header_index, pic_num, time_spent, None)
  os.remove(sys.path[0] + '/resources/photo_of_the_day.jpg')
