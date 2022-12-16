import allure
import pytest

from data_for_tests.partner_auth import *
from jsonschema import validate
from data_for_tests.auth import *
from helpers.common import response_status
from helpers.get_data_build import update_test_case
from sql.config import *

import requests


@allure.feature('White Label API: PartnerAuth/')
class TestPartnerAuth:
    @allure.testcase("https://jira.finam.ru/secure/Tests.jspa#/testCase/WHTLBL-T417")
    @allure.feature('PartnerAuth/RefreshToken')
    @allure.story('Обновление Access токена (и одновременно Refresh токена)')
    @allure.description('В SetUp создаем refresh token, отправляем запрос с ним и получаем access token. Сравнимаем результат с БД и валидацию')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_access_token(self, app, setup_get_access_token, db_cursor, allure_env, base_env):
        response = app.post_request(url_get_access, data=setup_get_access_token, headers=headers)
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        data_request = {
            "RefreshToken": response.json()["RefreshToken"],
            "AccessToken": response.json()['AccessToken'],
            "GlobalId": 'CB176865-D136-42FE-8D7E-B0AB30FCF399'
        }
        db_cursor['db_cursor'].execute(f"""
        SELECT [GlobalId]
        ,[RefreshToken]
        ,[AccessToken]
        FROM [{database}].[dbo].[Partners]
        where GlobalId = 'CB176865-D136-42FE-8D7E-B0AB30FCF399' and RefreshToken = '{data_request['RefreshToken']}'
        and AccessToken = '{data_request['AccessToken']}'
        """)
        sql_string = db_cursor['db_cursor'].fetchall()
        sql_dict = sql_string[0]
        with allure.step("Сравним данные с БД"):
            assert data_request == sql_dict, f"Данные с БД разные, данные из запроса = {data_request}, а данные из БД = {sql_dict}"
        with allure.step("Сравним валидацию"):
            validate(response.json(), app.get_json_schema(path_to_access_schema))
        update_test_case(update_get_access_token)

    @allure.testcase('https://jira.finam.ru/secure/Tests.jspa#/testCase/WHTLBL-T33')
    @allure.feature('Token/CreateRefresh')
    @allure.story('Получение Refresh токена с использованием globalId')
    @allure.description('Получение результата выполнения метода')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_new_refresh_token(self, allure_env):
        response = requests.request("POST", url_refresh, headers={}, data={})
        with allure.step("Проверка того, что код ответа 200, 201 или 202"):
            if response.status_code in [200, 201, 202]:
                f"Тест пройден успешно"
            else:
                f'Status_code не 200, а {response.status_code}'
                raise AssertionError('Status_code не 200, 201, 202, а ', response.status_code) from None

    @allure.testcase('https://jira.finam.ru/secure/Tests.jspa#/testCase/WHTLBL-T34')
    @allure.feature('PartnerAuth/RefreshToken')
    @allure.story('Получение Access токена и обновление Refresh токена')
    @allure.description('Проверка результата теста')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_new_create_access_token(self, app, allure_env, base_env):
        response = app.post_request(url_refresh, headers={}, data={}, flag=False)
        data_ = {'RefreshToken': response.text, 'AccessToken': ''}
        response = app.post_request(short_url_access, headers=headers, data=data_)
        with allure.step("Проверка того, что код ответа 200, 201 или 202"):
            if response.status_code in [200, 201, 202]:
                f"Тест пройден успешно"
            else:
                f'Status_code не 200, 201, 202, а {response.status_code}'
                raise AssertionError('Status_code != 200, 201, 202, а', response.status_code) from None

    @allure.testcase('https://jira.finam.ru/secure/Tests.jspa#/testCase/WHTLBL-T417')
    @allure.feature('PartnerAuth/RefreshToken')
    @allure.story('Обновление Access токена и обновление Refresh токена')
    @allure.description('Проверка обновления access токена ')
    @allure.severity(allure.severity_level.NORMAL)
    def test_new_update_access_token(self, app, allure_env, base_env):
        response = requests.request("POST", url_refresh, headers={}, data={})
        data_ = {'RefreshToken': response.text, 'AccessToken': ""}
        response = app.post_request(short_url_access, headers=headers, data=data_)
        with allure.step("Проверка того, что код ответа 200, 201, 202"):
            if response.status_code in [200, 201, 202]:
                data_ = {"RefreshToken": response.json()["RefreshToken"], "AccessToken": response.json()['AccessToken']}
                response = app.post_request(short_url_access, headers=headers, data=data_)
                if response.status_code in [200, 201, 202]:
                    f"Тест пройден успешно"
                else:
                    f'Status_code не 200, 201 или 202, а  {response.status_code}'
                    raise AssertionError('Status_code не 200, 201 или 202, а ', response.status_code) from None
            else:
                f'Status_code не 200, 201 или 202, а {response.status_code}'
                raise AssertionError('Status_code не 200, а ', response.status_code) from None

    @allure.testcase('https://jira.finam.ru/secure/Tests.jspa#/testCase/WHTLBL-T413')
    @allure.feature('txauth/v3/auth')
    @allure.story('Получение токена авторизации')
    @allure.description('Проверка получения токена авторизации ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_auth_token(self, allure_env):
        registration_data = {'login': 'Igor321', 'password': 'Igor321'}
        data_ = registration_data['login']
        pass_ = registration_data['password']
        response = requests.request("POST", url="https://txdev.finam.ru/grpc-json/txauth/v3/auth/EDO_DEV/" + data_,
                                    headers=auth_headers, data=data.replace('Vfhn2019', pass_))
        with allure.step("Проверка того, что код ответа 200, 201, 202 и токен не пустой"):
            if response.status_code in [200, 201, 202]:
                if response.json()['token'] != '':
                    f"Тест пройден успешно"
                else:
                    f'Token = "" '
                    raise AssertionError('Token = "" ') from None
            else:
                f'Status_code не 200, 201 или 202, а {response.status_code}'
                raise AssertionError('Status_code не 200, 201 или 202, а ', response.status_code) from None

    @allure.testcase('https://jira.finam.ru/secure/Tests.jspa#/testCase/WHTLBL-T416')
    @allure.feature('txauth/v3/auth')
    @allure.story('Проверка валидации полей метода')
    @allure.description('Негативные проверки получения токена авторизации')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('pass_', ['', '123', 1000*'wqe'])
    def test_validation_auth_token(self, app, pass_, allure_env):
        registration_data = {'login': 'Igor321', 'password': 'Igor321'}
        data_ = registration_data['login']
        response = requests.request("POST", url="https://txdev.finam.ru/grpc-json/txauth/v3/auth/EDO_DEV/" + data_, headers=auth_headers, data=data.replace('Vfhn2019', pass_))
        with allure.step("Проверка того, что код ответа 200, 201, 202 и токен пустой"):
            if response.status_code in [200, 201, 202]:
                if response.json()['token'] == '':
                    f"Тест пройден успешно"
                else:
                    f'Token != "" '
                    raise AssertionError('Token = "" ') from None
            else:
                f'Status_code не 200, 201 или 202, а {response.status_code}'
                raise AssertionError('Status_code не 200, 201 или 202, а ', response.status_code) from None