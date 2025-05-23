import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    with open("books.csv", mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Rating"])

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            rating_class = book.p["class"][1]

            writer.writerow([title, price, rating_class])

    print("Scraping successful! Data saved in 'books.csv'.")
else:
    print("Failed to connect to the website.")
