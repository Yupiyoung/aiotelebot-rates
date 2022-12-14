import requests
'''
В данном файле представлен класс, реализующий запрос на https://www.cbr-xml-daily.ru/daily_json.js для получения курса валют
метод create_rate_list принимает в себя аргумент, который является выбранной валютой, отправляет запрос и фильтрует валюты, в конченом итоге он возвращает курс одной из валют
'''
class CB_Rate:
    def __init__(self, base_url):
        self.base_url = base_url
    def create_rate_list(self, currency):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            if (response.json()['Valute']):
                res = response.json()['Valute']
                str = ''
                currency = currency.replace("ЦБ ", "")
                for i in res:
                    str += i
                if (currency in str):
                    for i in res:
                        if (currency == i):
                            rates = res[i]
                            price = rates['Value'] / rates['Nominal']
                            return (f'Курс {i} по ЦБ РФ {price}')
base_url = 'https://www.cbr-xml-daily.ru/daily_json.js'
get_cb_rate = CB_Rate(base_url=base_url)
