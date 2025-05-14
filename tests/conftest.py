import pytest

from generators import generate_create_courier_body, generate_order_body
from methods.courier_methods import CourierMethods


@pytest.fixture
def generate_courier_data():
    courier_body = generate_create_courier_body()
    login = courier_body["login"]
    password = courier_body["password"]
    firstname = courier_body["firstName"]
    yield [courier_body, login, password, firstname]
    courier_id = CourierMethods.get_id_courier(login, password)
    CourierMethods.delete_courier(courier_id)
