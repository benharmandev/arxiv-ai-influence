import arxiv
import datetime

def get_papers_from_last_week():
    # Calculate the date one week ago
    last_week_date = datetime.datetime.now() - datetime.timedelta(weeks=1)

    # Query the arXiv API for AI papers published in the last week
    query = f"cat:cs.AI AND submittedDate:[{last_week_date.strftime('%Y%m%d')}0000 TO *]"
    papers = arxiv.query(query, max_results=1000, sort_by="submittedDate", sort_order="descending")

    # Extract the paper URLs
    paper_urls = [paper["id"] for paper in papers]

    return paper_urls
