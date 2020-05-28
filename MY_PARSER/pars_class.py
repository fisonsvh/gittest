import urllib.request

from bs4 import BeautifulSoup


class Parser:
    raw_html = ''
    html = ''
    results = []

    def __init__(self, URL, path):
        self.URL = URL
        self.path = path

    def get_html(self):
        req = urllib.request.urlopen(self.URL)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        news = self.html.find_all('li', class_='liga-news-item')
        for item in news:
            title = item.find('span', class_='d-block').get_text(strip='True')  # ПОИСК ЗАГОЛОВКОВ
            # print(title)
            desc = item.find('span', class_='name-dop').get_text(
                strip='True')  # ПОИСК ТЕКСТА (strip='True') УБИРАЕТ ПРОБЕЛЫ)
            # print(desc)
            href = item.a.get('href')  # ПОИСК ССЫЛОКa
            # print(href)
            self.results.append({  # НАПОЛНЕНИЕ СЛОВАРЯ
                'title': title,
                'decs': desc,
                'href': href
            })

    def save(self):
        f = open('news.txt', 'w', encoding='UTF-8')  # ОТКРЫТИЕ ФАЙЛА
        i = 1
        for item in self.results:
            f.write(
                f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["decs"]}\nСсылка: {item["href"]}\n\n***********************\n\n')  # ЗАПИСЬ В ФАЙЛ
            i += 1
        f.close()

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
