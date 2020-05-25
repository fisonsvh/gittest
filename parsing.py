import urllib.request

from bs4 import BeautifulSoup

req = urllib.request.urlopen('https://www.ua-football.com/sport?page=2')
html = req.read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('li', class_='liga-news-item')
# print(news)
results = []

for item in news:
    title = item.find('span', class_='d-block').get_text(strip='True')
    # print(title)
    desc = item.find('span', class_='name-dop').get_text(strip='True')
    # print(desc)
    href = item.a.get('href')
    # print(href)
    results.append({
        'title': title,
        'decs': desc,
        'href': href
    })

f = open('news.txt', 'w', encoding='UTF-8')
i = 1
for item in results:
    f.write(
        f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["decs"]}\nСсылка: {item["href"]}\n\n***********************\n\n')
    i += 1
f.close()
