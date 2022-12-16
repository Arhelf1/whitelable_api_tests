import allure
from data_for_tests.account import *
import json
import ast
from jsonschema import validate
from allure import severity, severity_level
from helpers.get_data_build import update_test_case
from sql.config import *
import pytest
from flaky import flaky


@allure.feature('White Label API: Account/')
class TestAccount:
    @allure.feature('Account/Registration')
    @allure.testcase("https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T77")
    @allure.story('Регистрация УЗ клиента')
    @allure.description('Регистрируем 3 УЗ клиента на один PartnerId и проверям ответ с данными из БД')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_create_user(self, app, db_cursor, get_data_reg, get_access_token, allure_env, base_env):
        response = app.post_request(url_registation, data=get_data_reg, headers=get_access_token)
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        global_id = app.get_dict(response.json(), ['UserId'], "Отсутствует ключ UserId из http url_registation")
        auth_id = app.get_dict(response.json(), ['AuthId'], "Отсутствует ключ AuthId из http url_registation")
        with allure.step("Запрос отправлен, проверим что UserId > 0"):
            assert len(global_id) > 0, f"Регистрация не прошла успешно, {response.json()}"
            assert type(auth_id) == int, f"Регистрация не прошла успешно {response.json()}"
        db_cursor['db_cursor'].execute(f"""
        SELECT  [GlobalId] as UserId
                ,[AuthId]
                FROM [{database}].[dbo].[Clients]
                where GlobalId = '{global_id}'  and 
                AuthId = '{auth_id}' and 
                PartnerId = 3
        """)
        sql_string = db_cursor['db_cursor'].fetchall()
        json_string = json.dumps(sql_string, ensure_ascii=False, default=str)
        json_string = ast.literal_eval(json_string)
        d = {}
        for i in json_string:
            d.update(i)
        with allure.step("Запрос отправлен, сравним с БД"):
            for el in d:
                assert str(response.json()[el]) == str(d[el]), f"Данные с БД разнятся"
        with allure.step("Десериализуем ответ и сравним валидацию"):
            validate(response.json(), app.get_json_schema(path_to_client_schema))
        update_test_case(update_create_user)

    @allure.testcase("https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T78")
    @allure.feature('Account/RegisterConfirm')
    @allure.story('Подтверждение Регистрации через СМС')
    @allure.description('В SetUp создаем тестового пользователя. Подтверждаем регистрацию через смс и сравниваем ответ')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_check_register(self, app, user_id, get_access_token, allure_env, base_env):
        response = app.post_request(url_register_confirm, headers=get_access_token, data={
            "code": "000000",
            "userId": user_id
        })
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        with allure.step("Запрос на подтверждение регистрации отправлен"):
            assert response.text == '"Success"', f"Регистрация прошла не успешно"
        update_test_case(update_check_register)

    @allure.testcase("https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T92")
    @allure.feature('Account/isRegistered')
    @allure.story('Проверка существования учетной записи')
    @allure.description('Отправляем запрос с данными подтвержденной УЗ и проверяем ответ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_account(self, app, get_access_token, allure_env, base_env):
        response = app.post_request(url_is_registered, headers=get_access_token, data=user_is_registered)
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        with allure.step("Запрос на проверку УЗ отправлен, посмотрим ответ"):
            assert response.text == 'true', f"УЗ не найдена"
        update_test_case(update_is_register)

    @allure.testcase("https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T79")
    @allure.feature('Account/AddIdentityDocument')
    @allure.story('Добавление паспортных данных в УЗ клиента')
    @allure.description('Отправляем запрос с паспортными данными и проверяем валидность ответа и тип добавленного документа. серию и номер')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_passport(self, app, reg_function, get_personal_data, allure_env, base_env):
        data = app.get_passport_data(user_id=reg_function['user_id'])
        number = data['passport']['number']
        serial = data['passport']['serial']
        response = app.post_request(url_get_passport, data=data, headers=reg_function['header'])
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        created_documents = response.json()['CreatedDocuments']
        new_dict = app.filter_value_in_list(created_documents, 'DocumentKind', 'RussianPassport')
        serial_number = new_dict['Number']
        document_kind = new_dict['DocumentKind']
        with allure.step("Паспортные данные отправлены. Сравним валидацию, тип и номер документа"):
            assert document_kind == "RussianPassport", f"Добавленный документ не паспорт, а {document_kind}"
            assert serial_number == serial + " " + number, f"Добавленные серия и номер не совпадают, а = {serial_number}"
            validate(response.json(), app.get_json_schema(path_to_passport_schema))
        update_test_case(update_add_passport)

    @allure.testcase("https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T83")
    @allure.feature('Account/AddInn')
    @allure.story('Добавление ИНН в УЗ клиента')
    @allure.description('Отправляем запрос с UserID и ИНН. Проверяем что добавленный документ это ИНН, значение ИНН верно, валидация верна')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_inn(self, app, reg_function, allure_env, base_env):
        data = app.get_inn_data(user_id=reg_function['user_id'])
        inn = data['inn']
        response = app.post_request(url_get_inn, data=data, headers=reg_function['header'])
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        created_documents = response.json()['CreatedDocuments']
        new_dict = app.filter_value_in_list(created_documents, 'DocumentKind', 'Inn')
        number = new_dict['Number']
        document_kind = new_dict['DocumentKind']
        with allure.step("ИНН отправлен, проверим что добавленный документ это ИНН, значение ИНН верное, валидацию ответа"):
            assert document_kind == "Inn", f"Добавленный документ не ИНН, а {document_kind}"
            assert number == inn, f"Добавленный ИНН не совпадает, а = {number}"
            validate(response.json(), app.get_json_schema(path_to_inn_schema))
        update_test_case(update_add_inn)

    @allure.testcase("https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T81")
    @allure.feature('Account/AddSnils')
    @allure.story('Добавление СНИЛС в УЗ клиента')
    @allure.description('Отправляем запрос с UserID и СНИЛС. Проверяем что добавленный документ это СНИЛС, значение СНИЛС верное, валидация верна')
    @allure.severity(allure.severity_level.MINOR)
    def test_add_snils(self, app, reg_function, allure_env, base_env):
        data = app.get_snils_data(user_id=reg_function['user_id'])
        snils = data['snils']
        response = app.post_request(url_get_snils, data=data, headers=reg_function['header'])
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        created_documents = response.json()['CreatedDocuments']
        new_dict = app.filter_value_in_list(created_documents, 'DocumentKind', 'Snils')
        number = new_dict['Number']
        document_kind = new_dict['DocumentKind']
        with allure.step("СНИЛС отправлен, проверим что добавленный документ это СНИЛС, значение СНИЛС верное, валидацию ответа"):
            assert document_kind == "Snils", f"Добавленный документ не СНИЛС, а {document_kind}"
            assert number == snils, f"Добавленный СНИЛС не совпадает, а = {number}"
            validate(response.json(), app.get_json_schema(path_to_snils_schema))
        update_test_case(update_add_snils)

    @allure.testcase("https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T125")
    @allure.feature('Account/ResetIdentityDocuments')
    @allure.story('Редактирование документов пользователя')
    @allure.description('В SetUp создаем пользователя с документами, в тестовом шаге редактируем их, проверяем что данные изменились, валидацию')
    @allure.severity(allure.severity_level.MINOR)
    def test_reset_identity_documents(self, app, allure_env, base_env, setup_set_identity_documents, reg_function):
        number = str(setup_set_identity_documents['passport']['number'])
        serial = str(setup_set_identity_documents['passport']['serial'])
        inn = setup_set_identity_documents['inn']
        snils = setup_set_identity_documents['snils']
        with allure.step("Отправляем запрос к Account/ResetIdentityDocuments"):
            response = app.post_request(url_set_identity_documents, data=setup_set_identity_documents, headers=reg_function['header'])
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        with allure.step("Проверяем что изменились паспортные данные"):
            created_documents = response.json()['CreatedDocuments']
            new_dict = app.filter_value_in_list(created_documents, 'DocumentKind', 'RussianPassport')
            serial_number = new_dict['Number']
            document_kind = new_dict['DocumentKind']
            assert document_kind == "RussianPassport", f"Добавленный документ не паспорт, а {document_kind}"
            assert serial_number == serial + " " + number, f"Добавленные серия и номер не совпадают, а = {serial_number}"
        with allure.step("Проверяем что изменилась ИНН"):
            new_dict = app.filter_value_in_list(created_documents, 'DocumentKind', 'Inn')
            number = new_dict['Number']
            document_kind = new_dict['DocumentKind']
            assert document_kind == "Inn", f"Добавленный документ не ИНН, а {document_kind}"
            assert number == inn, f"Добавленный ИНН не совпадает, а = {number}"
        with allure.step("Проверяем что изменился СНИЛС"):
            new_dict = app.filter_value_in_list(created_documents, 'DocumentKind', 'Snils')
            number = new_dict['Number']
            document_kind = new_dict['DocumentKind']
            assert document_kind == "Snils", f"Добавленный документ не СНИЛС, а {document_kind}"
            assert number == snils, f"Добавленный СНИЛС не совпадает, а = {number}"
        with allure.step("Проверяем валидацию"):
            validate(response.json(), app.get_json_schema(path_to_reset_documents_schema))
        update_test_case(update_reset_documents)

    @allure.testcase('https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T85')
    @allure.feature('Account/SetUserAddress')
    @allure.story('Указание адреса клиента')
    @allure.description('Отправляем запрос с UserId и адресом. Проверяем что ответ Success')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_address(self, app, reg_function, get_data_address, allure_env, base_env):
        response = app.post_request(url_get_address, data=get_data_address, headers=reg_function['header'])
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        with allure.step("Данные с адресом отправлены. Проверим что ответ Success"):
            assert response.text == '"Success"', f"Адрес не добавлен, из-за {response.text}"
        update_test_case(update_add_address)

    @allure.testcase('https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T86')
    @allure.feature('Account/SetNonResidentAddress')
    @allure.story('Указание адреса клиента нерезидента')
    @allure.description('Отправляем запрос с UserId и адресом. Проверяем что ответ Success')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_add_custom_address(self, app, reg_function, get_custom_data_address, allure_env, base_env):
        response = app.post_request(url_get_custom_address, data=get_custom_data_address, headers=reg_function['header'])
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        with allure.step("Данные с дополнительными адресами отправлены. Проверим что ответ Success"):
            assert response.text == '"Success"', f"Адрес не добавлен, из-за {response.text}"
        update_test_case(update_add_custom_address)

    @allure.testcase('https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T84')
    @allure.feature('Account/UpdatePersonalInfo')
    @allure.story('Обновление персональных данных')
    @allure.description('Отправляем запрос с персональными данными. Проверяем ответ на содержание и валидность')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_personal_info(self, app, reg_function, get_personal_info, allure_env, base_env):
        response = app.post_request(url_get_personal_info, data=get_personal_info['response'], headers=reg_function['header'])
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}. Текст ошибки {response.json()}"
        with allure.step("Запрос с персональными данными отправлен. Проверим ответ на содержание"):
            assert response.json() == get_personal_info['request'], f"Данные не обновлены, потому что {response.json()}"
            validate(response.json(), app.get_json_schema(path_to_personal_info_schema))
        update_test_case(update_update_personal_info)

    @allure.testcase('https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T87')
    @allure.feature('Account/CreateSmsSignAgreement')
    @allure.story('Создание документов присоединения к регламенту Моревиль')
    @allure.description('Подготовительным шагом добавляем тестовому пользователю документы(Паспорт, СНИЛС, ИНН). В тестовом шаге отправляем запрос с UserId. Проверяем ответ на соответствие UserId, валидность ответа ')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_create_sms_sign_agreement(self, app, setup_create_sms_sign, allure_env, base_env):
        response = app.post_request(url_get_create_sms_sign, data=setup_create_sms_sign['data'], headers=setup_create_sms_sign['header'])
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        with allure.step('Запрос с UserId на присоединение к регламенту Моревиль отправлен. Проверим документ и валидность ответа'):
            assert response.json()[0]['Name'] == "Заявление о присоединении и регистрации в КИС", f"Созданный документ неверный, {response.json()}"
            validate(response.json(), app.get_json_schema(path_to_create_sms_sign_schema))
        update_test_case(update_create_sms_sign_agreement)

    @allure.testcase('https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T88')
    @allure.feature('Account/SignSmsSignAgreement')
    @allure.story('Подписание регламента Моревиль (отправка смс)')
    @allure.description('Подготовительным шагом добавляем тестовому пользователю документы и присоединяем его к Моревиль. В тестовом шаге получаем смс, проверяем что пришло Id отправки, валидность')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_sign_sms_sign(self, app, setup_sign_sms_sign, allure_env, base_env):
        data = {
            "documentIds": [setup_sign_sms_sign["id"]],
            "userId": setup_sign_sms_sign["user_id"]
        }
        response = app.post_request(url_get_sign_sms_sign, data=data, headers=setup_sign_sms_sign['header'])
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        with allure.step("Запрос на подтверждение присоединения к Моревиль отправлен. Проверим что смс ушла для этого пользователя, документ, валидность ответа"):
            assert response.json()['UserId'] == setup_sign_sms_sign['user_id'], f"UserId не совпадают, потому что {response.json()}"
            assert response.json()['DocumentsToSign'][0]['Name'] == "Заявление о присоединении и регистрации в КИС", f"Созданный документ неверный, {response.json()}"
            validate(response.json(), app.get_json_schema(path_to_sign_sms_sign_schema))
        update_test_case(update_sign_sms_sign)

    @allure.testcase('https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T119')
    @allure.feature('Account/ConfirmSmsSignAgreement')
    @allure.story('СМС подтверждение присоединения о присоединении к регламенту Моревиль')
    @allure.description('Подготовительным шагом добавляем тестовому пользователю документы и присоединяем его к Моревиль. В тестовом шаге подписываем, проверяем, что подписалось, валидность')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_confirm_sms_sign(self, app, setup_sign_sms_confirm, allure_env, base_env):
        response = app.post_request(url_confirm_sms_sign, data=setup_sign_sms_confirm["data"], headers=setup_sign_sms_confirm["header"])
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        with allure.step("Провери, что документ подписался"):
            assert response.json()["IsApproved"] == True, f"Документ не подписался, текст ошибки {response.json()}"
            assert response.json()["Id"] == setup_sign_sms_confirm["data"]["Id"], f"Id заявки неверный, текст ошибки {response.json()}"
            validate(response.json(), app.get_json_schema(path_confirm_sms_sign_schema))
        update_test_case(update_confirm_sms_sign)

    @allure.testcase('https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T90')
    @allure.feature('Account/CreateConnectClientToProduct')
    @allure.story('Создает пакет документов для подключения продукта клиенту')
    @allure.description('Подготовительным шагом создаем пользователя и добавляем ему паспорт и перс. данные. В тестовом шаге отправляем запрос с Id продукта и UserId')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_create_connect_client_to_product(self, app, setup_create_connect_client_to_product, allure_env, base_env):
        data = {
            "productId": 126,
            "userId": setup_create_connect_client_to_product['user_id']
        }
        response = app.post_request(url_create_connect_client_to_product, data=data, headers=setup_create_connect_client_to_product['header'])
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        with allure.step("Запрос на формирование документов на подпись отправлен, проверим документы и валидацию"):
            from random import randint
            assert response.json()[randint(0, 11)]["Name"] in documents_create_connect_client_to_product, f"Документ не найден в списке документов, код ошибки {response.json()}"
            validate(response.json(), app.get_json_schema(path_to_create_connect_client_to_product_schema))
        update_test_case(update_create_connect_client_to_product)

    @allure.testcase('https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T120')
    @allure.feature('Account/SignConnectClientToProduct')
    @allure.story('Отправляем смс для подписания документов на добавление продукта')
    @allure.description('Подготовительным шагом создаем пользователя и добавляем ему паспорт и перс. данные. В тестовом шаге отправляем запрос с Id документов и UserId')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_sign_connect_client_to_product(self, app, setup_sign_connect_client_to_product, allure_env, base_env):
        response = app.post_request(url_sign_connect_client_to_product, data=setup_sign_connect_client_to_product['data'], headers=setup_sign_connect_client_to_product['header'])
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        with allure.step("Запрос на отправку смс отправлен, проверяем документы и валидацию"):
            from random import randint
            assert response.json()['DocumentsToSign'][randint(0, 11)]["Name"] in documents_create_connect_client_to_product, f"Документ не найден в списке документов, код ошибки {response.json()}"
            validate(response.json(), app.get_json_schema(path_to_sign_connect_client_to_product_schema))
        update_test_case(update_sign_connect_client_to_product)

    @allure.testcase('https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T91')
    @allure.feature('Account/SmsSignConnectClientToProduct')
    @allure.story('Подпись документов по подключению продукта клиенту')
    @allure.description('Подготовительным шагом создаем пользователя с паспортом, присоединяем его к продукту. В тестовом шаге подтверждаем присоединение. Проверяем что подпись подтверждена и валидность')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_confirm_connect_client_to_product(self, app, setup_confirm_connect_client, allure_env, base_env):
        response = app.post_request(url_confirm_connect, data=setup_confirm_connect_client['data'], headers=setup_confirm_connect_client['header'])
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        with allure.step('Запрос на подпись документов отправлен. Проверим что они подписались, Id подписания, валидность'):
            assert response.json()['IsApproved'] == True, f"Подписание прошло не успешно, потому что {response.json()}"
            assert response.json()['Id'] == setup_confirm_connect_client['data']['id'], f"Id подписания не совпадает, потому что {response.json()}"
            assert response.json()['UserId'] == setup_confirm_connect_client['data']['userId'], f"UserId не совпадает, потому что {response.json()}"
            validate(response.json(), app.get_json_schema(path_to_confirm_connect))
        update_test_case(update_confirm_connect_client_to_product)

    @allure.testcase('https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T101')
    @allure.feature('Account/AddPassportScans')
    @allure.story('Производит распознавание сканов страниц паспорта')
    @allure.description('Подготовительным шагом создаем пользователя. Проверяем что на скан паспорта вернулись корректные данные, валидацию.')
    @pytest.mark.parametrize("file, excepted", [(file_passport_jpg, passport_data_after_request), (file_passport_png, passport_data_after_request), (file_passport_pdf, passport_data_after_request_pdf)])
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_passport_scans(self, app, reg_function, allure_env, base_env, file, excepted):
        with allure.step("Отправляем запрос со сканом паспорта"):
            response = app.post_request(url_add_passport_scans, files=file, data={}, headers=reg_function['header_f'])
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        with allure.step('Проверяем что пришли корректные данные'):
            assert response.json() == excepted, f'Данные пришли не корректные, данные = {response.json()}'
        with allure.step('Проверяем валидность'):
            validate(response.json(), app.get_json_schema(path_to_passport_scans_schema))
        update_test_case(update_add_passport_scans)

    @allure.testcase('https://jira.finam.ru/secure/Tests.jspa#/testCase/INTRA-T124')
    @allure.feature('Account/AddPassportScans')
    @allure.story('Производит распознавание сканов страниц паспорта и добавляет их к клиенту')
    @allure.description('Подготовительным шагом создаем пользователя с документами, подключаем АСП и пакет 126. Добавляем скан паспорта, проверяем что он добавился в документы')
    @allure.severity(allure.severity_level.NORMAL)
    @flaky(max_runs=3, min_passes=1)
    def test_check_passport_scan_in_documents(self, app, setup_get_documents_files):
        list_file_name = []
        with allure.step("Отправляем запрос со сканом паспорта"):
            response = app.post_request(url_add_passport_scans, files=file_passport_test, data={}, headers=setup_get_documents_files['header_f'])
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        with allure.step('Отправляем запрос к /Documents/GetDocumentFiles'):
            response = app.post_request(url_get_documents_files, data=setup_get_documents_files['data'], headers=setup_get_documents_files['header'])
        with allure.step("Проверим что ответ 200"):
            assert response.status_code == 200, f"Ответ не 200, а {response.status_code}, текст ошибки: {response.json()}"
        with allure.step('Проверяем что скан паспорта добавился к документам'):
            for el in response.json():
                list_file_name.append(el['FileName'])
            assert 'passport-test.jpeg' in list_file_name, f"Скан паспорта не добавился к документам пользователя, документы пользователя = {list_file_name}"
        update_test_case(update_check_passport_scan_in_documents)




