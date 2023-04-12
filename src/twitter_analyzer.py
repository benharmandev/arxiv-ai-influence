import tweepy

def search_tweets(paper_urls, api):
    tweets = []

    for url in paper_urls:
        # Search for tweets containing the paper URL
        query = f"url:{url}"
        results = tweepy.Cursor(api.search_tweets, q=query).items(120)

        for tweet in results:
            tweets.append(tweet)

    return tweets
