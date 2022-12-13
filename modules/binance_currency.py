import requests
'''
В данном файле представлен клсасс, реализующий запрос на Binance API для получения криптовалюты с привязкой к USDT
метод create_symbols_list отпраляет запрос на Binance Api и  в ответ получает все связки с USDT
'''
class Binance_Currency:
    def __init__(self, base_url, endpoint, filter):
        self.base_url = base_url
        self.endpoint = endpoint
        self.filter = filter
    def create_symbols_list(self):
        response = requests.get(self.base_url + self.endpoint)
        if response.status_code == 200:
            response = response.json()
            curr_arr = []
            pairs_data = response['symbols']
            full_data_dic = {s['symbol']: s for s in pairs_data if filter in s['symbol']}
            for i in full_data_dic.keys():
                curr_arr.append(i.replace(self.filter, ''))
            return curr_arr
base_url = 'https://api.binance.com'
endpoint = '/api/v3/exchangeInfo'
filter = 'USDT'
get_binance_currency = Binance_Currency(base_url=base_url, endpoint=endpoint, filter=filter)
