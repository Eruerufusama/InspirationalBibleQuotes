from pre_processing import json_to_dict, write_to_json
from sys import argv

def main():
  if argv[1] == "-r" or argv[1] == "--recover" or argv[1] == "--restore":
    recover_settings()
  else:
    reset_settings()

def recover_settings():
  settings = json_to_dict("/resources/settings_recover.json")
  write_to_json("/resources/settings.json", settings)

def reset_settings():
  settings = json_to_dict("/resources/settings.json")
  write_to_json("/resources/settings_recover.json", settings)

  if argv[1] == "-a" or argv[1] == "--auth":
    settings["auth"]["api private key"] = ""
    settings["auth"]["api public key"] = ""
    settings["auth"]["token private key"] = ""
    settings["auth"]["token public key"] = ""

  settings["image"]["image text source"] = "/resources/bible_list.txt"
  settings["image"]["font source"] = "/fonts/Roboto-Medium.ttf"
  settings["image"]["image file"] = "/resources/photo_of_the_day.jpg"
  settings["image"]["size"]["height"] = 1080
  settings["image"]["size"]["width"] = 1080
  settings["image"]["margin"] = 0.1
  settings["image"]["chars per line"] = 40
  settings["image"]["font-size"] = 44
  settings["image"]["shadow offset"] = 2
  settings["image"]["horizontal align"] = "left"
  settings["image"]["vertical align"] = "top"

  settings["tweet"]["hashtags"]["woeids"] = "/resources/woeid.json"
  settings["text"]["hashtags"]["keywords"] = "/resources/keywords.txt"
  settings["tweet"]["hashtags"]["all cities"] = "/resources/list_of_cities.txt"
  settings["tweet"]["hashtags"]["searchspace"] = 10
  settings["tweet"]["emojis"]["source"] = "/resources/emojis.json"
  settings["tweet"]["emojis"]["amplitude"] = 4
  settings["tweet"]["text"]["source"] = "/resources/tweet_headers.txt"
  settings["tweet"]["text"]["max chars"] = 240

  write_to_json("/resources/settings.json", settings)

if __name__ == "__main__":
    main()