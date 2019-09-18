import sys
import tweepy  # Twitter module
from pre_processing import json_to_list, file_to_list, json_to_dict

# Sånne greier vi trenger for autentikasjon
api_key, api_secret = "WO1t9lUsG8OjAoEnJrU37Ohzd", "31YhGtvSEadWkN5uL5FEdFpd4ddW4VtcaIW4sKJ92bkStBuAX2"
token_key, token_secret = "1166347129025155072-EaGxHUB9bUf5ImDmdyXOXPq4U5cZSZ", "bbJtob2GjLx4of2NwTYjMkw7OdBhhFzimufoFzySPFzKd"

# Konstruksjon av et objekt vi kan bruke. bla bla bla--
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(token_key, token_secret)
api = tweepy.API(auth)


def bot(header):
    # Tweet
    print("Posting image.")
    #api.update_with_media(sys.path[0] + '/resources/photo_of_the_day.jpg', header)
    print("Image posted.")

def get_hashtags(location, settings):
    woeids = json_to_list(settings["text"]["hashtags"]["woeids"])
    keywords = file_to_list(settings["text"]["hashtags"]["keywords"])
    cities = file_to_list(settings["text"]["hashtags"]["cities to search"])
    searchspace = settings["text"]["hashtags"]["searchspace"]

    # Dette er den mest vederstyggerlige linjen noensinne skrevet.
    hashtag_woeids = [woeid["woeid"] for i, city in enumerate(cities) if not i > searchspace for woeid in woeids if woeid["city"] == city]
    pass


    


if __name__ == "__main__":
    settings = json_to_dict("/resources/settings.json")
    get_hashtags("New York", settings)
