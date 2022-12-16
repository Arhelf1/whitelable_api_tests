import allure
import pytest
import requests
from jsonschema import validate
from sql.query import check_sms
from data_for_tests.order_create_sell import *
from helpers.common import get_actual_qoute_price, response_status


@allure.feature('White Label API: Order/CreateSell')
class TestOrderCreateSell:

    @pytest.mark.parametrize("board", [('TQBR', 'SBER'), ('MCT', 'GOOG')])
    @pytest.allure.BLOCKER
    def test_create_sell_tqrb(self, app, board):
        price = get_actual_qoute_price(board[0], app)
        order_sell = app.post_request(url, get_body(board[0], board[1], price), headers=app.token())
        response_status(order_sell, url)
        order_sell_data = order_sell.json()
        validate(order_sell_data, app.get_json_schema(path_to_json))
        assert len(order_sell_data) > 0, 'Order/CreateSell вернул пустой список данных.'
        assert app.models.order_buy.validate_after_operation(order_sell_data['orderId'], price)
        assert app.models.order_create_sell.validate_sms(check_sms, str(order_sell_data['documentId']))

    @pytest.mark.parametrize("board", ["TQBR"])
    @pytest.mark.parametrize("tiker", ["SBER"])
    @pytest.mark.parametrize("lot", [0])
    @pytest.allure.BLOCKER
    def test_lot_less_zero(self, app, board, tiker, lot):
        price = get_actual_qoute_price(board, app)
        order_sell = app.post_request(url, get_body(board, tiker, price=price, lot=lot), headers=app.token())
        assert order_sell.status_code == requests.codes.method_not_allowed
        order_sell_data = order_sell.json()
        validate(order_sell_data, app.get_json_schema(path_to_low_price))
        assert len(order_sell_data) > 0, 'Order/CreateSell вернул пустой список данных.'
        if order_sell_data['message'] != error_message_lot:
            raise AssertionError(order_sell_data['message'] + ' | ERROR : Лот должен быть больше нуля и кратен 10 |')
        assert order_sell_data['code'] == 23

    @pytest.mark.parametrize("board", ["TQBR"])
    @pytest.mark.parametrize("tiker", ["SBER"])
    @pytest.mark.parametrize("price", [0])
    @pytest.allure.BLOCKER
    def test_price_changed(self, app, board, tiker, price):
        order_sell = app.post_request(url, get_body(board, tiker, price=price), headers=app.token())
        assert order_sell.status_code == requests.codes.method_not_allowed
        order_sell_data = order_sell.json()
        validate(order_sell_data, app.get_json_schema(path_to_low_price))
        assert len(order_sell_data) > 0, 'Order/CreateSell вернул пустой список данных.'
        assert order_sell_data['message'] == "Цены изменились"
        assert order_sell_data['code'] == 20
