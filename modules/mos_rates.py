import  requests
from datetime import datetime
import json

'''
В данном файле реализован класс, который выводит курс валют, основываясь на данных МосБиржи 
'''
class Mos_Rate:
    def __init__(self, base_url, currency):
        self.base_url = base_url
        self.currency = currency
    def create_rate_list(self):
        response = requests.get(self.base_url)
        response = response.text
        response = response[14:]
        response = response[:-1]
        response = json.loads(response)
        if (not response[1]['history']):
            return ('На данный момент нет актуального курса')
        else:
            response = response[1]['history'][0]['CLOSE']
            if (response > 0):
                return (f'МосБиржа {self.currency} \nПокупка: {response}₽')
            elif (response <= 0):
                return (f'По данной валюте катировок на сегодня нет')
date = f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day - 1}'
currency_usd='USD'
mos_usd =  (f'https://iss.moex.com/iss/history/engines/currency/markets/selt/boards/CETS/securities/USD000000TOD.jsonp?iss.meta=off&iss.json=extended&callback=JSON_CALLBACK&lang=ru&from={date}')
get_mos_usd = Mos_Rate(base_url=mos_usd, currency=currency_usd)
currency_eur='EUR'
mos_eur =  (f'https://iss.moex.com/iss/history/engines/currency/markets/selt/boards/CETS/securities/EUR_RUB__TOD.jsonp?iss.meta=off&iss.json=extended&callback=JSON_CALLBACK&lang=ru&from={date}')
get_mos_eur = Mos_Rate(base_url=mos_eur, currency=currency_eur)
currency_cny='CNY'
mos_cny =  (f'https://iss.moex.com/iss/history/engines/currency/markets/selt/boards/CETS/securities/CNY000000TOD.jsonp?iss.meta=off&iss.json=extended&callback=JSON_CALLBACK&lang=ru&from={date}')
get_mos_cny = Mos_Rate(base_url=mos_cny, currency=currency_cny)
currency_byn='BYN'
mos_byn =  (f'https://iss.moex.com/iss/history/engines/currency/markets/selt/boards/CETS/securities/BYNRUB_TOD.jsonp?iss.meta=off&iss.json=extended&callback=JSON_CALLBACK&lang=ru&from={date}')
get_mos_byn = Mos_Rate(base_url=mos_byn, currency=currency_byn)
currency_try='TRY'
mos_try=(f'https://iss.moex.com/iss/history/engines/currency/markets/selt/boards/CETS/securities/TRYRUB_TOD.jsonp?iss.meta=off&iss.json=extended&callback=JSON_CALLBACK&lang=ru&from={date}')
get_mos_try = Mos_Rate(base_url=mos_try, currency=currency_try)
mos_command_list = [{'name': 'МосБиржа USD'}, {'name': 'МосБиржа EUR'}, {'name': 'МосБиржа TRY'},  {'name': 'МосБиржа CNY'},  {'name': 'МосБиржа BYN'}]

