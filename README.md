# InspirationalBibleQuotes
A twitter-bot that posts inspirational bible quotes onto wallpapers.

In actuality it's more of a template-bot that can be tweaked to suit any kind of twitter-bot that posts images with some text overlaid onto it. Feel free to use it for whatever, however, we do not take responsibility for any malicious uses. Please be polite, and do not act in bad faith.

## How to use.
1.  Clone the repository.

2.  Create a twitter developer account and get access tokens to authorize your own bot. If you are unfamiliar with how to do this, look up a recent tutorial. 

3.  run "pip install -r requirements.txt"

4.  Open the settings.json and configure them to your needs. They should be relatively self-explanatory.

5.  Insert your authentication-tokens in the settings-file.

6.  to run the program, simply execute "run.py".

## Explaining what the resource-files are used for.
If you want to customize the bot to your needs, knowing how the program handles it's resources is important.

### bible_list.txt
  is a file that seperates each verse on newline, or "\n" in python-jargon. If you want to replace this file with your own, without messing around with the code, format the file in the same structure as this.
  You can change the source-file in settings.json.

### emojis.json
  If you have enabled emojis in the settings-file, congratulations! You are a person of culture. In this file you'll find emojis and their respective probability-distribution in a key-value pair. Replace the emojis with whatever emojis you like, and change their respective probability to increase or decrease their occurance-frequency. Higher numbers means more likely to appear.

### keywords.txt
  is structured the same way bible_list is structured.
  This file is used to match against trending hashtags. To put simply, if you want to automatically pull hashtags from trending hashtags, replace the words in this file with the words you want to potentially include in your hashtags.
  As of now, the matching-function the program uses is quite basic, but we plan to impliment a regex as of a later date. #probablyNeverGonnaHappen

### list_of_cities.txt
  This file is structured the same as the previous two txt-files.
  When the program runs, it will use the "searchspace" parameter from the settings-file to decide how many cities it will find hashtags from. It runs sequencially through the file, from top to bottom.

### settings.json
  has settings in it.

### tweet_headers.txt
  Every tweet in this file is split on double newline instead of single. ("\n\n")
  Replace these lines with whatever you want the bot to possibly tweet.

### woeid.json
  list of dictonary-objects containing Yahoo! world ids of every american city. You can replace these with whatever woeids you want. These can be obtained with a simple api-request to twitters api. Read the documentation for more info about this.