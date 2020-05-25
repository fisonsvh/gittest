import urllib.request

from bs4 import BeautifulSoup

req = urllib.request.urlopen('https://www.ua-football.com/sport?page=2')  # ЗАПРОС СТРАНИЦЫ
html = req.read()  # ЧТЕНИЕ СТРАНИЦЫ

soup = BeautifulSoup(html, 'html.parser')  # ПРЕОБРАЗОВАНИЕ СТРАНИЦЫ В ЧИТАБЕЛЬНЫЙ ВИД
news = soup.find_all('li', class_='liga-news-item')  # ПОИСК БЛОКОВ ДЛЯ ПАРСИНГА
# print(news)
results = []  #СОЗДАНИЕ СПИСКА, КУДА БУДУТ СОХРАНЯТЬСЯ ДАННЫЕ

for item in news:
    title = item.find('span', class_='d-block').get_text(strip='True')  #ПОИСК ЗАГОЛОВКОВ
    # print(title)
    desc = item.find('span', class_='name-dop').get_text(strip='True')  #ПОИСК ТЕКСТА (strip='True') УБИРАЕТ ПРОБЕЛЫ)
    # print(desc)
    href = item.a.get('href')  #ПОИСК ССЫЛОК
    # print(href)
    results.append({  #НАПОЛНЕНИЕ СЛОВАРЯ
        'title': title,
        'decs': desc,
        'href': href
    })

f = open('news.txt', 'w', encoding='UTF-8')  #ОТКРЫТИЕ ФАЙЛА
i = 1
for item in results:
    f.write(
        f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["decs"]}\nСсылка: {item["href"]}\n\n***********************\n\n')  #ЗАПИСЬ В ФАЙЛ
    i += 1
f.close()
