import tweepy,random


class TweetMonkey(object):
	def __init__(self):
		# put all your access tokens and whatnot here		
		auth = tweepy.OAuthHandler('', '')
		auth.set_access_token('', '')

		self.api = tweepy.API(auth)

	def tweet(self,word):
		try:	
			self.api.update_status(status=word)
		except Exception as e:
			print e
