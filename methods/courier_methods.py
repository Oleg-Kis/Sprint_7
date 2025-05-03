import requests

from data import Url, DataForCourier


class CourierMethods:
    @staticmethod
    def create_courier(body):
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=body)
        return response

    @staticmethod
    def create_courier_without_name(body):
        login = CourierMethods.create_courier(body[1])
        password = CourierMethods.create_courier(body[2])
        params = {"login": login, "password": password}
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', params=params)
        return response

    @staticmethod
    def get_id_courier(login, password):
        params = {'login': login, 'password': password}
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER}', params = params)
        return response.json

    @staticmethod
    def delete_courier(courier_id):
        params = {'id': courier_id}
        return requests.delete(f'{Url.BASE_URL}{Url.DELETE_COURIER}', params = params)
