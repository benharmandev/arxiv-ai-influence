# Collect Reddit posts containing paper URLs
def search_reddit_posts(paper_urls, reddit):
    posts = []

    for url in paper_urls:
        # Search for Reddit posts containing the paper URL
        search_results = reddit.subreddit("all").search(url, limit=120)

        for post in search_results:
            posts.append(post)

    return posts
