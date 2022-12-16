url = 'Order/Buy'
path_to_json = 'json_schemes/order_buy.json'
path_to_low_price = 'json_schemes/low_price.json'

# user data
user_data = []
tmp = ['Хачатрян', 'Артур', 'Варданович', '+79036122221', 10.0]


# get body for post request
def get_body(board, tiker, price, user_id='10BA465C-D6AE-4EFD-9F6D-8F7927A35237', lot=10,
             transaction_id='12346789', first_name='Артур',
             last_name='Хачатрян', middle_name='Варданович', phone='+79036122221'):
    return {"userId": user_id,
            "SecurityBoard": board,
            "SecurityCode": tiker,
            "price": price,
            "lot": lot,
            "TransactionId": transaction_id,
            "firstName": first_name,
            "lastName": last_name,
            "middleName": middle_name,
            "phone": phone
            }
