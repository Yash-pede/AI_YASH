import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.indiatoday.in/india')
soup = BeautifulSoup(r.content, 'html.parser')

titles = [h2.text for h2 in soup.find_all('h2')][:5]
for i in range(1, len(titles)+1):
    print(f"{i}. {titles[i-1]}")
