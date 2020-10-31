from bs4 import BeautifulSoup
import requests


# Зберігаєм у винляді txt:
def save():
    with open('parse_info.txt', 'a') as file:
        file.write(f'{comp["title"]} -> Price:{comp["price"]} -> Link{comp["link"]}\n')
        file.write(f'\n')


# Означення ф-ції parse:
def parse():
    URL = 'https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.116 Safari/537.36 OPR/69.0.3686.95'
    }
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='offer-wrapper')
    comps = []

    for item in items:
        comps.append({
            'title': item.find('a', class_='marginright5 link linkWithHash detailsLink').get_text(strip=True),
            'price': item.find('p', class_='price').get_text(strip=True),
            'link': item.find('a', class_='marginright5 link linkWithHash detailsLink').get('href')
        })
        global comp
        for comp in comps:
            print(f'{comp["title"]} -> Price:{comp["price"]} -> Link{comp["link"]}')
            save()
            print('\n')


# Виклик ф-ції parse:
parse()
input("")
