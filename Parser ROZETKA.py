import requests
from bs4 import BeautifulSoup

URL = "https://rozetka.com.ua/notebooks/c80004/producer=asus/"
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'accept': '*/*'
}


def get_html(url, params=None):
    r = requests.get(url, headers=None, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='proposition')
    cars = []


def pars():
    html = get_html(URL)


pars()
