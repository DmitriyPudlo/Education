import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/all/'

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'Java']

HEADERS = {'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415; '
                     '_gid=GA1.2.512914915.1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru; _ym_isad=2; '
                     '__gads=ID=87f529752d2e0de1-221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
          'Accept-Language': 'ru-RU,ru;q=0.9',
          'Sec-Fetch-Dest': 'document',
          'Sec-Fetch-Mode': 'navigate',
          'Sec-Fetch-Site': 'same-origin',
          'Sec-Fetch-User': '?1',
          'Cache-Control': 'max-age=0',
          'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/96.0.4664.93 Safari/537.36',
          'sec-ch-ua-mobile': '?0'
          }

response = requests.get(url, headers=HEADERS)

soup = BeautifulSoup(response.text, features='lxml')

soup = soup.findAll('div', class_='tm-article-snippet')
result = []
for all_info in soup:
    tags = all_info.findAll('a', class_='tm-article-snippet__hubs-item-link')
    for tag in tags:
        if tag.find('span').text in KEYWORDS:
            date = all_info.find('span', class_='tm-article-snippet__datetime-published').find('time').get('title')
            head = all_info.find('a', class_='tm-article-snippet__title-link').text
            url_col = 'https://habr.com' + all_info.find('a', class_='tm-article-snippet__title-link').get('href')
            result.append([date, head, url_col])


print(*result, sep='\n')
