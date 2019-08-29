import random
import requests
import urllib
from PIL import Image, ImageFont, ImageDraw
import bot


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
    urllib.request.urlretrieve(url, './photo_of_the_day.png')


def put_quote_on_wallpaper(wallpaper, biblequote):
    # ----- Open image -----#
    image = Image.open(wallpaper)
# ----- Select Font-type, Font-size ----- #
    font = ImageFont.truetype("/Library/Fonts/arial.ttf", 24)
# ----- Draw text onto wallpaper ----- #
    draw = ImageDraw.Draw(image)
    draw.text((100, 100), biblequote, "black", font)
    print(123)
    image.save('./photo_of_the_day.png')


def main():
    verse = select_quote()
    get_img()  # Download img
    put_quote_on_wallpaper('./photo_of_the_day.png', verse)
    # ---- Upload img to twitter ---- #
    bot.main()


if __name__ == '__main__':
    main()
