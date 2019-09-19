import tweepy

# Sånne greier vi trenger for autentikasjon
api_key, api_secret = "WO1t9lUsG8OjAoEnJrU37Ohzd", "31YhGtvSEadWkN5uL5FEdFpd4ddW4VtcaIW4sKJ92bkStBuAX2"
token_key, token_secret = "1166347129025155072-EaGxHUB9bUf5ImDmdyXOXPq4U5cZSZ", "bbJtob2GjLx4of2NwTYjMkw7OdBhhFzimufoFzySPFzKd"

# Konstruksjon av et objekt vi kan bruke. bla bla bla--
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(token_key, token_secret)
api = tweepy.API(auth)

api.trends_place()