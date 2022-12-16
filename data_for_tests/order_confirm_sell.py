url = 'Order/ConfirmSell'
path_to_json = 'json_schemes/order_confirm_sell.json'
path_to_json_sms = 'json_schemes/no_sms.json'


# get body for post request
def get_body(code=0, document_id=0, order_id=0, user_id='10BA465C-D6AE-4EFD-9F6D-8F7927A35237'):
    return {"Code": code,
            "UserId": user_id,
            "DocumentId": document_id,
            "OrderId": order_id
            }
