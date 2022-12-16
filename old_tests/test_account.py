import allure
import pytest
from data_for_tests.account import *
from data_for_tests.quotes_test_data import security_settings_approve_quotes, partners_approve_exchanges
from helpers.common import validate_schema, response_status


@allure.feature('White Label API: Account/')
class TestAccount:
    @pytest.allure.BLOCKER
    def test_account_get_securities(self, app):
        portfolio = app.get_request(url_get_securities + user_id, app.token())
        response_status(portfolio, url_get_securities)
        portfolio_data = portfolio.json()
        assert len(portfolio_data) > 0, 'Метод Account/GetSecurities вернул пустой список данных'
        validate_schema(app, portfolio_data, path_to_get_securities_json)
        assert app.models.quotes.validate_quotes('code', approved_quotes, portfolio_data)
        assert app.models.quotes.validate_exchanges('board', approved_exchanges, portfolio_data)
        assert portfolio_data[0]['total'] > 0, 'У клиента нет денег'

    @pytest.allure.BLOCKER
    def test_account_security_settings(self, app):
        instruments = app.get_request(url_security_settings, app.token())
        instruments_data = instruments.json()
        response_status(instruments, url_security_settings)
        assert len(instruments_data) > 0, 'Метод Order/CreateSell вернул пустой список котировок'
        validate_schema(app, instruments_data, path_to_security_settings_json)
        # проверяем что приходят только разрешенные партнеру тикеры
        assert app.models.quotes.validate_quotes(tiker_id, security_settings_approve_quotes, instruments_data)
        # проверяем что приходят только разрешенные партнеру биржи
        assert app.models.quotes.validate_exchanges(board_id, partners_approve_exchanges, instruments_data)
