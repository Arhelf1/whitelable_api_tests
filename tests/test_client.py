import allure
from data_for_tests.client import *
from jsonschema import validate

from helpers.get_data_build import update_test_case


@allure.feature('White Label API: Client/')
class TestClient:
    @allure.feature('Client/GetProductsStatuses')
    @allure.testcase("https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T93")
    @allure.story('Получение статусов продуктов клиента')
    @allure.description('В подготовительном шаге создаем пользователя с паспортом, добавляем ему продукт. Отправляем запрос на получение статуса. Проверяем Id продукта, название, валидацию')
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_products_statuses(self, app, setup_get_product_statuses, allure_env, base_env):
        response = app.post_request(url_get_client_products_statuses, data=setup_get_product_statuses['data'], headers=setup_get_product_statuses['header'])
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        with allure.step("Запрос на получение статуса продуктов клиента отправлен. Проверим Id, название продукта, валидацию"):
            assert response.json()[0]['ProductId'] == 126, f"Id продукта неверный, а {response.json()}"
            assert response.json()[0]['ProductName'] == "Дистанционный единый счет_WhiteLabel", f"Название продукта неверное, потому что {response.json()}"
            assert response.json()[0]['Status'] in statuses, f"Проверка что статус входит в список ожидаемых статусов"
            validate(response.json(), app.get_json_schema(path_to_products_statuses))
        update_test_case(update_get_products_statuses)
