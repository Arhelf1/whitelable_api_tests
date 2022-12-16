import allure
import pytest
import requests
from jsonschema import validate
from data_for_tests.order_confirm_sell import *
from data_for_tests import order_create_sell as cs
from helpers.common import response_status


@allure.feature('White Label API: Order/ConfirmSell')
class TestOrderConfirmSell:

    @pytest.mark.parametrize("board", [('TQBR', 'SBER'), ('MCT', 'AAPL')])
    @pytest.allure.BLOCKER
    def test_confirm_sell(self, app, board):
        # тут вызвать Order/CreateSell и и спользовать его ответ (DocumentId, OrderId)
        order_sell = app.post_request(cs.url, cs.get_body(board[0], board[1]), headers=app.token())
        assert order_sell.status_code == requests.codes.ok
        order_sell_data = order_sell.json()
        assert len(order_sell_data) > 0, 'Создание заявки на продажу. CreateSell вернул пустой список данных.'
        # тут заполучить смс код надобно
        sms_code = app.models.order_confirm_sell.get_sms_code(str(order_sell_data['documentId']))
        # Order/ConfirmSell
        order_confirm_sell = app.post_request(url, get_body(sms_code, order_sell_data['documentId'], order_sell_data['orderId']), headers=app.token())
        response_status(order_confirm_sell, url)
        order_confirm_sell_data = order_confirm_sell.json()
        assert len(order_confirm_sell_data) > 0, 'Подтверждение заявки на продажу. ConfirmSell вернул пустой список данных.'
        # validate(order_confirm_sell_data, app.get_json_schema(path_to_json))
        assert order_confirm_sell_data['orderId'] == order_sell_data['orderId']

    @pytest.allure.BLOCKER
    def test_no_sms_code(self, app):
        no_sms = app.post_request(url, get_body(code=''), headers=app.token())
        # assert no_sms.status_code == requests.codes.bad_request
        no_sms_data = no_sms.json()
        assert len(no_sms_data) > 0, 'Метод ConfirmSell вернул пустой список данных.'
        # разобраться с валидацией схем
        validate(no_sms_data, app.get_json_schema(path_to_json_sms))
        assert no_sms_data['modelState']['request.Code'][0] == "Код полученный из СМС обязателен для заполнения"
