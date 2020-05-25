import requests
from bs4 import BeautifulSoup
import csv

URL = "https://mvs.gov.ua/ua/news"
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'accept': '*/*'
}

FILE = 'news.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('a', class_='pagination__item')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Дата', 'Заголовок', 'Просмотры', 'Ссылка'])
        for item in items:
            writer.writerow(
                [item['date'], item['title'], item['views'], item['link']])


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='article new-item')
    news = []
    for item in items:
        news.append({
            'date': item.find('span', class_='article__date').get_text(),
            'title': item.find('a', class_='article__title').get_text(),
            'views': item.find('span', class_='article__watches').get_text(),
            'link': item.find('a', class_='article__title').get('href')
        })
    return news


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        news = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f'Парсинг страницы: {page} из {pages_count}...')
            html = get_html(URL, params={'page': page})
            news.extend(get_content(html.text))
        print(pages_count)
        print(news)
        print(f'Получено {len(news)} новостей')
        save_file(news, FILE)
    else:
        print('Error')


parse()
