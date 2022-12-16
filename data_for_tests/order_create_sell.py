url = 'Order/CreateSell'
path_to_json = 'json_schemes/order_create_sell.json'
path_to_low_price = 'json_schemes/order_low_price.json'
path_to_price_changed = 'json_schemes/order_price_changed.json'

error_message_lot = "Размер лота указан неверно. Убедитесь, что он больше нуля и кратен 10"


# get body for post request
def get_body(board, tiker, price=200, user_id='10BA465C-D6AE-4EFD-9F6D-8F7927A35237', lot=10,
             number='40702810638050013199', bank='наименование банка', bik='044525225', first_name='Артур',
             last_name='Хачатрян', middle_name='Варданович', phone='+79036122221'):
    return {"userId": user_id,
            "SecurityBoard": board,
            "SecurityCode": tiker,
            "price": price,
            "lot": lot,
            "Account": {
                "Number": number,
                "Bank": bank,
                "Bik": bik
            },
            "firstName": first_name,
            "lastName": last_name,
            "middleName": middle_name,
            "phone": phone
            }
