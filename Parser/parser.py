import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://auto.ria.com/newauto/marka-mercedes-benz/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'accept': '*/*'}

LINK = 'https://auto.ria.com'
FILE = 'cars.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='page-item mhide')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='proposition')
    cars = []
    for item in items:
        cars.append({
            'title': item.find('h3', class_='proposition_name').get_text(strip=True),
            'subtitle': item.find('div', class_='proposition_equip size13 mt-5').get_text(strip=True),
            'price_USD': item.find('div', class_='proposition_price').find_next('span').get_text(strip=True),
            'city': item.find('div', class_='proposition_region grey size13').find_next('strong').get_text(strip=True),
            'link': LINK + item.find('div', class_='proposition_equip size13 mt-5').find_next('a').get('href'),
            'gas': item.find('span', class_='i-block').get_text(),
        })
    return cars


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Марка', 'Описание', 'Цена', 'Город', 'Ссылка', 'Тип топлива'])
        for item in items:
            writer.writerow(
                [item['title'], item['subtitle'], item['price_USD'], item['city'], item['link'], item['gas']])


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        cars = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f'Парсинг страницы: {page} из {pages_count}...')
            html = get_html(URL, params={'page': page})
            cars.extend(get_content(html.text))
        print(pages_count)
        print(cars)
        print(f'Получено {len(cars)} автомобилей')
        save_file(cars, FILE)
        # cars = get_content(html.text)
    else:
        print('Error')


parse()
