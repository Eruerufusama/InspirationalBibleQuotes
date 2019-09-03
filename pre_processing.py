from random import randint, choice
from urllib.request import urlretrieve
from time import sleep
from re import split


def select_quote():
    with open('bible_verses.txt') as bible:
        bible = bible.read()
        bible_list = split('\d\d?\:\d\d?', bible)
        verse = choice(bible_list)
# ----- Remove verse number from line ----- #
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
