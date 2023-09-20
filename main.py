import requests
from bs4 import BeautifulSoup as bs

# Отправляем GET-запрос
URL_TEMPLATE = 'https://www.noob-club.ru/'
r = requests.get(URL_TEMPLATE)

#Проверяем доступность сайта
#print(r.status_code)

# Создаем объект Beautiful Soup для парсинга HTML
soup = bs(r.text, "html.parser")

#Заголовок
title = soup.title.text
print(title)

#Текст из тега
tag_text = soup.find_all('span', class_='entry-header')
for text in tag_text:
    print(text.text)