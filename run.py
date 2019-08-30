import random
import requests
import urllib
from PIL import Image, ImageFont, ImageDraw
from textwrap import wrap
import bot


def select_header():
    with open('tweet_headers.txt') as header:
        headers = header.read().split("\n")
        return random.choice(headers)


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
        # ----- Remove verse number from line ----- #
        verse = verse[verse.find(' ') + 1:].rstrip()
        return verse


def get_img():
    pic_num = random.randint(2, 1084)
    url = 'https://picsum.photos/1440/2560'
    urllib.request.urlretrieve(url, './photo_of_the_day.jpg')


def put_quote_on_wallpaper(wallpaper, biblequote):
    lines = wrap(biblequote, 30)
    image = Image.open(wallpaper)
    font = ImageFont.truetype("/Library/Fonts/arial.ttf", 88)

# ----- Draw text onto wallpaper ----- #
    draw = ImageDraw.Draw(image)
    x_text = 100
    y_text = 100
    for line in lines:
        width, height = font.getsize(line)
        # ----- Outline text on image ----- #
        draw.text((x_text - 1, y_text), line, font=font, fill='black')
        draw.text((x_text + 1, y_text), line, font=font, fill='black')
        draw.text((x_text, y_text - 1), line, font=font, fill='black')
        draw.text((x_text, y_text + 1), line, font=font, fill='black')
        # ----- Main part of text ----- #
        draw.text((x_text, y_text), line, "white", font)
        y_text += height

    image.save('./photo_of_the_day.jpg')


def main():
    verse = select_quote()
    # ----- Download imgage ----- #
    get_img()
    put_quote_on_wallpaper('./photo_of_the_day.jpg', verse)
    tweet = select_quote()
    # ----- Upload img to twitter ----- #
    bot.main(tweet)


if __name__ == '__main__':
    main()
