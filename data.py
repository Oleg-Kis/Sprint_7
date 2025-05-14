class DataForOrder:
    CREATE_ORDER_BODY = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
    ]
    }

class DataForCourier:
    CREATE_COURIER_BODY = {
    "login": "ninjhfgfaaaa",
    "password": "1234",
    "firstName": "sasklgfcfge"
    }

class MessageAnswer:
    ERR_WITHOUT_NAME = "Недостаточно данных для создания учетной записи"
    OK_CREATE_COURIER = {'ok': True}
    ERR_WITHOUT_PASS = "Недостаточно данных для входа"
    ERR_INCORRECT_PASS = "Учетная запись не найдена"

class ColorScooter:
    COLOR = ['', 'BLACK', 'GREY', 'BLACK, GREY']
