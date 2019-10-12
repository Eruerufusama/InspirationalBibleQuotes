from functions import *
from random import randint, choice
from textwrap import wrap
import sys
from urllib.request import urlretrieve
import tweepy
import numpy.random as numpy
from PIL import Image as IMG
from PIL import ImageDraw, ImageFont, ImageFilter

class Tweet:
    def __init__(self):
        self.init()


    def init(self):
        self.load_settings()
        self.evaluate_settings()
        self.create_twitter_object()


    def show_image(self):
        self.image.image.show()


    def show_header(self):
        print(self.header.header)


    def create_header(self):
        self.header = Header()
        self.header.create()
        self.get_hashtag()

    def create_image(self):
        self.image = Image()
        self.image.create()


    def create_twitter_object(self):
        auth = tweepy.OAuthHandler(self.public_api_key, self.private_api_key)
        auth.set_access_token(self.public_token_key, self.private_token_key)

        self.bot = tweepy.API(auth)


    def get_woeids(self):
        woeids = []
        for i, city in enumerate(self.all_cities):
            if i > self.searchspace:
                break
            else:
                for woeid in self.woeids:
                    if woeid["city"] == city:
                        woeids.append(woeid["woeid"])
                        break
        return woeids

    def get_hashtag(self):
        woeids = self.get_woeids()

        for woeid in woeids:
            place = self.bot.trends_place(woeid)

            all_hashtags = [trend["name"] for trend in place[0]["trends"] if trend["name"][0] == "#"]

            hashtags = [hashtag for keyword in self.keywords for hashtag in all_hashtags if keyword in hashtag]

        if len(hashtags) > 0:
            self.header.hashtag = choice(hashtags)


    def post(self):
        image = self.image.image_path
        header = self.header.header

        self.bot.update_with_media(image + header)


    def evaluate_settings(self):
        pass


    def load_settings(self):
        settings = json_to_dict("/resources/settings.json")

        self.public_api_key = settings["auth"]["api public key"]
        self.private_api_key = settings["auth"]["api private key"]
        self.public_token_key = settings["auth"]["token public key"]
        self.private_token_key = settings["auth"]["token private key"]

        self.woeids = json_to_list(settings["tweet"]["hashtags"]["woeids"])
        self.keywords = file_to_list(settings["tweet"]["hashtags"]["woeids"])
        self.all_cities = file_to_list(settings["tweet"]["hashtags"]["all cities"])
        self.searchspace = settings["tweet"]["hashtags"]["searchspace"]


class Header:
    def __init__(self):
        self.init()


    def init(self):
        self.load_settings()
        self.evaluate_settings()


    def create(self):
        self.select_header()
        self.emojify_header()
        self.merge()


    def merge(self):
        self.header = self.header_with_emojis + self.hashtag


    def select_header(self):
        with open(self.header_source) as header:
            headers = header.read().split("\n\n")
            i = randint(0, len(headers)-1)

            self.plain_header = headers[i]
    


    def emojify_header(self):

        # Splits the words in the twitter-header.
        words_in_header = self.plain_header.split()

        # Places emojis inn between words, and appends emojis before and after.
        self.fill_with_emojis(words_in_header)


    def fill_with_emojis(self, words):
        remaining_chars = self.max_chars - len(''.join(words)) - (self.meme_amp * 2) - len(self.hashtag)
        avg = remaining_chars / (len(words))

        self.emojis = list(self.emojis_dict.keys())
        self.probabilities = list(self.emojis_dict.values())

        emoji_prefix = self.create_prefix_or_suffix()
        emoji_suffix = self.create_prefix_or_suffix()

        if avg < 1:
            self.header_with_emojis = emoji_prefix + self.plain_header + emoji_suffix
        else:
            emojified_message = self.smash_emojis_between_words(words, avg)
            self.header_with_emojis = emoji_prefix + emojified_message + emoji_suffix


    def smash_emojis_between_words(self, words, avg):
        emojified_message = ''

        for i, word in enumerate(words, 1):
            emojified_message += word

            if i == len(words):
                break

            for i in range(randint(1, int(avg) if avg < 5 else 5)):
                emojified_message += ''.join(numpy.choice(self.emojis, size=1, p=self.probabilities))

        return emojified_message


    def create_prefix_or_suffix(self):
        return ''.join(numpy.choice(self.emojis, size=self.meme_amp, p=self.probabilities))


    def evaluate_settings(self):
        pass


    def load_settings(self):
        settings = json_to_dict("/resources/settings.json")

        self.hashtag = ""
        self.header = ""
        self.emojis_dict = json_to_dict(settings["tweet"]["emojis"]["source"])
        self.meme_amp = settings["tweet"]["emojis"]["amplitude"]
        self.header_source = sys.path[0] + settings["tweet"]["text"]["source"]
        self.max_chars = settings["tweet"]["text"]["max chars"]

class Image:
    def __init__(self):
        self.init()

    def create(self):
        self.choose_background_image()
        self.create_background_image()
        self.create_text_layer()
        self.merge_layers()

    def save(self):
        self.image.save(self.image_path)


    def init(self):
        self.load_settings()
        self.evaluate_settings()


    def choose_background_image(self):
        url = f'https://picsum.photos/{self.width}/{self.height}/'
        urlretrieve(url, self.image_path)


    def create_background_image(self):
        self.image = IMG.open(self.image_path)


    def create_text_layer(self):
        self.text_layer = IMG.new('RGBA', (self.width, self.height), None)
        
        self.create_font()
        self.create_draw_object()
        self.get_text()
        self.split_text()
        self.draw_text()


    def get_text(self):
        list_of_text = file_to_list(self.text_source)
        i = randint(0, len(list_of_text)-1)

        self.text = list_of_text[i]
    

    def draw_text(self):
        self.get_text_height()
        self.get_paragraph_height()

        y = self.get_vertical_pos()

        for line in self.lines:
            x = self.get_horizontal_pos(line)

            if self.has_shadow():
                self.draw.text((x + self.shadow_offset, y + self.shadow_offset), line, "black", self.font)
            
            self.draw.text((x, y), line, "white", self.font)

            y += self.text_height


    def get_vertical_pos(self):
        if self.text_align_vertical.lower() == "center":
            return int(self.height / 2 - self.paragraph_height / 2)

        elif self.text_align_vertical.lower() == "top":
            return int(self.height * self.margin)

        elif self.text_align_vertical.lower() == "bottom":
            return int(self.height * (1 - self.margin) - self.paragraph_height)


    def get_horizontal_pos(self, line):
        text_width = self.font.getsize(line)[0]

        if self.text_align_horizontal.lower() == "center":
            return self.width / 2 - text_width / 2

        elif self.text_align_horizontal.lower() == "left":
            return self.width * self.margin

        elif self.text_align_horizontal.lower() == "right":
            return self.width * (1 - self.margin) - text_width


    def has_shadow(self):
        if self.shadow_offset > 0:
            return True
        else:
            return False


    def create_font(self):
        self.font = ImageFont.truetype(self.font_type, self.font_size)


    def create_draw_object(self):
        self.draw = ImageDraw.Draw(self.text_layer)



    def get_text_height(self):
        self.text_height = self.font.getsize(self.lines[0])[1]


    def get_paragraph_height(self):
        self.paragraph_height = self.text_height * len(self.lines)


    def split_text(self):
        self.lines = wrap(self.text, self.chars_per_line)


    def merge_layers(self):
        self.image.paste(self.text_layer, (0, 0), self.text_layer)


    def load_settings(self):
        settings = json_to_dict("/resources/settings.json")

        self.text_source = settings["image"]["image text source"]
        self.text_align_horizontal = settings["image"]["horizontal align"]
        self.text_align_vertical = settings["image"]["vertical align"]
        self.shadow_offset = settings["image"]["shadow offset"]
        self.font_type = sys.path[0] + settings["image"]["font source"]
        self.font_size = settings["image"]["font size"]
        self.margin = settings["image"]["margin"]
        self.width = settings["image"]["size"]["width"]
        self.height = settings["image"]["size"]["height"]
        self.chars_per_line = settings["image"]["chars per line"]
        self.image_path = sys.path[0] + settings["image"]["image file"]


#######################
#   WORK IN PROGRESS
#######################
    def evaluate_settings(self):
        max_size = 2000
        min_size = 240

        for size in [self.width, self.height]:
            if size > max_size:
                raise SizeError(f'Error: Any given size can not exceed {max_size}px')
            if size < min_size:
                raise SizeError(f'Error: Any given size can not be less than {min_size}px')

class SizeError(Exception): pass