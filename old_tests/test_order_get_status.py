import allure
import pytest
from jsonschema import validate
import requests
from data_for_tests.order_get_status import status_list, path_to_get_status, url as url_get_status
from data_for_tests.order_buy import *
from helpers.common import get_actual_qoute_price, response_status


@allure.feature('White Label API: Order/GetStatus')
class TestOrderGetStatus:

    @pytest.mark.parametrize("board", ["TQBR"])
    @pytest.mark.parametrize("tiker", ["SBER"])
    @pytest.allure.BLOCKER
    def test_get_status(self, board, tiker, app):

        # Создаем заявку на покупку
        price = get_actual_qoute_price(board, app)
        order_buy = app.post_request(url, get_body(board, tiker, price), headers=app.token())
        response_status(order_buy, url)
        order_buy_data = order_buy.json()
        assert len(order_buy_data) > 0, 'Order/Buy вернул пустой список данных.'

        # Пороверка статуса заявки
        quotes = app.get_request(url_get_status + str(order_buy_data['orderId']), app.token())
        response_status(quotes, url_get_status)
        quotes_data = quotes.json()
        validate(quotes_data, app.get_json_schema(path_to_get_status))
        assert len(quotes_data) > 0, 'Order/GetStatus вернул пустой список данных.'
        assert quotes_data['orderStatus'] in status_list
