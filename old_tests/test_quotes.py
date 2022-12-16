import allure
import pytest
import requests
from data_for_tests.quotes_test_data import *
from helpers.common import validate_schema, response_status


@allure.feature('White Label API: Quotes')
class TestQuotes:
    @pytest.allure.BLOCKER
    def test_quotes(self, app):
        quotes = app.get_request(url, app.token())
        response_status(quotes, url)
        quotes_data = quotes.json()
        assert len(quotes_data) > 0, 'Quotes вернул пустой список данных.'
        # проверяем что приходят только разрешенные партнеру тикеры
        assert app.models.quotes.validate_quotes(security_code, partners_approve_quotes, quotes_data)

    @pytest.allure.BLOCKER
    def test_exchanges(self, app):
        quotes = app.get_request(url, app.token())
        assert quotes.status_code == requests.codes.ok
        quotes_data = quotes.json()
        assert len(quotes_data) > 0, 'Quotes вернул пустой список данных.'
        # проверяем что приходят только разрешенные партнеру биржи
        assert app.models.quotes.validate_exchanges(security_board, partners_approve_exchanges, quotes_data)

    @pytest.allure.BLOCKER
    def test_title(self, app):
        quotes = app.get_request(url, app.token())
        assert quotes.status_code == requests.codes.ok
        quotes_data = quotes.json()
        assert len(quotes_data) > 0, 'Quotes вернул пустой список данных.'
        # проверяем что приходят только разрешенные партнеру биржи
        assert app.models.quotes.validate_title(tiker_title, quotes_data)

    @pytest.allure.BLOCKER
    def test_quotes_larger(self, app):
        quotes = app.get_request(url, app.token())
        assert quotes.status_code == requests.codes.ok
        quotes_data = quotes.json()
        assert len(quotes_data) > 0, 'Quotes вернул пустой список данных.'
        # проверяем что пришло нужное количество котировок
        # если пришло меньше, выводим отсутствующие и падаем с ошибкой
        assert app.models.quotes.validate_quotes_larger(partners_approve_quotes, quotes_data)

    @pytest.allure.BLOCKER
    def test_lot_size(self, app):
        quotes = app.get_request(url, app.token())
        assert quotes.status_code == requests.codes.ok
        quotes_data = quotes.json()
        assert len(quotes_data) > 0, 'Quotes вернул пустой список данных.'
        # проверяем что lotSize > 0
        assert app.models.quotes.validate('lotSize', quotes_data)

    @pytest.allure.BLOCKER
    def test_ask(self, app):
        quotes = app.get_request(url, app.token())
        assert quotes.status_code == requests.codes.ok
        quotes_data = quotes.json()
        assert len(quotes_data) > 0, 'Quotes вернул пустой список данных.'
        # проверяем что ask not 0
        assert app.models.quotes.validate('ask', quotes_data)

    @pytest.allure.BLOCKER
    def test_bid(self, app):
        quotes = app.get_request(url, app.token())
        assert quotes.status_code == requests.codes.ok
        quotes_data = quotes.json()
        assert len(quotes_data) > 0, 'Quotes вернул пустой список данных.'
        # проверяем что bid not 0
        assert app.models.quotes.validate('bid', quotes_data)

    @pytest.allure.BLOCKER
    def test_interval(self, app):
        quotes = app.get_request(url, app.token())
        assert quotes.status_code == requests.codes.ok
        quotes_data = quotes.json()
        assert len(quotes_data) > 0, 'Quotes вернул пустой список данных.'
        # проверяем что ask лежит в диапазоне значений за год
        assert app.models.quotes.validate_interval(quotes_list, interval_list, quotes_data)

    @pytest.allure.BLOCKER
    def test_doubles(self, app):
        quotes = app.get_request(url, app.token())
        assert quotes.status_code == requests.codes.ok
        quotes_data = quotes.json()
        validate_schema(app, quotes_data, path_to_json)
        assert len(quotes_data) > 0, 'Quotes вернул пустой список данных.'
        # проверяем поля securityCode, securityBoard, title на дубли
        assert app.models.quotes.validate_doubles(doubles_fields_list, quotes_data)
