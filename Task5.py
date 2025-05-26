import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "http://books.toscrape.com/"

# Send an HTTP GET request
response = requests.get(url)

# If response is successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    # Create/open an HTML file to save styled content
    with open("books.html", mode="w", encoding="utf-8") as file:
        file.write("""
        <html>
        <head>
            <title>Books to Scrape - Web Scraping</title>
            <style>
                body { font-family: Arial; background-color: #f4f4f4; padding: 20px; }
                h1 { text-align: center; }
                table { width: 80%; margin: auto; border-collapse: collapse; }
                th, td { border: 1px solid #999; padding: 10px; text-align: center; }
                th { background-color: #333; color: white; }
                tr:nth-child(even) { background-color: #eee; }
            </style>
        </head>
        <body>
            <h1>Books Data</h1>
            <table>
                <tr><th>Title</th><th>Price</th><th>Rating</th></tr>
        """)

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            rating_class = book.p["class"][1]  # One, Two, Three, etc.

            file.write(f"<tr><td>{title}</td><td>{price}</td><td>{rating_class}</td></tr>\n")

        file.write("""
            </table>
        </body>
        </html>
        """)

    print("Scraping successful! Data saved to 'books.html'.")
else:
    print("Failed to retrieve the webpage.")