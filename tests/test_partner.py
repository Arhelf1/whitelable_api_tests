import allure
from data_for_tests.partner import *
from helpers.get_data_build import update_test_case
from sql.query import *
import json
import ast
from jsonschema import validate


@allure.feature('White Label API: Partner/')
class TestPartner:
    @allure.testcase("https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T99")
    @allure.feature('Partner/AvailableProducts')
    @allure.story('Получение списка доступных продуктов')
    @allure.description('Получаем список доступных продуктов по PartnerId и сравниваем результат с БД')
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_products(self, app, db_cursor, allure_env, base_env, get_access_token):
        response = app.get_request(url_get_products, headers=get_access_token)
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        db_cursor['db_cursor'].execute(select_products_of_partner)
        json_string = json.dumps(db_cursor['db_cursor'].fetchall())
        json_string.encode()
        result_string = json_string.encode().decode("unicode-escape")
        result_string = ast.literal_eval(result_string)
        with allure.step("Запрос отправлен, сравним ответ с данными из БД"):
            assert response.json() == result_string, f"Продукт и Партнер не найдены"
        with allure.step("Запрос отправлен. Проверим валидацию ответа"):
            validate(response.json(), app.get_json_schema(path_to_get_products))
        update_test_case(update_get_products)
