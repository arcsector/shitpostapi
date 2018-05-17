import tweepy
import praw
import datetime
from json import loads, dumps
import logging
from os import environ

#Authenticate with twitter
consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret'] 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

#get access token
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']
auth.set_access_token(access_token, access_token_secret)

#create api instance
api = tweepy.API(auth)

#get status url picture url
status = api.user_timeline(id='ShitpostBot5000', count=1)[0]
statusurl = status.entities['media'][0]['expanded_url']
statusurl = statusurl[:statusurl.find('/photo/')]
picurl = status.entities['media'][0]['media_url_https']
#authenticate with reddit
reddit = praw.Reddit(
	client_id=environ['client_id'], 
	client_secret=environ['client_secret'], 
	password=environ['password'], 
	user_agent=environ['user_agent'], 
	username=environ['username']
)

#check if previous post has same image url
postcomp = reddit.subreddit('ShitpostBot5000').new(limit=1)
postcomp = next(postcomp)
if postcomp.url != picurl:
	#post to reddit
	title = datetime.datetime.now() - datetime.timedelta(minutes=1)
	title = title.strftime('Shitpost: %B %d, %Y at %I:%M')
	url = picurl
	post = reddit.subreddit('ShitpostBot5000').submit(title=title, url=url)
	reddit.submission(id=post.id).reply("Twitter Link: "+statusurl)
else:
	logging.error("Url is the same as the previous post")
