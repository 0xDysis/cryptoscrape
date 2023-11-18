import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def scrape_and_tally(url, words_to_tally):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')
    text = soup.get_text()
    words = text.split()
    filtered_words = [word for word in words if word.lower() in words_to_tally]
    word_count = Counter(filtered_words)
    return word_count


with open('words.txt', 'r') as f:
    words_to_tally = {re.sub(r'\d+', '', line).strip().lower() for line in f if line.strip()}

urls = ['https://www.coindesk.com/']

for url in urls:
    word_count = scrape_and_tally(url, words_to_tally)
    print(f'URL: {url}')
    for word, count in word_count.most_common(100):
        print(f'{word}: {count}')
    print('\n')