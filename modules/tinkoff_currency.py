import requests
'''
В данном файле представлен класс, реализующий запрос в Тинькофф-банк для получения валюты с привязкой к рублю
метод create_symbols_list отпраляет запрос в Тинькофф-банк и  в ответ получает все связки с рублём, кроме него
'''
class Tinkoff_Currency:
    def __init__(self, base_url):
        self.base_url = base_url
    def create_currency_list(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            list_currency = []
            for cur in response.json():
                if (not cur['currency']['name'] == 'RUB'):
                    currency = cur['currency']['name']
                    list_currency.append({"method": "Тинькофф", "currency": currency})
            return list_currency

base_url = 'https://acdn.tinkoff.ru/mp-resources/currencies.json'
get_tinkoff_currency = Tinkoff_Currency(base_url=base_url)

