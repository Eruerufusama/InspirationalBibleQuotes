import sys
import tweepy  # Twitter module
from pre_processing import json_to_list, file_to_list, json_to_dict
from random import choice

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

def get_hashtags(settings):
    hashtags = []

    woeids = json_to_list(settings["text"]["all_hashtags"]["woeids"])
    keywords = file_to_list(settings["text"]["all_hashtags"]["keywords"])
    cities = file_to_list(settings["text"]["all_hashtags"]["cities to search"])
    searchspace = settings["text"]["all_hashtags"]["searchspace"]
    
    hashtag_woeids = []
    for i, city in enumerate(cities):
        for woeid in woeids:
            if woeid["city"] == city:
                hashtag_woeids.append(woeid["woeid"])
                break
        if i > searchspace:
            break
    
    for woeid in hashtag_woeids:
        response = api.trends_place(woeid)
        all_hashtags = [trend["name"] for trend in response[0]["trends"] if trend["name"][0] == '#']
        
        for keyword in keywords:
            for hashtag in all_hashtags:
                # Some advanced Regex would be fantastic here.
                if keyword in hashtag and hashtag not in hashtags:
                    hashtags.append(hashtag)

    return choice(hashtags)

if __name__ == "__main__":
    get_hashtags(json_to_dict('/resources/settings.json'))