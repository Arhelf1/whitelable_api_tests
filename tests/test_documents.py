import allure
from data_for_tests.documents import *
from jsonschema import validate

from helpers.get_data_build import update_test_case


@allure.feature('White Label API: Documents/')
class TestDocuments:
    @allure.feature('Documents/GetDocumentFiles')
    @allure.testcase("https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T94")
    @allure.story('Получить информацию о списке файлов документа')
    @allure.description('В Setup создаем пользователя, добавляем ему документы, присоединяем его к Моревиль и добавляем продукт. Отправляем запрос на получение списка документов. Проверяем название файлов, валидацию')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_documents_files(self, app, setup_get_documents_files, allure_env, base_env):
        response = app.post_request(url_get_documents_files, data=setup_get_documents_files['data'], headers=setup_get_documents_files['header'])
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        with allure.step("Запрос на получение списка документов отправлен. Проверим название файлов и валидацию"):
            assert response.json()[0]['FileName'] == 'bbbtestbb', f"Документ не найден, потому что {response.json()}"
            assert response.json()[1]['FileName'] == 'bbbtestbb.sms', f"Документ не найден, потому что {response.json()}"
            validate(response.json(), app.get_json_schema(path_json_scheme_get_documents_files))
        update_test_case(update_get_documents_files)

    @allure.feature('Documents/GetFileContent')
    @allure.testcase('https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T95')
    @allure.story('Получить содержимое файла')
    @allure.description('В Setup оздаем пользователя с документами, присоединяем к Моревиль и добавляем продукт, получаем список документов. Проверяем что есть необходимый')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_file_content(self, app, setup_get_file_content, allure_env, base_env):
        response = app.post_request(url_get_file_content, data=setup_get_file_content['data'], headers=setup_get_file_content['header'])
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        with allure.step("Запрос на просмотр содержимого файла отправлен. Проверим наличие контента"):
            assert response.text == "Hello", f"Контент не найден, потому что {response.text}"
        update_test_case(update_get_file_content)
