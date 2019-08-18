import requests


class DataAggregator(object):
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def get(self, url):
        response = requests.get(url=(self.endpoint + url))
        response.raise_for_status()
        return response.json()

    def buy(self, account, product, quantity):
        return self.get("/buy/{}/{}/{}".format(account, product, quantity))
