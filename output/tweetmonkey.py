import tweepy,random


class TweetMonkey(object):
	def __init__(self):
		# put all your access tokens and whatnot here		
		auth = tweepy.OAuthHandler('', '')
		auth.set_access_token('', '')

		self.api = tweepy.API(auth)
		self.api.update_status(status='heya'+str(random.randint(0,100)))

	def tweet(self,word):
		self.api.update_status(status=word)
