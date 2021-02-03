import time
import requests
from bs4 import BeautifulSoup


class Currency:
    DORAR_UAH = 'https://www.google.com.ua/search?client=opera&sxsrf=ALeKk02hD2NHtyQ1mRAiEpmOekZ' \
                'AfHgDeg%3A1596919614864&source=hp&ei=Pg8vX8iUMsr9rgSJ6ISoBA&q=usd+to+uah&oq=&gs_lcp=' \
                'CgZwc3ktYWIQARgBMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgc' \
                'IIxDqAhAnMgcILhDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnUABYAGDwGGgBcAB4AIABAIgBAJIBAJgBAKoBB2d3cy13a' \
                'XqwAQo&sclient=psy-ab'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 OPR/69.0.3686.95'}

    old_converted_price = 27.72
    difference = 0.9

    def __int__(self):
        self.old_converted_price = float(self.old_converted_price)

    def get_currency_price(self):
        full_page = requests.get(self.DORAR_UAH, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "SwHCTb", "data-precision": 2})
        return convert[0].text

    def check_currency(self):
        currenc = float(self.get_currency_price().replace(",", "."))
        if currenc >= self.old_converted_price + self.difference:
            print("\nКурс сильно виріс. Пора щось міняти...")
        elif currenc <= self.old_converted_price - self.difference:
            print("\nКурс сильно впав. Пора щось міняти...")
        print('Зараз 1 долар = ' + str(currenc) + ' грн.')
        time.sleep(1)
        self.check_currency()


currency = Currency()
currency.check_currency()
