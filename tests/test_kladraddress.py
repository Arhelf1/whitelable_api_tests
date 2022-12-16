import allure
from data_for_tests.kladraddress import *
from jsonschema import validate
from flaky import flaky
from helpers.get_data_build import update_test_case


@allure.feature('White Label API: KladdrAddress/')
class TestKladr:
    @allure.testcase("https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T96")
    @allure.feature('Fias/AvailableCountries')
    @allure.story('Справочник стран')
    @allure.title('Получаем список стран')
    @allure.description("Проверяем кол-во стран в справочнике и валидацию")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_get_country(self, app, allure_env, base_env, get_access_token):
        response = app.get_request(url_get_country, headers=get_access_token)
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        with allure.step("Запрос отправлен, сравним кол-во стран"):
            assert len(response.json()) == 260, f"Количество стран = {len(response.json())}"
        with allure.step("Десериализуем ответ и проверим валидацию"):
            validate(response.json(), app.get_json_schema(path_to_schemes_countries))
        update_test_case(update_get_country)

    @allure.testcase("https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T97")
    @allure.feature('Fias/SearchAddress')
    @allure.story('Поиск адресов')
    @allure.description('Проверяем найденный адрес и валидацию')
    @allure.severity(allure.severity_level.MINOR)
    def test_search_address(self, app, allure_env, base_env, get_access_token):
        response = app.post_request(url_search_address, headers=get_access_token, data=search_address)
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        with allure.step("Запрос отправлен, проверим что адрес нашелся"):
            assert response.json() == founded_address, f"Адрес не найден {response.text}"
        with allure.step("Десериализуем ответ и проверим валидацию"):
            validate(response.json(), app.get_json_schema(path_to_schemes_address))
        update_test_case(update_search_address)

    @allure.testcase("https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T98")
    @allure.feature('Fias/Details')
    @allure.story('Получить детализацию адреса по идентификатору FIAS')
    @allure.description('Отправляем запрос с идентификатором. Проверяем структуру и тело ответа')
    @allure.severity(allure.severity_level.MINOR)
    def test_get_details_fias(self, app, allure_env, base_env, get_access_token):
        response = app.get_request(url_search_details, headers=get_access_token)
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.text}"
        with allure.step("Десериализуем ответ и сравним город, тип адреса и Id"):
            assert response.json() == founded_kladr, f"Детализация адреса по КЛАДР не найдена {response.text}"
        with allure.step("Десериализуем ответ и проверим валидацию"):
            validate(response.json(), app.get_json_schema(path_to_schemes_kladdr))
        update_test_case(update_get_details_fias)
