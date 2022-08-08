import requests
from bs4 import BeautifulSoup

url = 'https://2ip.ru/'

response = requests.get(url)

soup = BeautifulSoup(response.text, features='lxml')

soup = soup.find('div', class_='ip').find('span').text

print(soup)
