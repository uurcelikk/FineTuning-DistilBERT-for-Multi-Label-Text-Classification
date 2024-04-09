## Code Explanation
""" 
This code is used to scrape quotes from a specific website. The purpose of the code is as follows:

1. First, we import the necessary libraries: `pandas`, `urllib.request`, and `BeautifulSoup`.

2. We define a function called `extract_quotes_from_page`. This function is used to extract quotes from a specific page.

3. We define a variable named `base_url`. This variable contains the base URL of the website from which we will scrape quotes.

4. We use a loop to call the `extract_quotes_from_page` function for each page and collect the quotes.

5. We convert the obtained quotes into a DataFrame and save them to a CSV file.

The purpose of this code is to fetch quotes from a specific website, transform these quotes into a DataFrame, and store them in a CSV file. The reason for explaining this code in markdown is 
"""

import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

def extract_quotes_from_page(page_url):
    """Fetches quotes from a single page."""

    with urlopen(page_url) as page:
        soup = BeautifulSoup(page, 'html.parser')

    quotes = soup.find_all('div', class_='quote')# Find all div elements with class 'quote'

    return [
        {    # Extract features
            'quote': quote.find('span', class_='text').text,
            'author': quote.find('small', class_='author').text,
            'tags': [tag.text for tag in quote.find('div', class_='tags').find_all('a')]
         } 
        for quote in quotes
    ]

if __name__ == '__main__':
    base_url = 'https://quotes.toscrape.com/page/'
    all_quotes = []

    for page_num in range(1, 11):
        url = base_url + str(page_num) + '/'
        all_quotes.extend(extract_quotes_from_page(url))
        
    # Create a DataFrame from the scraped quotes and save to a CSV file
    df = pd.DataFrame(all_quotes, columns=['quote', 'author', 'tags'])
    df.to_csv('quotes.csv', index=False)
