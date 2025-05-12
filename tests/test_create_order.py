import allure
import pytest

from methods.order_methods import OrderMethods


class TestOrders:
    @allure.title("Создание заказа")
    @allure.description("Создание заказов со всеми варантами цветов")
    @pytest.mark.parametrize('color', ['', 'BLACK', 'GREY', 'BLACK, GREY'])
    def test_create_all_color_options(self, generate_order, color):
        order = OrderMethods.create_order(generate_order, color)
        assert order.status_code == 201 and type(order.json()['track']) == int

    @allure.title("Получить список заказов")
    def test_list_orders(self):
        order_list = OrderMethods.order_list()
        assert order_list.status_code == 200 and  type(order_list.json()["orders"]) == list
