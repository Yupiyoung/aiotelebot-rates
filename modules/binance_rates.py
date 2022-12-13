import requests
#Класс, реализующий запрос на Binance Api для получения курсов с привязкой к USDT
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

