import tweepy
import praw
from config import *
from arxiv_fetcher import get_papers_from_last_week
from twitter_analyzer import search_tweets
from reddit_analyzer import search_reddit_posts

# Set up Tweepy
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

# Set up PRAW
reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_SECRET,
                     user_agent=REDDIT_USER_AGENT,
                     username=REDDIT_USERNAME,
                     password=REDDIT_PASSWORD)

# Fetch arXiv papers from the last week
paper_urls = get_papers_from_last_week()

# Search tweets and Reddit posts containing the paper URLs
tweets = search_tweets(paper_urls, api)
reddit_posts = search_reddit_posts(paper_urls, reddit)

# TODO: Analyze the popularity of the tweets and Reddit posts
# TODO: Identify the most popular papers
# TODO: Perform further analysis on the most popular papers, if necessary
