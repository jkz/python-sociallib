from sociallib import twitter


consumer = twitter.Consumer(key, secret)
token = twitter.Token(key, secret)
auth = twitter.Auth(consumer, token)
provider = twitter.Provider(auth=auth)
api = twitter.API(auth=auth)
