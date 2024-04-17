import requests


class BinanceAPI:
    def __init__(self, api_key, secret_key):
        self.base_url = "https://api.binance.com/api/v3"
        self.api_key = api_key
        self.secret_key = secret_key

    def get_all_tickers(self):
        endpoint = "/ticker/24hr"
        response = requests.get(f"{self.base_url}{endpoint}")
        return response.json()

    def get_ticker(self, symbol):
        endpoint = "/ticker/24hr"
        params = {"symbol": symbol}
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        return response.json()

    def get_all_prices(self):
        endpoint = "/ticker/price"
        response = requests.get(f"{self.base_url}{endpoint}")
        return response.json()

    def get_price(self, symbol):
        endpoint = "/ticker/price"
        params = {"symbol": symbol}
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        return response.json()

    def get_all_volumes(self):
        endpoint = "/ticker/volume"
        response = requests.get(f"{self.base_url}{endpoint}")
        return response.json()

    def get_volume(self, symbol):
        endpoint = "/ticker/volume"
        params = {"symbol": symbol}
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        return response.json()

