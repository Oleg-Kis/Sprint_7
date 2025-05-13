import requests

from data import Url


class CourierMethods:
    @staticmethod
    def create_courier(body):
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json = body)
        return response

    @staticmethod
    def create_courier_without_name(body):
        login = (body[1])
        password = (body[2])
        params = {"login": login, "password": password}
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', params = params)
        return response

    @staticmethod
    def get_id_courier(login, password):
        params = {'login': login, 'password': password}
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER}', data = params)
        return response.json()['id']

    @staticmethod
    def login_courier(body):
        login = (body[1])
        password = (body[2])
        params = {'login': login, 'password': password}
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER}', data = params)
        return response

    @staticmethod
    def login_courier_without_password(body):
        login = (body[1])
        params = {'login': login, 'password': ''}
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER}', data=params)
        return response

    @staticmethod
    def login_courier_incorrect_password(body):
        login = (body[1])
        password = (body[2])
        params = {'login': login, 'password': password + 'a'}
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER}', data=params)
        return response

    @staticmethod
    def delete_courier(courier_id):
        params = {'id': courier_id}
        return requests.delete(f'{Url.BASE_URL}{Url.DELETE_COURIER}', params = params)
