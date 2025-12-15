import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

# this is the website we will scrape
load_dotenv()
URL = os.environ.get("Scrape_URL")
# I will go to the website and get hte HTML content 

if not URL:
    print("Scrape_URL environment variable not set")
    exit()

response = requests.get(URL)

# Now we check if the request was successful 

if response.status_code == 200:
    print("Successfully accessed the website")

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # find the first book element on the page and print its title
    first_book = soup.find("article", class_="product_pod")
    first_book_price = soup.find("div", class_="product_price")
    if not first_book_price:
        print("Price tag not found on the page")
        exit()

    if not first_book:
        print("No book elements found on the page")
        exit()

    h3_tag = first_book.find("h3")
    book_title_tag = h3_tag.find("a") if h3_tag else None

    first_book_price = first_book.find("p", class_="price_color")
    
    if not book_title_tag or not first_book_price:
        print("Book title or price tag not found")
        exit()

    # the title is stored in the 'title' attribute on the link
    book_title = book_title_tag.get("title") or book_title_tag.text.strip()
    book_price = first_book_price.text
    print("First book title:", book_title)
    print("First book price:", book_price)
else:
    print("Failed to access the website")
    exit()