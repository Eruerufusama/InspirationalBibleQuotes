# Home-made family recipes
from functions import json_to_dict, json_to_list, file_to_list
from image import Image
from header import Header

# Third party modules
import tweepy
from random import choice

class Tweet:
    def __init__(self):
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
        self.image.save()


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

        self.bot.update_with_media(image, header)


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

    
    def evaluate_settings(self):
        pass