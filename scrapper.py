import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/all/'

response = requests.get(url)

soup = BeautifulSoup(response.text, features='lxml')

soup = soup.find('a', class_='tm-article-snippet__hubs-item-link')

print(soup)
