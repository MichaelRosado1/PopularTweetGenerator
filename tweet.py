import os
import tweepy
from dotenv import load_dotenv
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

#This function will search through the latest top trending tweet and return a list of words
def getWordsFromTweets():
	tweets = api.search(q='basketball', result_type='popular')
	print(tweets[0])
	

def postTweet(tweet):
	try:
		api.update_status(status = tweet)
		print('Tweet sent successfully')
		print('Posted Tweet: ')
		print(tweet)
	except:
		print('Encountered error while trying to update status')


def main(): 
	tweet = "Hello, world!"
	#postTweet(tweet)
	getWordsFromTweets()



main()
