import requests
from bs4 import BeautifulSoup


def save(ad):
    '''Сохраняет объявление'''
    with open('parse_info.txt', 'w') as file:
        file.write(
            f'Title: {ad["title"]} -> Price: {ad["price"]} -> Link: {ad["link"]}')


def parse(URL):
    '''Парсит определенную странцу пользователя'''
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }

    response = requests.get(URL, 'html.parse')
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('tr', class_='wrap')

    ad = {'title': items[5].find('a', class_='marginright5').get_text(),
          'price': items[5].find('p', class_='price').get_text(),
          'link': items[5].find('a', class_='marginright5').get('href')}

    save(ad)