import requests
import os

# API configuration
API_KEY = os.getenv('NEWS_API_KEY', '4a391eb2d1394a038152fb079373b327')  # Default API key if not set in environment
BASE_URL = 'https://newsapi.org/v2/everything'
QUERY = 'tesla'
FROM_DATE = '2024-07-20'
SORT_BY = 'publishedAt'


def fetch_news():
    url = f"{BASE_URL}?q={QUERY}&from={FROM_DATE}&sortBy={SORT_BY}&apiKey={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        articles = data.get('articles', [])

        if not articles:
            print("No articles found.")
            return

        for index, article in enumerate(articles):
            print(f"{index + 1}. {article['title']}")
            print(f"   Source: {article['source']['name']}")
            print(f"   Published At: {article['publishedAt']}")
            print(f"   URL: {article['url']}\n")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")


fetch_news()
# if __name__ == "__main__":
#     fetch_news()
