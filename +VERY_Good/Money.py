import time
import requests
from bs4 import BeautifulSoup

class Currency:
    DORAR_UAH = 'https://www.google.com.ua/search?client=opera&sxsrf=ALeKk02hD2NHtyQ1mRAiEpmOekZAfHgDeg%3A1596919614864&source=hp&ei=Pg8vX8iUMsr9rgSJ6ISoBA&q=usd+to+uah&oq=&gs_lcp=CgZwc3ktYWIQARgBMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcILhDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnUABYAGDwGGgBcAB4AIABAIgBAJIBAJgBAKoBB2d3cy13aXqwAQo&sclient=psy-ab'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 OPR/69.0.3686.95'}

    current_converted_priece = 27.72
    diference = 1

    def __int__(self):
        self.current_converted_priece = float(self.current_converted_priece)

    def get_currency_price (self):
        full_page = requests.get(self.DORAR_UAH, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text

    def check_currency(self):
        currency = float(self.get_currency_price().replace(",","."))
        if currency >= self.current_converted_priece + self.diference:
            print("Курс сильно виріс. Пора щось міняти...")
        elif currency <= self.current_converted_priece - self.diference:
            print("Курс сильно впав. Пора щось міняти...")
        print ('Зараз 1 долар = '+ str(currency) +' грн.')
        time.sleep(5)
        self.check_currency()

currency = Currency()
currency.check_currency()
