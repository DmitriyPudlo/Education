import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/all/'

response = requests.get(url)

soup = BeautifulSoup(response.text, features='lxml')

soup = soup.find('div', class_='tm-article-snippet')

print(soup)
