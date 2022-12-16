import allure
import pytest
import requests
from jsonschema import validate
from data_for_tests.order_buy import *
from helpers.common import get_actual_qoute_price, response_status


@allure.feature('White Label API: Qrder/Buy')
class TestOrderBuy:

    @pytest.mark.parametrize("board", [('TQBR', 'SBER'), ('MCT', 'GOOG')])
    @pytest.allure.BLOCKER
    def test_order_buy_tqbr(self, app, board):
        price = get_actual_qoute_price(board[0], app)
        order_buy = app.post_request(url, get_body(board[0], board[1], price), headers=app.token())
        response_status(order_buy, url)
        order_buy_data = order_buy.json()
        validate(order_buy_data, app.get_json_schema(path_to_json))
        assert len(order_buy_data) > 0, 'Метод Order/Buy вернул пустой список данных.'
        assert app.models.order_buy.validate_after_operation(order_buy_data['orderId'], price)

    @pytest.mark.parametrize("board", [('TQBR', 'SBER', 50.03), ('MCT', 'GOOG', 50.03)])
    @pytest.allure.BLOCKER
    def test_tqbr_low_price(self, app, board):
        order_buy = app.post_request(url, get_body(board[0], board[1], board[2]), headers=app.token())
        assert order_buy.status_code == requests.codes.method_not_allowed
        order_buy_data = order_buy.json()
        validate(order_buy_data, app.get_json_schema(path_to_low_price))
        assert len(order_buy_data) > 0, 'Метод Order/Buy вернул пустой список данных.'
        assert order_buy_data['message'] == 'Цены изменились'
        assert order_buy_data['code'] == 20
