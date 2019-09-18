import sys
from random import randint, choice
from urllib.request import urlretrieve
from time import sleep
import json
import logger

# Opens a text-file and returns the content of the file in the form of a list.
def file_to_list(filepath):
    with open(sys.path[0] + filepath) as FILE:
        FILE_LIST = FILE.read().split('\n')
        if FILE_LIST[-1] == '':
            del FILE_LIST[-1]
        return FILE_LIST

# Opens the bible and assigns it an index. Returns a list of tuples, where every verse has an associated index.
def select_quote():
    bible_list = file_to_list('/resources/bible_list.txt')
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
        print("Filetype not supported. Open settings.json and choose a supported filetype.")
        print(f"supported filetypes: {supported_files}")
        exit()

    for i in [width, height]:
        if i < min_size or i > max_size:
            print(f"Make sure the image is no larger than {max_size}px, and no smaller than {min_size}px. \n You can do this by respecifying the width and height in settings.json")


    # Actual processing
    try:
        pic_num = randint(2, 1084)
        url = f'https://picsum.photos/{width}/{height}/'
        urlretrieve(url, sys.path[0] + f'/resources/photo_of_the_day.{filetype}')
        sleep(2)
    except OSError:
        get_img(settings)

def json_to_dict(json_file):
    with open(sys.path[0] + json_file, encoding="utf-8") as json_file:
        return dict(json.load(json_file))

def json_to_list(json_file):
    with open(sys.path[0] + json_file, encoding="utf-8") as json_file:
        return list(json.load(json_file))

def write_to_json(json_file, dct):
    with open(sys.path[0] + json_file, 'w') as json_file:
        print(dct)
        json.dump(dct, json_file)
