import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")

def get_financial_news(query="general", page_size=10):
    """
    Fetch financial news using Finnhub API
    query can be: "general", "forex", "crypto", "merger" or specific stock symbols
    """
    # Ensure query is never empty
    if not query or query.strip() == "":
        query = "general"

    # Map common queries to Finnhub categories
    category_mapping = {
        "stocks": "general",
        "oil": "general",
        "forex": "forex",
        "crypto": "crypto",
        "markets": "general",
        "general": "general"
    }

    # Try to map query to category, default to general
    category = category_mapping.get(query.lower().strip(), "general")

    url = f"https://finnhub.io/api/v1/news"
    params = {
        "category": category,
        "token": FINNHUB_API_KEY,
    }

    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()
    data = response.json()

    # Finnhub returns news in different format, let's standardize it
    articles = []
    for item in data[:page_size]:  # Limit to requested page_size
        # Convert Unix timestamp to readable date
        timestamp = item.get("datetime", 0)
        if timestamp:
            try:
                # Convert Unix timestamp to datetime string
                published_date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            except (ValueError, OSError):
                published_date = "Unknown"
        else:
            published_date = "Unknown"
            
        article = {
            "title": item.get("headline", "No title"),
            "description": item.get("summary", "No description available"),
            "url": item.get("url", ""),
            "source": {"name": item.get("source", "Finnhub")},
            "publishedAt": published_date,
            "image": item.get("image", "")
        }
        articles.append(article)

    return articles
