import threading,logging,random,string
from workers.monkey import *
from textparser.parsermonkey import *
from output.tweetmonkey import *

logging.basicConfig(level=logging.DEBUG, 
	format='[%(asctime)s]:(%(threadName)s): %(message)s',
	datefmt='%m/%d/%Y %I:%M:%S %p',
	filename='log.txt')

class MonkeyMama(object):
	def __init__(self):
		jim = ParserMonkey()
		self.text = jim.getMessage().split(" ")
		self.cursor = 0
		self.monkeyList = []
		self.pam = TweetMonkey()

	def main(self):
		for a in range(0,100):
			self.monkeyList.append(Monkey(self))
			self.monkeyList[a].updateWord(self.text[self.cursor])
			self.monkeyList[a].run()

	def reportVictory(self,word):
		self.cursor+=1
		for a in self.monkeyList:
			a.updateWord(self.text[self.cursor])
			pam.tweet(word+" ("+str(round(self.cursor/len(self.text)))+' percent complete)')


if __name__=='__main__':
	dee = MonkeyMama()
	dee.main()