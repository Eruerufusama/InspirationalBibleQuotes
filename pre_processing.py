import sys
from random import randint, choice
from urllib.request import urlretrieve
from time import sleep
import json
import logger


def select_quote():
  with open(sys.path[0] + '/resources/bible_list.txt') as bible:
    bible = bible.read()
    bible_list = bible.split('\n')
    if bible_list[-1] == '':
      del bible_list[-1]
    index = randint(0, len(bible_list) - 1)
    return bible_list[index], index


def get_img(settings):
  # Assign settings from settings.json
  width = settings["canvas"]["size"]["width"]
  height = settings["canvas"]["size"]["height"]
  filetype = settings["image-data"]["filetype"].replace(".", "")

  supported_files = ["jpg", "png", "jfif", "pjpeg", "pjp", "gif"]
  min_size, max_size = 540, 1920

  # Pre-checks
  if filetype not in supported_files:
    msg = f'Error: filetype {filetype} is not a supported filetype.'
    logger.log('Error', None, None, None, msg)
    exit()

  if not (min_size < (width or height) < max_size):
    msg = f'Error: file resolution exceeds max/min limitations.'
    logger.log('Error', None, None, None, msg)
    exit()

  # Actual processing
  try:
    pic_num = randint(2, 1084)
    url = f'https://picsum.photos/{width}/{height}/'
    urlretrieve(url, sys.path[0] + f'/resources/photo_of_the_day{filetype}')
    return pic_num
  except OSError:
    get_img(settings)


def json_to_dict(json_file):
  with open(json_file, encoding="utf-8") as json_file:
    json_object = json.load(json_file)
    return dict(json_object)


def write_to_json(json_file, dct):
  with open(json_file, 'w') as json_file:
    json.dump(dct, json_file)
