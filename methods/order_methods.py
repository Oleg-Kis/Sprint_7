import requests

from urls import Url


class OrderMethods:
    @staticmethod
    def create_order(body, color):
        body = body['color'].append(color)
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_ORDER}', json = body)
        return response
    @staticmethod
    def order_list():
        response = requests.get(f'{Url.BASE_URL}{Url.LIST_ORDERS}')
        return response
