import allure
import pytest
from flaky import flaky
import pdfplumber


@allure.feature('White Label Integration Tests BackOffice')
class TestIntegrationBO:
    @allure.feature('Проверка документа "Заявление о присоединении к Регламенту, регистрации в КИС"')
    @allure.story('Подключение АСП - Account/CreateSmsSignAgreement')
    @allure.description('В Setup создаем пользователя(перс. данные, документы), присоединяем его к Моревиль, скачиваем документ, проверяем что в нем корректные данные')
    @pytest.mark.integtest
    @flaky(max_runs=3, min_passes=1)
    def test_get_document_asp(self, app, setup_get_document_asp, allure_env, base_env):
        with allure.step('Скачиваем документ "Заявление о присоединении и регистрации в КИС"'):
            app.download_file_by_id(file_id=setup_get_document_asp['data_for_request']['fileId'], file_name='Заявление о присоединении и регистрации в КИС',
                                    user_id=setup_get_document_asp['data_for_request']['userId'], header=setup_get_document_asp['header'])
        with allure.step('Проверяем что в документе корректные ФИО и серия номер паспорта'):
            with pdfplumber.open('documents_for_parse//Заявление о присоединении и регистрации в КИС.pdf') as pdf:
                first_page = pdf.pages[0]
                assert setup_get_document_asp['data_for_parse'][0] in first_page.extract_text(), f"ФИО в шапке документа неверные, документ ={first_page.extract_text()}"
                assert setup_get_document_asp['data_for_parse'][1] in first_page.extract_text(), f"ФИО в футере документа неверные, документ ={first_page.extract_text()}"
                assert str(setup_get_document_asp['data_for_parse'][2]['passport']['serial']) in first_page.extract_text(), f"Серия паспорта в шапке документа неверная, документ ={first_page.extract_text()}"
                assert str(setup_get_document_asp['data_for_parse'][2]['passport']['number']) in first_page.extract_text(), f"Номер паспорта в шапке документа неверный, документ ={first_page.extract_text()}"
        with allure.step("TearDown! Удаляем скачанный файл по имени"):
            app.remove_file_by_name(abs_path='documents_for_parse//Заявление о присоединении и регистрации в КИС.pdf')

    @allure.feature('Проверка документа "Заявление о присоединении к Деп. договору"')
    @allure.story('Подключение Продукта WhiteLabel 126 - Account/CreateConnectClientToProduct')
    @allure.description('В Setup создаем пользователя(перс. данные, документы), присоединяем его к Моревиль, подключаем продукт 126, скачиваем документ, проверяем что в нем корректные данные')
    @pytest.mark.integtest
    @flaky(max_runs=3, min_passes=1)
    def test_get_document_accedence(self, app, setup_get_documents_from_product, allure_env, base_env):
        with allure.step("Ищем документ 'Заявление о присоединении к Деп. договору' по имени"):
            accedence_id = app.find_file_id_by_name(request=setup_get_documents_from_product['list_documents'], name='Заявление о присоединении к Деп. договору')
        with allure.step("Скачиваем документ 'Заявление о присоединении к Деп. договору'"):
            app.download_file_by_id(file_id=accedence_id, file_name='Заявление о присоединении к Деп. договору', user_id=setup_get_documents_from_product['user_id'], header=setup_get_documents_from_product['header'])
        with allure.step('Проверяем что в документе корректные ФИО и серия номер паспорта'):
            with pdfplumber.open('documents_for_parse//Заявление о присоединении к Деп. договору.pdf') as pdf:
                first_page = pdf.pages[0]
                assert setup_get_documents_from_product['data_for_parse'][0] in first_page.extract_text(), f"ФИО в шапке документа неверные, документ ={first_page.extract_text()}"
                assert setup_get_documents_from_product['data_for_parse'][1] in first_page.extract_text(), f"ФИО в футере документа неверные, документ ={first_page.extract_text()}"
                assert str(setup_get_documents_from_product['data_for_parse'][2]['passport']['serial']) in first_page.extract_text(), f"Серия паспорта в футере документа неверная, документ ={first_page.extract_text()}"
                assert str(setup_get_documents_from_product['data_for_parse'][2]['passport']['number']) in first_page.extract_text(), f"Номер паспорта в футере документа неверный, документ ={first_page.extract_text()}"
        with allure.step("TearDown! Удаляем скачанный файл по имени"):
            app.remove_file_by_name(abs_path='documents_for_parse//Заявление о присоединении к Деп. договору.pdf')

    @allure.feature('Проверка документа "Заявление о выборе условий обслуживания"')
    @allure.story('Подключение Продукта WhiteLabel 126 - Account/CreateConnectClientToProduct')
    @allure.description('В Setup создаем пользователя(перс. данные, документы), присоединяем его к Моревиль, подключаем продукт 126, скачиваем документ, проверяем что в нем корректные данные')
    @pytest.mark.integtest
    @flaky(max_runs=3, min_passes=1)
    def test_get_document_service_condition(self, app, setup_get_documents_from_product, allure_env, base_env):
        with allure.step("Ищем документ 'Заявление о выборе условий обслуживания' по имени"):
            service_condition_id = app.find_file_id_by_name(request=setup_get_documents_from_product['list_documents'], name='Заявление о выборе условий обслуживания')
        with allure.step("Скачиваем документ 'Заявление о выборе условий обслуживания'"):
            app.download_file_by_id(file_id=service_condition_id, file_name='Заявление о выборе условий обслуживания', user_id=setup_get_documents_from_product['user_id'], header=setup_get_documents_from_product['header'])
        with allure.step('Проверяем что в документе корректные ФИО и серия номер паспорта'):
            with pdfplumber.open('documents_for_parse//Заявление о выборе условий обслуживания.pdf') as pdf:
                first_page = pdf.pages[0]
                assert setup_get_documents_from_product['data_for_parse'][0] in first_page.extract_text(), f"ФИО в шапке документа неверные, документ ={first_page.extract_text()}"
                assert setup_get_documents_from_product['data_for_parse'][1] in first_page.extract_text(), f"ФИО в футере документа неверные, документ ={first_page.extract_text()}"
                assert str(setup_get_documents_from_product['data_for_parse'][2]['passport']['serial']) in first_page.extract_text(), f"Серия паспорта в шапке документа неверная, документ ={first_page.extract_text()}"
                assert str(setup_get_documents_from_product['data_for_parse'][2]['passport']['number']) in first_page.extract_text(), f"Номер паспорта в шапке документа неверный, документ ={first_page.extract_text()}"
        with allure.step("TearDown! Удаляем скачанный файл по имени"):
            app.remove_file_by_name(abs_path='documents_for_parse//Заявление о выборе условий обслуживания.pdf')

    @allure.feature('Проверка документа "Сведения о связанных лицах"')
    @allure.story('Подключение Продукта WhiteLabel 126 - Account/CreateConnectClientToProduct')
    @allure.description('В Setup создаем пользователя(перс. данные, документы), присоединяем его к Моревиль, подключаем продукт 126, скачиваем документ, проверяем что в нем корректные данные')
    @pytest.mark.integtest
    @flaky(max_runs=3, min_passes=1)
    def test_get_document_related_people(self, app, setup_get_documents_from_product, allure_env, base_env):
        with allure.step("Ищем документ 'Сведения о связанных лицах' по имени"):
            related_people_id = app.find_file_id_by_name(request=setup_get_documents_from_product['list_documents'], name='Сведения о связанных лицах')
        with allure.step("Скачиваем документ 'Сведения о связанных лицах'"):
            app.download_file_by_id(file_id=related_people_id, file_name='Сведения о связанных лицах', user_id=setup_get_documents_from_product['user_id'], header=setup_get_documents_from_product['header'])
        with allure.step('Проверяем что в документе корректные ФИО'):
            with pdfplumber.open('documents_for_parse//Сведения о связанных лицах.pdf') as pdf:
                first_page = pdf.pages[0]
                assert setup_get_documents_from_product['data_for_parse'][0] in first_page.extract_text(), f"ФИО в шапке документа неверные, документ ={first_page.extract_text()}"
        with allure.step("TearDown! Удаляем скачанный файл по имени"):
            app.remove_file_by_name(abs_path='documents_for_parse//Сведения о связанных лицах.pdf')

    @allure.feature('Проверка документа "Согласие на передачу персональных данных"')
    @allure.story('Подключение Продукта WhiteLabel 126 - Account/CreateConnectClientToProduct')
    @allure.description('В Setup создаем пользователя(перс. данные, документы), присоединяем его к Моревиль, подключаем продукт 126, скачиваем документ, проверяем что в нем корректные данные')
    @pytest.mark.integtest
    @flaky(max_runs=3, min_passes=1)
    def test_get_document_transfer_personal_data(self, app, setup_get_documents_from_product, allure_env, base_env):
        with allure.step("Ищем документ 'Согласие на передачу персональных данных' по имени"):
            personal_data_id = app.find_file_id_by_name(request=setup_get_documents_from_product['list_documents'], name='Согласие на передачу персональных данных')
        with allure.step("Скачиваем документ 'Согласие на передачу персональных данных'"):
            app.download_file_by_id(file_id=personal_data_id, file_name='Согласие на передачу персональных данных', user_id=setup_get_documents_from_product['user_id'], header=setup_get_documents_from_product['header'])
        with allure.step('Проверяем что в документе корректные ФИО'):
            with pdfplumber.open('documents_for_parse//Согласие на передачу персональных данных.pdf') as pdf:
                first_page = pdf.pages[0]
                assert setup_get_documents_from_product['data_for_parse'][0] in first_page.extract_text(), f"ФИО в шапке документа неверные, документ ={first_page.extract_text()}"
        with allure.step("TearDown! Удаляем скачанный файл по имени"):
            app.remove_file_by_name(abs_path='documents_for_parse//Согласие на передачу персональных данных.pdf')

    @allure.feature('Проверка документа "Акт о получении идентификационного кода"')
    @allure.story('Подключение Продукта WhiteLabel 126 - Account/CreateConnectClientToProduct')
    @allure.description('В Setup создаем пользователя(перс. данные, документы), присоединяем его к Моревиль, подключаем продукт 126, скачиваем документ, проверяем что в нем корректные данные')
    @pytest.mark.integtest
    @flaky(max_runs=5, min_passes=1)
    def test_get_document_id_code(self, app, setup_get_documents_from_product, allure_env, base_env):
        with allure.step("Ищем документ 'Акт о получении идентификационного кода' по имени"):
            id_code_id = app.find_file_id_by_name(request=setup_get_documents_from_product['list_documents'], name='Акт о получении идентификационного кода')
        with allure.step("Скачиваем документ 'Акт о получении идентификационного кода'"):
            app.download_file_by_id(file_id=id_code_id, file_name='Акт о получении идентификационного кода', user_id=setup_get_documents_from_product['user_id'], header=setup_get_documents_from_product['header'])
        with allure.step('Проверяем что в документе корректные ФИО'):
            with pdfplumber.open('documents_for_parse//Акт о получении идентификационного кода.pdf') as pdf:
                first_page = pdf.pages[0]
                assert setup_get_documents_from_product['data_for_parse'][0] in first_page.extract_text(), f"ФИО в шапке документа неверные, документ ={first_page.extract_text()}"
                assert setup_get_documents_from_product['data_for_parse'][1] in first_page.extract_text(), f"ФИО в футере документа неверные, документ ={first_page.extract_text()}"
        with allure.step("TearDown! Удаляем скачанный файл по имени"):
            app.remove_file_by_name(abs_path='documents_for_parse//Акт о получении идентификационного кода.pdf')

    @allure.feature('Проверка документа "Акт о получении доступа в ЛК"')
    @allure.story('Подключение Продукта WhiteLabel 126 - Account/CreateConnectClientToProduct')
    @allure.description('В Setup создаем пользователя(перс. данные, документы), присоединяем его к Моревиль, подключаем продукт 126, скачиваем документ, проверяем что в нем корректные данные')
    @pytest.mark.integtest
    @flaky(max_runs=3, min_passes=1)
    def test_get_document_access_to_lk(self, app, setup_get_documents_from_product, allure_env, base_env):
        with allure.step("Ищем документ 'Акт о получении доступа в ЛК' по имени"):
            access_lk_id = app.find_file_id_by_name(request=setup_get_documents_from_product['list_documents'], name='Акт о получении доступа в ЛК')
        with allure.step("Скачиваем документ 'Акт о получении доступа в ЛК'"):
            app.download_file_by_id(file_id=access_lk_id, file_name='Акт о получении доступа в ЛК', user_id=setup_get_documents_from_product['user_id'], header=setup_get_documents_from_product['header'])
        with allure.step('Проверяем что в документе корректные ФИО и серия номер паспорта'):
            with pdfplumber.open('documents_for_parse//Акт о получении доступа в ЛК.pdf') as pdf:
                first_page = pdf.pages[0]
                assert setup_get_documents_from_product['data_for_parse'][0] in first_page.extract_text(), f"ФИО в шапке документа неверные, документ ={first_page.extract_text()}"
                assert setup_get_documents_from_product['data_for_parse'][1] in first_page.extract_text(), f"ФИО в футере документа неверные, документ ={first_page.extract_text()}"
                assert str(setup_get_documents_from_product['data_for_parse'][2]['passport']['serial']) in first_page.extract_text(), f"Серия паспорта в футере документа неверная, документ ={first_page.extract_text()}"
                assert str(setup_get_documents_from_product['data_for_parse'][2]['passport']['number']) in first_page.extract_text(), f"Номер паспорта в футере документа неверный, документ ={first_page.extract_text()}"
        with allure.step("TearDown! Удаляем скачанный файл по имени"):
            app.remove_file_by_name(abs_path='documents_for_parse//Акт о получении доступа в ЛК.pdf')

    @allure.feature('Проверка документа "Статус физического лица"')
    @allure.story('Подключение Продукта WhiteLabel 126 - Account/CreateConnectClientToProduct')
    @allure.description('В Setup создаем пользователя(перс. данные, документы), присоединяем его к Моревиль, подключаем продукт 126, скачиваем документ, проверяем что в нем корректные данные')
    @pytest.mark.integtest
    @flaky(max_runs=3, min_passes=1)
    def test_get_document_status_person(self, app, setup_get_documents_from_product, allure_env, base_env):
        with allure.step("Ищем документ 'Статус физического лица' по имени"):
            status_person_id = app.find_file_id_by_name(request=setup_get_documents_from_product['list_documents'], name='Статус физического лица')
        with allure.step("Скачиваем документ 'Статус физического лица'"):
            app.download_file_by_id(file_id=status_person_id, file_name='Статус физического лица', user_id=setup_get_documents_from_product['user_id'], header=setup_get_documents_from_product['header'])
        with allure.step('Проверяем что в документе корректные ФИО'):
            with pdfplumber.open('documents_for_parse//Статус физического лица.pdf') as pdf:
                first_page = pdf.pages[0]
                assert setup_get_documents_from_product['data_for_parse'][0] in first_page.extract_text(), f"ФИО в шапке документа неверные, документ ={first_page.extract_text()}"
        with allure.step("TearDown! Удаляем скачанный файл по имени"):
            app.remove_file_by_name(abs_path='documents_for_parse//Статус физического лица.pdf')

    @allure.feature('Проверка документа "Анкета физического лица"')
    @allure.story('Подключение Продукта WhiteLabel 126 - Account/CreateConnectClientToProduct')
    @allure.description('В Setup создаем пользователя(перс. данные, документы), присоединяем его к Моревиль, подключаем продукт 126, скачиваем документ, проверяем что в нем корректные данные')
    @pytest.mark.integtest
    @flaky(max_runs=3, min_passes=1)
    def test_get_document_form_person(self, app, setup_get_documents_from_product, allure_env, base_env):
        with allure.step("Ищем документ 'Анкета физического лица' по имени"):
            form_person_id = app.find_file_id_by_name(request=setup_get_documents_from_product['list_documents'], name='Анкета физического лица')
        with allure.step("Скачиваем документ 'Анкета физического лица'"):
            app.download_file_by_id(file_id=form_person_id, file_name='Анкета физического лица', user_id=setup_get_documents_from_product['user_id'], header=setup_get_documents_from_product['header'])
        with allure.step('Проверяем что в документе корректные ФИО, ИНН и серия номер паспорта'):
            with pdfplumber.open('documents_for_parse//Анкета физического лица.pdf') as pdf:
                first_page = pdf.pages[0]
                assert setup_get_documents_from_product['data_for_parse'][4] in first_page.extract_text(), f"Имя в шапке неверное, документ ={first_page.extract_text()}"
                assert setup_get_documents_from_product['data_for_parse'][5] in first_page.extract_text(), f"Фамилия в шапке неверная, документ ={first_page.extract_text()}"
                assert setup_get_documents_from_product['data_for_parse'][6] in first_page.extract_text(), f"Отчество в шапке неверное, документ ={first_page.extract_text()}"
                assert setup_get_documents_from_product['data_for_parse'][0] in first_page.extract_text(), f"ФИО в футере документа неверные, документ ={first_page.extract_text()}"
                assert str(setup_get_documents_from_product['data_for_parse'][2]['passport']['serial']) in first_page.extract_text(), f"Серия паспорта в шапке документа неверная, документ ={first_page.extract_text()}"
                assert str(setup_get_documents_from_product['data_for_parse'][2]['passport']['number']) in first_page.extract_text(), f"Номер паспорта в шапке документа неверный, документ ={first_page.extract_text()}"
                assert str(setup_get_documents_from_product['data_for_parse'][3]['inn']) in first_page.extract_text(), f"ИНН в шапке документа неверный, документ ={first_page.extract_text()}"
        with allure.step("TearDown! Удаляем скачанный файл по имени"):
            app.remove_file_by_name(abs_path='documents_for_parse//Анкета физического лица.pdf')

    @allure.feature('Проверка документа "Поручения на открытие счетов ДЕПО"')
    @allure.story('Подключение Продукта WhiteLabel 126 - Account/CreateConnectClientToProduct')
    @allure.description('В Setup создаем пользователя(перс. данные, документы), присоединяем его к Моревиль, подключаем продукт 126, скачиваем документ, проверяем что в нем корректные данные')
    @pytest.mark.integtest
    @flaky(max_runs=5, min_passes=1)
    def test_get_document_order_to_open_an_account(self, app, setup_get_documents_from_product, allure_env, base_env):
        with allure.step("Ищем документ 'Поручения на открытие счетов ДЕПО' по имени"):
            order_open_id = app.find_file_id_by_name(request=setup_get_documents_from_product['list_documents'], name='Поручения на открытие счетов ДЕПО')
        with allure.step("Скачиваем документ 'Поручения на открытие счетов ДЕПО'"):
            app.download_file_by_id(file_id=order_open_id, file_name='Поручения на открытие счетов ДЕПО', user_id=setup_get_documents_from_product['user_id'], header=setup_get_documents_from_product['header'])
        with allure.step('Проверяем что в документе корректные ФИО, ИНН и серия номер паспорта'):
            with pdfplumber.open('documents_for_parse//Поручения на открытие счетов ДЕПО.pdf') as pdf:
                full_fio = setup_get_documents_from_product['data_for_parse'][0].replace(' ', '')
                short_fio = setup_get_documents_from_product['data_for_parse'][1].replace(' ', '')
                first_page = pdf.pages[0]
                second_page = pdf.pages[1]
                third_page = pdf.pages[2]
                fourth_page = pdf.pages[3]
                assert full_fio in first_page.extract_text(), f"ФИО в шапке на 1 странице документа неверное, документ ={first_page.extract_text()}"
                assert short_fio in first_page.extract_text(), f"ФИО в футере на 1 странице документа неверная, документ ={first_page.extract_text()}"
                assert full_fio in second_page.extract_text(), f"ФИО в шапке на 2 странице документа неверное, документ ={second_page.extract_text()}"
                assert short_fio in second_page.extract_text(), f"ФИО в футере на 2 странице документа неверная, документ ={second_page.extract_text()}"
                assert full_fio in third_page.extract_text(), f"ФИО в шапке на 3 странице документа неверное, документ ={third_page.extract_text()}"
                assert short_fio in third_page.extract_text(), f"ФИО в футере на 3 странице документа неверная, документ ={third_page.extract_text()}"
                assert full_fio in fourth_page.extract_text(), f"ФИО в шапке на 4 странице документа неверное, документ ={fourth_page.extract_text()}"
                assert short_fio in fourth_page.extract_text(), f"ФИО в футере на 4 странице документа неверная, документ ={fourth_page.extract_text()}"
        with allure.step("TearDown! Удаляем скачанный файл по имени"):
            app.remove_file_by_name(abs_path='documents_for_parse//Поручения на открытие счетов ДЕПО.pdf')

    @allure.feature('Проверка документа "Заявление о получении доступа к Transaq Connector"')
    @allure.story('Подключение Продукта WhiteLabel 126 - Account/CreateConnectClientToProduct')
    @allure.description('В Setup создаем пользователя(перс. данные, документы), присоединяем его к Моревиль, подключаем продукт 126, скачиваем документ, проверяем что в нем корректные данные')
    @pytest.mark.integtest
    @flaky(max_runs=3, min_passes=1)
    def test_get_document_transaq_connector(self, app, setup_get_documents_from_product, allure_env, base_env):
        with allure.step("Ищем документ 'Заявление о получении доступа к Transaq Connector' по имени"):
            access_lk_id = app.find_file_id_by_name(request=setup_get_documents_from_product['list_documents'], name='Заявление о получении доступа к Transaq Connector')
        with allure.step("Скачиваем документ 'Заявление о получении доступа к Transaq Connector'"):
            app.download_file_by_id(file_id=access_lk_id, file_name='Заявление о получении доступа к Transaq Connector', user_id=setup_get_documents_from_product['user_id'], header=setup_get_documents_from_product['header'])
        with allure.step('Проверяем что в документе корректные ФИО и серия номер паспорта'):
            with pdfplumber.open('documents_for_parse//Заявление о получении доступа к Transaq Connector.pdf') as pdf:
                first_page = pdf.pages[0]
                assert setup_get_documents_from_product['data_for_parse'][0] in first_page.extract_text(), f"ФИО в шапке документа неверные, документ ={first_page.extract_text()}"
                assert setup_get_documents_from_product['data_for_parse'][1] in first_page.extract_text(), f"ФИО в футере документа неверные, документ ={first_page.extract_text()}"
                assert str(setup_get_documents_from_product['data_for_parse'][2]['passport']['serial']) in first_page.extract_text(), f"Серия паспорта в футере документа неверная, документ ={first_page.extract_text()}"
                assert str(setup_get_documents_from_product['data_for_parse'][2]['passport']['number']) in first_page.extract_text(), f"Номер паспорта в футере документа неверный, документ ={first_page.extract_text()}"
        with allure.step("TearDown! Удаляем скачанный файл по имени"):
            app.remove_file_by_name(abs_path='documents_for_parse//Заявление о получении доступа к Transaq Connector.pdf')





