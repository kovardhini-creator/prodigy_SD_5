## Task 5 – Web Scraping: Book Data from Online Store

Prodigy Infotech Internship | Web Development / Data Scraping

📝 Overview

This project demonstrates the use of Python for web scraping, specifically targeting book data from the online site Books to Scrape. The goal is to extract book titles, prices, and ratings from the main catalog page and display the data in a visually formatted HTML table.

🛠️ Features

 🔍 Extracts Title, Price, and Rating of each book listed

 📄 Outputs the results to a styled HTML file (books.html)

 🧠 Uses requests and BeautifulSoup libraries for HTTP and HTML parsing

 🎨 Clean, responsive table layout with CSS styling

 💾 Saves output in a reusable, offline-readable HTML document

🔗 Target Website

  URL: http://books.toscrape.com/
 A sandbox site used widely for practicing web scraping.

💡 Logic & Workflow

~ Send a GET request to fetch HTML content.

~ Parse HTML with BeautifulSoup to extract book details.

~ Loop through each <article class="product_pod"> to extract:

~ Book title (from <h3><a> title attribute)

~ Price (from <p class="price_color">)

~ Rating (from CSS class in <p class="star-rating">)

~ Write the extracted data into an HTML table using inline CSS for better presentation.

📂 Output File

File Name: books.html
Contains:

~ A stylized HTML table with the following columns:

📖 Book Title

💰 Price

⭐ Rating (e.g., One, Two, Three)

🖥️ Technologies Used
Python

~ requests – For sending HTTP requests

~ BeautifulSoup – For HTML parsing

~ HTML + CSS – For styled output display

👨‍💻 Code Entry Point

python task5.py

The script will create a file named books.html in the current directory.

🧑 Author

Name: A. Kovardhini
Course: B.Sc. Computer Science with Artificial Intelligence
Internship Role: Web Development Intern, Prodigy Technologies
📧 Email: a.kovardhini1410@gmail.com

