# As we are using Python for web screping, let's first download the necessary libraries.
# run pip install requests and pip install beautifulsoup4 .

# Using python, we can for example scrape a website and print its HTML content. As in this case we will be using example.com since it doesnt block bots as other websites do (linkedin etc)



#import requests
#from bs4 import BeautifulSoup

#def scrape():
   #url = 'https://www.example.com'
    #response = requests.get(url)
    #soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)



# Now after this we can run this script in terminal using: python scraper_python.py

# Awesome, it works. 
# Similarly I can do web scraping using javascript. But for now as it is not needed, and since I want to specialise myself in python, I will not do it now.

#BeautifulSoup and cheerio are libraries that help us navigate HTML in code. They allow us to pass in certain paths and patterns to get certain snippets of HTML.

#Let’s go ahead and capture 3 things from this page: The title, the text, and the “More information…” link.

#We’ll use CSS Selectors to find these elements in the HTML. CSS Selectors are notations used to locate HTML elements, and they are very easy to learn. Can be found here: https://www.w3schools.com/cssref/css_selectors.php

#Let’s capture the title, text, and extract the link from the <a> tag. Add these lines to your code.
#Python:



#import requests
#from bs4 import BeautifulSoup

#def scrape():
    #url = 'https://www.example.com'
    #response = requests.get(url)
    #soup = BeautifulSoup(response.text, 'html.parser')
    #title = soup.select_one('h1').text
    #text = soup.select_one('p').text
    #link = soup.select_one('a').get('href')
    #print(title)
    #print(text)
    #print(link)
    
#if __name__ == '__main__':
    #scrape()



# As we have noticed, this scraper works succesfully. But we still want to save this information in SQL database for future use. So let's do that now.

import requests
from bs4 import BeautifulSoup
import sqlite3

def scrape_and_save_to_db():
    # Scrape the website
    url = 'https://www.example.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract title, text, and link
    title = soup.select_one('h1').text
    text = soup.select_one('p').text
    link = soup.select_one('a').get('href')
    
    # Print the scraped data
    print(title)
    print(text)
    print(link)
    
    # Save to SQLite database
    conn = sqlite3.connect('scraped_data.db')  # Creates a database file
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scraped_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            text TEXT,
            link TEXT
        )
    ''')
    
    # Insert data into the table
    cursor.execute('''
        INSERT INTO scraped_data (title, text, link)
        VALUES (?, ?, ?)
    ''', (title, text, link))
    
    # Commit and close the connection
    conn.commit()
    conn.close()
    print("Data saved to database successfully!")

if __name__ == '__main__':
    scrape_and_save_to_db()