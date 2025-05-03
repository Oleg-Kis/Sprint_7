import data


def modify_create_order_body(key,value):
    body_order = data.DataForOrder.CREATE_ORDER_BODY.copy()
    body_order[key]=value
    return body_order

def modify_create_courier_body(key, value):
    body_courier = data.DataForCourier.CREATE_COURIER_BODY.copy()
    body_courier[key]=value
    return body_courier
