from random import randint, choice
from urllib.request import urlretrieve
from time import sleep


def select_quote():
    with open('../resources/bible_list.txt') as bible:
        bible = bible.read()
        bible_list = bible.split('\n')
        index = randint(0, len(bible_list) - 1)
        return bible_list[index], index


def get_img():
    try:
        pic_num = randint(2, 1084)
        url = 'https://picsum.photos/1080/1080/'
        urlretrieve(url, '../resources/photo_of_the_day.jpg')
        sleep(2)
    except OSError:
        get_img()
