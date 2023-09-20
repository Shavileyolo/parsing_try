import requests
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook

# Отправляем GET-запрос
URL_TEMPLATE = 'https://www.noob-club.ru/'
r = requests.get(URL_TEMPLATE)

#Проверяем доступность сайта
#print(r.status_code)

# Создаем объект Beautiful Soup для парсинга HTML
soup = bs(r.text, "html.parser")

#Заголовок
title = soup.title.text
#print(title)

#Текст из тега
tag_text = soup.find_all('span', class_='entry-header')
tags = []
for text in tag_text:
    tags.append(text.text)
    #print(text.text)


#Сохраняем результаты в файле
#Создание таблицы
wb = Workbook()
sheet = wb.active

#Запись в таблицу
for i, tag in enumerate(tags):
    sheet.cell(row = i+1, column = 1, value = tag)

#Сохраняем результаты
wb.save('test.xlsx')