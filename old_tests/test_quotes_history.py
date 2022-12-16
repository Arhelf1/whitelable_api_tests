import allure
import pytest
from data_for_tests.quotes_history_test_data import *
from helpers.common import validate_schema, response_status


@allure.feature('White Label API: Quotes/GetHistory')
class TestQuotesGetHistory:

    @pytest.mark.parametrize("board", [('TQBR', 'SBER'), ('MCT', 'GOOG')])
    @pytest.mark.parametrize("time", ["Minute", "Hour", "Day", "Week", "Month", "Quarter"])
    @pytest.allure.BLOCKER
    def test_quotes_get_history_tqbr(self, app, board, time):
        quotes_history = app.post_request(url, get_body(board[0], board[1], time), headers=app.token())
        response_status(quotes_history, url)
        quotes_history_data = quotes_history.json()
        validate_schema(app, quotes_history_data, path_to_json)
        assert len(quotes_history_data) > 0, 'Quotes/GetHistory вернул пустой список данных.'
        # проверяем что количество возвращенных диктов равно CandleCount
        assert len(quotes_history_data) == CandleCount, 'Количество свечек не соответствует ожидаемому.'
        # проверяем что все поля в ответе не NULL
        assert app.models.quotes.validate_all(receive_field_list, quotes_history_data)

    @pytest.allure.BLOCKER
    def test_time_frame(self):
        pass
