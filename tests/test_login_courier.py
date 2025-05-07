from data import MessageAnswer
from methods.courier_methods import CourierMethods


class TestLoginCourier:
    def test_login_courier_valid_data(self, generate_courier_data):
        courier = CourierMethods.create_courier(generate_courier_data[0])
        courier_id = CourierMethods.login_courier(generate_courier_data)
        assert courier.status_code == 201
        assert courier_id.status_code == 200 and type(courier_id.json()['id']) == int

    def test_login_courier_without_password(self, generate_courier_data):
        courier = CourierMethods.create_courier(generate_courier_data[0])
        courier_log_in = CourierMethods.login_courier_without_password(generate_courier_data)
        assert courier.status_code == 201
        assert courier_log_in.status_code == 400 and courier_log_in.json()["message"] == MessageAnswer.ERR_WITHOUT_PASS
