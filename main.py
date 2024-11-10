from bs4 import BeautifulSoup
import requests

# Send a GET request to the Hacker News website and retrieve the HTML content
response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

# Parse the HTML content using BeautifulSoup with the "html.parser" parser
soup = BeautifulSoup(yc_web_page, "html.parser")

# Select all article elements with the class "titleline" and extract the first article links
articles = [a.find() for a in soup.select(".titleline")]

articles_texts = []
articles_links = []

# Loop through each article element to extract and store the text and link
for article_tag in articles:
    text = article_tag.getText()
    articles_texts.append(text)
    link = article_tag.get("href")
    articles_links.append(link)

# Extract and convert upvote counts for each article into integers
articles_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# Find the highest upvote count and the index of the article with the most upvotes
max_value = max(articles_upvotes)
index_value = articles_upvotes.index(max_value)

print(str(max_value)+" points:-", articles_texts[index_value])


