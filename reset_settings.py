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

  settings["canvas"]["margin"] = 0.1
  settings["canvas"]["size"]["height"] = 1080
  settings["canvas"]["size"]["width"] = 1080

  settings["image-data"]["filetype"] = "jpg"
  settings["image-data"]["quality"] = 100

  settings["text"]["characters per line"] = 40
  settings["text"]["font"] = "/fonts/Roboto-Medium.ttf"
  settings["text"]["font-size"] = 44
  settings["text"]["hashtags"]["cities to search"] = "/resources/list_of_cities.txt"
  settings["text"]["hashtags"]["keywords"] = "/resources/keywords.txt"
  settings["text"]["hashtags"]["searchspace"] = 10
  settings["text"]["hashtags"]["woeids"] = "/resources/woeid.json"
  settings["text"]["horizontal align"] = "left"
  settings["text"]["shadow offset"] = 2
  settings["text"]["text from source"] = "/resources/bible_verses.txt"
  settings["text"]["vertical align"] = "top"

  write_to_json("/resources/settings.json", settings)

if __name__ == "__main__":
    main()