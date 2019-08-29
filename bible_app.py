# pics: https://picsum.photos/ - https://picsum.photos/200/300
# bible: https://api.imgflip.com/get_memes


'''
https://picsum.photos/id/1084/800/1200

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
import urllib
from PIL import Image, ImageFont, ImageDraw


def select_quote():
    with open('bible_verses.txt') as bible:
        bible_list = bible.read().split('\n\n')
        # ----- Limit length of quote -----#
        while True:
            verse = random.choice(bible_list)
            if len(verse) > 110:
                verse = random.choice(bible_list)
            else:
                break
        verse = verse[verse.find(' ') + 1:].rstrip()
        return verse


def get_img():
    pic_num = random.randint(2, 1084)
    url = 'https://picsum.photos/800/1200'
    #r = requests.get(url)
    # print(r.text)
    urllib.request.urlretrieve(url, './photo_of_the_day.jpeg')


def put_quote_on_wallpaper():
    # ----- Open image -----#
    get_img()
    image = Image.open("photo_of_the_day.jpeg")
# ----- Create string -----#
    string = select_quote()
# ----- Select Font-type, Font-size ----- #
    font = ImageFont.truetype("/Library/Fonts/arial.ttf", 24)
# ----- Draw text onto wallpaper ----- #
    draw = ImageDraw.Draw(image)
    draw.text((100, 100), string, "black", font)

    # Debug
    image.show()


if __name__ == '__main__':
    put_quote_on_wallpaper()
