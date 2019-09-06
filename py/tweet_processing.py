from random import choice, randint
import numpy.random as numpy
import pre_processing
import admin_emoji


def create_header():
    header = select_header()
    return fill_header_with_emojis(header, 6)


def select_header():
    with open('../resources/tweet_headers.txt') as header:
        message = choice(header.read().split("\n\n"))
        return message


def fill_header_with_emojis(header, meme_amplitude):

    emoji_dict = admin_emoji.json_to_dict('../resources/emojis.json')
    split_header = header.split()

    max_chars = 240
    # Remaining number of characters allowed in a tweet
    remaining_chars = max_chars - len(''.join(split_header)) - (meme_amplitude * 2)
    # Average emojis per word in tweet
    avg = remaining_chars / (len(split_header))

    emoji_keys = list(emoji_dict.keys())
    emoji_values = list(emoji_dict.values())
    premojis = ''.join(numpy.choice(emoji_keys, size=meme_amplitude, p=emoji_values))
    postmojis = ''.join(numpy.choice(emoji_keys, size=meme_amplitude, p=emoji_values))
    emojified_message = ''

    # If tweet is to long to add emojis between words
    if avg < 1:
        returnstring = premojis + header + postmojis

    else:
        for i, word in enumerate(split_header, 1):
            emojified_message += word
            # Don't add emojis behind last word, postmojis covers this.
            if i == len(split_header):
                break
            # Insert random number of emojis if average is less than 5
            for i in range(randint(1, int(avg) if avg < 5 else 5)):
                # Replace with function returning emojis relative to probability
                emojified_message += ''.join(numpy.choice(emoji_keys, size=1, p=emoji_values))

    returnstring = premojis + emojified_message + postmojis
    return returnstring