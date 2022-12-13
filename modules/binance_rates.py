import requests
'''
В данном файле представлен класс, реализующий запрос на Binance API для получения курса криптовалют с привязкой к USDT
метод create_rate_list принимает в себя аргумент, который является выбранной криптовалютой, и отправляет запрос на Binance Api, и в ответ получает курс для покупки выбранной криптовалюты
'''
class Binance_Rate:
    def __init__(self, base_url, filter, endpoint):
        self.base_url = base_url
        self.filter = filter
        self.endpoint = endpoint
    def create_rate_list(self, crypto):
        response = requests.get(self.base_url + self.endpoint + crypto + self.filter)
        if response.status_code == 200:
            response = response.json()
            return (f"{response['symbol']} | {response['price']}{self.filter}")
base_url = 'https://api.binance.com'
filter = "USDT"
endpoint = (f'/api/v3/ticker/price?symbol=')
get_binance_rate = Binance_Rate(base_url=base_url, filter=filter,endpoint=endpoint )

