# @Inspira39021145
import tweepy

api_key = "WO1t9lUsG8OjAoEnJrU37Ohzd"
api_secret = "31YhGtvSEadWkN5uL5FEdFpd4ddW4VtcaIW4sKJ92bkStBuAX2"

token_key = "1166347129025155072-EaGxHUB9bUf5ImDmdyXOXPq4U5cZSZ"
token_secret = "bbJtob2GjLx4of2NwTYjMkw7OdBhhFzimufoFzySPFzKd"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(token_key, token_secret)
api = tweepy.API(auth)

api.update_status("Tweet")