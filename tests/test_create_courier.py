from data import MessageAnswer
from methods.courier_methods import CourierMethods


class TestCreateCourier:
    def test_create_courier_all_valid_data(self, generate_courier_data):
        courier = CourierMethods.create_courier(generate_courier_data[0])
        assert courier.status_code == 201 and courier.json() == MessageAnswer.OK_CREATE_COURIER

    def test_create_two_identical_couriers(self, generate_courier_data):
        courier_one = CourierMethods.create_courier(generate_courier_data[0])
        courier_two = CourierMethods.create_courier(generate_courier_data[0])
        assert courier_one.status_code == 201 and courier_two.status_code == 409

    def test_not_create_courier_without_name(self,generate_courier_data):
        courier = CourierMethods.create_courier_without_name(generate_courier_data)
        assert courier.status_code == 400 and courier.json()["message"] == MessageAnswer.ERR_WITHOUT_NAME
