import requests
class CB_Currency:
    def __init__(self, base_url):
        self.base_url = base_url
    def create_currency_list(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            if (response.json()['Valute']):
                cur_arr = []
                res = response.json()['Valute']
                for cur in res:
                    cur_arr.append('ЦБ ' + cur)
                return cur_arr
base_url = 'https://www.cbr-xml-daily.ru/daily_json.js'
get_cb_currency = CB_Currency(base_url=base_url)

