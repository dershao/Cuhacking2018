import praw
from random import randint
import webbrowser
from . import subreddits
from . import keys


def getRedditInstance():
	"""
	Get the Reddit instance to make API calls.

	"""

	reddit = praw.Reddit(client_id=keys.praw["client_id"], client_secret=keys.praw["client_secret"], user_agent=keys.praw["user_agent"])
	return reddit

def getSubredditInstance(reddit, subreddit):
	"""
	Get subreddit instance from specified subreddit string.

	"""

	sub = reddit.subreddit(subreddit)

	return sub

def getRandomSubmission(subreddit):
	"""
	Get random subreddit submission from specified subreddit instance.

	"""
	topMonthlyPosts = subreddit.top('month')
	index = randint(0, 4)

	i = 0
	for post in topMonthlyPosts:
		print(post)
		if (i == index):
			print(post, " inside for loop")
			return post.url

		i = i + 1

def pickSubreddit(emotion):
	"""
	Pick a subreddit based on specified emotion.
	"""
	return subreddits.EMOTION_DICTIONARY[emotion]

def getContent(emotion):
	"""
	Get random content based on specified emotion.
	"""
	reddit = getRedditInstance()
	pickedSub = pickSubreddit(emotion);
	subreddit = getSubredditInstance(reddit, pickedSub)
	randomSubmission = getRandomSubmission(subreddit)

	return randomSubmission

if __name__ == "__main__":

	#testing reddit scraping
	reddit = getRedditInstance()
	pickedSub = pickSubreddit("sad");
	subreddit = getSubredditInstance(reddit, pickedSub)
	randomSubmission = getRandomSubmission(subreddit)
	webbrowser.open(randomSubmission)
