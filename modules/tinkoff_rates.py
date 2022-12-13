import requests
'''
В данном файле представлен класс, реализующий запрос в Тинькофф-банк для получения курса криптовалют с привязкой к рублю
метод create_rate_list принимает в себя аргумент, который является выбранной валютой, и отправляет запрос в Тинькофф-банк, и в ответ получает курс для покупки выбранной валюты
'''
class Tinkoff_Rate:
    def __init__(self, base_url):
        self.base_url = base_url
    def create_rate_list(self, currency):
        response = requests.get(self.base_url + currency +  '&to=RUB')
        if response.status_code == 200:
            buy = response.json()['payload']['rates'][1]['buy']
            sell = response.json()['payload']['rates'][1]['sell']
            return (f'Тинькофф {currency} \nПокупка: {buy}  | Продажа: {sell}')
base_url = 'https://api.tinkoff.ru/v1/currency_rates?from='
get_tinkoff_rate = Tinkoff_Rate(base_url=base_url)

