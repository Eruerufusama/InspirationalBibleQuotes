from random import choice


def create_header():
    header = select_header()
    return fill_header_with_emojis(header, 4)


def select_header():
    with open('tweet_headers.txt') as header:
        return choice(header.read().split("\n"))


def fill_header_with_emojis(header, meme_amplitude):
    returnstring = ""

    with open("emojis.txt", encoding="utf-8") as emoji_file:
        emojis = emoji_file.read().split()

        for i in range(meme_amplitude):
            returnstring += choice(emojis)

        splitted_header = header.split()

        for word in splitted_header:
            returnstring += word
            for i in range(meme_amplitude):
                returnstring += choice(emojis)
    return returnstring

    