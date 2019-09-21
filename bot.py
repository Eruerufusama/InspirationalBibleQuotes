import sys
import tweepy
from pre_processing import json_to_list, file_to_list, json_to_dict
from random import choice


def twitter_object(settings):
  # Authentification variables
  api_key = settings["auth"]["api public key"]
  api_secret = settings["auth"]["api private key"]
  token_key = settings["auth"]["token public key"]
  token_secret = settings["auth"]["token private key"]

  # Applying authentification
  auth = tweepy.OAuthHandler(api_key, api_secret)
  auth.set_access_token(token_key, token_secret)
  return tweepy.API(auth)


def bot(header, settings):
  api = twitter_object(settings)
  api.update_with_media(sys.path[0] + '/resources/photo_of_the_day.jpg', header)


def get_hashtags(settings):
  hashtags = []

  woeids = json_to_list(settings["text"]["hashtags"]["woeids"])
  keywords = file_to_list(settings["text"]["hashtags"]["keywords"])
  cities = file_to_list(settings["text"]["hashtags"]["cities to search"])
  searchspace = settings["text"]["hashtags"]["searchspace"]

  hashtag_woeids = []
  for i, city in enumerate(cities):
    for woeid in woeids:
      if woeid["city"] == city:
        hashtag_woeids.append(woeid["woeid"])
        break
    if i > searchspace:
      break
  
  api = twitter_object(settings)

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
