import random
import requests
import urllib
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from textwrap import wrap
import bot

def select_header():
    with open('tweet_headers.txt') as header:
        headers = header.read().split("\n")
        return random.choice(headers)

def fill_header_with_emojis(header):
    returnstring = ""
    memeload = 4

    with open("emojis.txt", encoding="utf-8") as emoji_file:
        emojis = emoji_file.read().split()

        for i in range(memeload):
            returnstring += random.choice(emojis)
        splitted_header = header.split()
        for word in splitted_header:
            returnstring += word
            for i in range(memeload):
                returnstring += random.choice(emojis)
    return returnstring

def create_header():
    header = select_header()
    return fill_header_with_emojis(header)

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
    url = 'https://picsum.photos/1080/1920'
    urllib.request.urlretrieve(url, './photo_of_the_day.png')

def put_quote_on_wallpaper(wallpaper, biblequote):
    lines = wrap(biblequote, 40) # Split verse into multiple lines if needed
    font = ImageFont.truetype("/Library/Fonts/arial.ttf", 48) # Define font-parameters

# Open layers
    image = Image.open(wallpaper) # Background
    text_layer = Image.new('RGBA', (image.size[0], image.size[1]), None) # Text-layer

# Create draw-object
    draw = ImageDraw.Draw(text_layer)

# Draw text onto text-layer
    x = 100
    y = 100
    offset = 2

    # Draws shadow
    for line in lines:
        width, height = font.getsize(line)
        draw.text((x + offset, y + offset), line, "black", font)
        y += height
    y = 100

    # Draws overlaid text
    for line in lines:
        width, height = font.getsize(line)
        draw.text((x, y), line, "white", font)

        y += height
    
# Merges layers
    image.paste(text_layer, (0, 0), text_layer)

    image.show() # Debug
    image.save('./photo_of_the_day.png')


def main():
    verse = select_quote()
    # ----- Download imgage ----- #
    get_img()
    put_quote_on_wallpaper('./photo_of_the_day.png', verse)

    tweet = create_header()
    # ----- Upload img to twitter ----- #
    bot.main(tweet)


if __name__ == '__main__':
    main()
