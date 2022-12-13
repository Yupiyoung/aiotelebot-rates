import requests

'''
В данном файле представлен клсасс, реализующий запрос на Binance https://p2p.binance.com/ru/trade/ для получения курсов с криптовалюты к Рублю
Также в этом фалйе предсталены команды для введения в бота, для реалицации метода create_rate_list
'''
class Binance_P2P:
    header = {
        'authority': 'p2p.binance.com',
        'accept': '*/*',
        'c2ctype': 'c2c_merchant',
        'clienttype': 'web',
        'content-type': 'application/json',
        'lang': 'ru',
        'origin': 'https://p2p.binance.com',
        'referer': 'https://p2p.binance.com/ru/trade/all-payments/USDT?fiat=RUB',
        'user-agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    }
    def __init__(self, base_url):
        self.base_url = base_url
    def create_rate_list(self, message):
        for cur in p2p_command_list:
            if (cur['name'] == message):
                buy_json_data = {
                    'proMerchantAds': False,
                    'page': 1,
                    'rows': 10,
                    'payTypes': [
                        cur['bank'],
                    ],
                    'countries': [],
                    'publisherType': None,
                    'asset': cur['currency'],
                    'fiat': 'RUB',
                    'tradeType': 'BUY',
                }
                sell_json_data = {
                    'proMerchantAds': False,
                    'page': 1,
                    'rows': 10,
                    'payTypes': [
                         cur['bank'],
                    ],
                    'countries': [],
                    'publisherType': None,
                    'asset': cur['currency'],
                    'fiat': 'RUB',
                    'tradeType': 'SELL',
                }
                buy = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',headers=self.header, json=buy_json_data)
                sell = requests.post(
                    'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=self.header, json=sell_json_data)
                if buy.status_code == 200 and sell.status_code == 200:
                    buy = buy.json()
                    sell = sell.json()
                    if (len(sell['data']) > 0 or len(buy['data']) > 0):
                        sell = sell['data'][0]['adv']['price']
                        buy = buy['data'][0]['adv']['price']
                        return (f'Binance P2P {cur["name"]} \nПокупка: {buy}₽  | Продажа: {sell}₽')
                    elif (len(sell['data']) < 0 or len(buy()['data']) > 0):
                        buy = buy['data'][0]['adv']['price']
                        return (f'Binance P2P {cur["name"]} \nПокупка: {buy}₽  | Продажа: Нет Объявлений')
                    elif (len(sell['data']) > 0 or len(buy['data']) < 0):
                        sell = sell['data'][0]['adv']['price']
                        return (f'Binance P2P {cur["name"]} \nПокупка: Нет Объявлений  | Продажа: {sell}₽')
                    elif (len(sell['data']) < 0 or len(buy['data']) < 0):
                        return (f' {cur["name"]} Нет Объявлений ')
base_url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
get_p2p_rate = Binance_P2P(base_url=base_url)
p2p_command_list = [{'name': 'Сбербанк USDT', 'currency': 'USDT', 'bank': 'RosBankNew'}, {'name': 'Сбербанк BUSD', 'currency': 'BUSD', 'bank': 'RosBankNew'}, {'name': 'Сбербанк BTC', 'currency': 'BTC', 'bank': 'RosBankNew'},  {'name': 'Сбербанк BNB', 'currency': 'BNB', 'bank': 'RosBankNew'}, {'name': 'Сбербанк RUB', 'currency': 'RUB', 'bank': 'RosBankNew'}, {'name': 'Сбербанк ETH', 'currency': 'ETH', 'bank': 'RosBankNew'}, {'name': 'Сбербанк SHIB', 'currency': 'SHIB', 'bank': 'RosBankNew'}, {'name': 'Тинькофф USDT', 'currency': 'USDT', 'bank': 'TinkoffNew'}, {'name': 'Тинькофф BUSD', 'currency': 'BUSD', 'bank': 'TinkoffNew'}, {'name': 'Тинькофф BTC', 'currency': 'BTC', 'bank': 'TinkoffNew'},  {'name': 'Тинькофф BNB', 'currency': 'BNB', 'bank': 'TinkoffNew'}, {'name': 'Тинькофф RUB', 'currency': 'RUB', 'bank': 'TinkoffNew'}, {'name': 'Тинькофф ETH', 'currency': 'ETH', 'bank': 'TinkoffNew'}, {'name': 'Тинькофф SHIB', 'currency': 'SHIB', 'bank': 'TinkoffNew'}, {'name': 'Райффайзен банк USDT', 'currency': 'USDT', 'bank': 'RaiffeisenBank'}, {'name': 'Райффайзен банк BUSD', 'currency': 'BUSD', 'bank': 'RaiffeisenBank'}, {'name': 'Райффайзен банк BTC', 'currency': 'BTC', 'bank': 'RaiffeisenBank'},  {'name': 'Райффайзен банк BNB', 'currency': 'BNB', 'bank': 'RaiffeisenBank'}, {'name': 'Райффайзен банк RUB', 'currency': 'RUB', 'bank': 'RaiffeisenBank'}, {'name': 'Райффайзен банк ETH', 'currency': 'ETH', 'bank': 'RaiffeisenBank'}, {'name': 'Райффайзен банк SHIB', 'currency': 'SHIB', 'bank': 'RaiffeisenBank'}]

