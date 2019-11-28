from twitter import Tweet

if __name__ == "__main__":
    tweet = Tweet()

    tweet.create_header()
    tweet.create_image()

    tweet.post()
