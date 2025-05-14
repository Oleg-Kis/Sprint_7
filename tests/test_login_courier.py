import allure

from data import MessageAnswer
from methods.courier_methods import CourierMethods


class TestLoginCourier:
    @allure.title("Логин курьера с валидными данными")
    def test_login_courier_valid_data(self, generate_courier_data):
        with allure.step('Создаем курьера'):
            courier = CourierMethods.create_courier(generate_courier_data[0])
        with allure.step('Авторизация курьера'):
            courier_id = CourierMethods.login_courier(generate_courier_data)
        assert courier.status_code == 201
        assert courier_id.status_code == 200 and type(courier_id.json()['id']) == int

    @allure.title("Логин курьера без поля Пароль")
    def test_login_courier_without_password(self, generate_courier_data):
        with allure.step('Создаем курьера'):
            courier = CourierMethods.create_courier(generate_courier_data[0])
        with allure.step('Авторизация курьера без пароля'):
            courier_log_in = CourierMethods.login_courier_without_password(generate_courier_data)
        assert courier.status_code == 201
        assert courier_log_in.status_code == 400 and courier_log_in.json()["message"] == MessageAnswer.ERR_WITHOUT_PASS

    @allure.title("Логин курьера с неверным паролем")
    def test_login_incorrect_data(self, generate_courier_data):
        with allure.step('Создаем курьера'):
            courier = CourierMethods.create_courier(generate_courier_data[0])
        with allure.step('Авторизация курьера с неверным паролем'):
            courier_log = CourierMethods.login_courier_incorrect_password(generate_courier_data)
        assert courier.status_code == 201
        assert courier_log.status_code == 404 and courier_log.json()["message"] == MessageAnswer.ERR_INCORRECT_PASS
