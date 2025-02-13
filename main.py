import requests
import sqlite3
from bs4 import BeautifulSoup
import time
from database import connection, create_database

# news download function
def fetch_news():
    url = "https://www.pkp.pl/pl/pkp-aktualnosci"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_items = soup.select('.item-content')
    news_list = []

    for item in news_items:
        title = item.select_one('.page-header').text.strip()
        date = item.select_one('.published').text.strip()
        link = item.select_one('a')['href']
        full_link = f"https://www.pkp.pl{link}" if not link.startswith('http') else link
        news_list.append((title, date, full_link))
    return news_list

# function, that adds news to the database
def add_news_to_db(news_list):
    conn = connection()
    cursor = conn.cursor()

    for title, date, link in news_list:
        try:
            cursor.execute('''
                INSERT INTO news (title, date, link)
                VALUES (?, ?, ?)
            ''', (title, date, link))
        except sqlite3.IntegrityError:
            continue

    conn.commit()
    conn.close()

# main function serve process
def main():
    create_database()

    while True:
        news_list = fetch_news()
        add_news_to_db(news_list)
        print(f"Added {len(news_list)} new entries.")
        time.sleep(3600)

if __name__ == "__main__":
    main()