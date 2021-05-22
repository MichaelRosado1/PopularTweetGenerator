import re
import json
import random
import os
import tweepy
from dotenv import load_dotenv
from graph import Graph, Vertex
load_dotenv()

# API KEYS
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET_KEY = os.getenv('CONSUMER_SECRET_KEY')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
ACCESS_KEY = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def makeGraph(words):
	g = Graph()

	previousWord = None

	for word in words:
		wordVertex = g.getVertex(word)

		if previousWord:
			previousWord.incrementEdge(wordVertex)

		previousWord = wordVertex

	g.generateProbMapping()
	return g


#This function will search through the latest top trending tweet and return a list of words
def getWordsFromTweets(topic):
	tweets = api.search(q=topic, result_type='popular')
	text = ""
	for tweet in tweets:
		text += tweet.text

	text = re.sub(r'https?:\/\/\S*', '', text, flags=re.MULTILINE)
	text = text.split()
	return text


def postTweet(tweet):
	try:
		#api.update_status(status = tweet)
		print('Tweet sent successfully')
		print('Posted Tweet: ')
		print(tweet)
	except:
		print('Encountered error while trying to update status')

def compose(g, tweet, length=50):
	composition = []

	word = g.getVertex(random.choice(tweet))
	for _ in range(length):
		composition.append(word.value)
		word = g.getNextWord(word)
	return composition


def main(): 
	tweet = getWordsFromTweets('Basketball')
	g = makeGraph(tweet)
	composition = compose(g, tweet, 20)
	print(' '.join(composition))
	#postTweet(' '.join(composition))



main()
