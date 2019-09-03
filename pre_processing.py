from random import randint, choice
from urllib.request import urlretrieve
from time import sleep


def select_quote():
  with open('bible_verses.txt') as bible:
      bible_list = bible.read().split('\n\n')
    # Limit length of quote -----#
      while True:
          verse = choice(bible_list)
          if len(verse) > 110:
              verse = choice(bible_list)
          else:
              break
    # Remove verse number from line ----- #
      verse = verse[verse.find(' ') + 1:].rstrip()
      return verse


def get_img():
  try:
    pic_num = randint(2, 1084)
    print(pic_num)
    url = 'https://picsum.photos/1080/1080/'
    urlretrieve(url, './photo_of_the_day.jpg')
    sleep(2)
  except OSError:
    get_img()