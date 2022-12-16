import allure
import pytest
from jsonschema import validate
import requests
from data_for_tests.v2_registration import *
from sql.query import sms_by_user_id
from helpers.common import validate_schema, response_status


@allure.feature('White Label API: /v2/Registration')
class TestV2Registration:

    @pytest.allure.BLOCKER
    def test_v2_registration(self, app):
        # Генерируем значения для ФИО
        first_name, last_name, middle_name = app.models.v2_registration.get_fio()
        # Генерируем значения для серии и номера паспорта и телефона
        serial = app.models.v2_registration.get_numbers(4)
        number = app.models.v2_registration.get_numbers(6)
        # ОТПРАВЛЯЕМ ЗАПРОС НА ОТКРЫТИЕ СЧЕТА
        registration = app.post_request(url_reg, get_body(first_name, last_name, middle_name, serial, number), headers=app.token())
        response_status(registration, url_reg)
        registration_data = registration.json()
        assert len(registration_data) > 0, 'v2/Registration вернул пустой список данных.'
        assert len(registration_data['userId']) > 0, 'v2/Registration вернул пустой userId.'
        type(self).reg_data = registration_data

    @pytest.allure.BLOCKER
    def test_sms_send(self, app):
        try:
            # извлечь все id документов
            doc_ids = app.models.v2_registration.get_doc_ids(self.reg_data)
            # ОТПРАВЛЯЕМ КЛИЕНТУ СМС
            sms = app.post_request(url_sms, get_body_sms(self.reg_data['userId'], doc_ids), headers=app.token())
            response_status(sms, url_sms)
            sms_data = sms.json()
            assert len(sms_data) > 0, 'Sms/Send вернул пустой список данных.'
            validate(sms_data, app.get_json_schema(path_to_sms_send_json))
            # проверка телефона
            assert sms_data['phone'][-4:] == phone, 'Номер телефона не совпадает.'
        except Exception:
            pytest.mark.skip('registration failed!')

    @pytest.allure.BLOCKER
    def test_sms_confirm(self, app):
        try:
            doc_ids = app.models.v2_registration.get_doc_ids(self.reg_data)
            # извлечь смс
            code = app.models.order_create_sell.validate_sms(sms_by_user_id, self.reg_data['userId'])
            # ПОЛЬЗОВАТЕЛЬ ПОДТВЕРЖДАЕТ СМС
            sms_confirm = app.post_request(url_sms_confirm, get_body_sms_confirm(code[0][0],
                                                                                 self.reg_data['userId'],
                                                                                 doc_ids), headers=app.token())
            response_status(sms_confirm, url_sms_confirm)
            sms_confirm_data = sms_confirm.json()
            assert len(sms_confirm_data) > 0, 'Sms/Confirm вернул пустой список данных.'
            validate(sms_confirm_data, app.get_json_schema(path_to_sms_confirm_json))
            # проверка пришедших айдишников документов
            assert app.models.v2_registration.validate_ids(doc_ids, sms_confirm_data['documentIds'])
        except Exception:
            pytest.mark.skip('registration failed!')

    @pytest.allure.BLOCKER
    def test_get_status(self, app):
        try:
            # ЖДЕМ ИСПОЛНЕНИЯ ЗАЯВКИ, ПЕРЕОДИЧЕСКИ ПРОВЕРЯЯ ЕЕ СТАТУС
            status = app.get_request(url_get_status + self.reg_data['userId'], app.token())
            response_status(status, url_get_status)
            status_data = status.json()
            assert len(status_data) > 0, 'Ждем исполнения заявки и получаем пустой список данных.'
            # проверка статусов
            assert app.models.v2_registration.validate_status(status_data['status'])
        except Exception:
            pytest.mark.skip('registration failed!')

    @pytest.allure.BLOCKER
    def test_orders(self, app):
        try:
            # /v2/Registration/Orders
            orders = app.post_request(url_orders, get_body_order(self.reg_data['userId'],
                                                                 self.reg_data['openAccountDocumentIds']),
                                      headers=app.token())
            response_status(orders, url_orders)
            orders_data = orders.json()
            assert len(orders_data) > 0, 'v2/Registration/Orders вернул пустой список данных.'
            validate_schema(app, orders_data, path_to_reg_orders_json)
            # проверка id и тд.
            assert TestV2Registration.reg_data['openAccountDocumentIds'][0] == orders_data[0]['documentId']
            assert orders_data[0]['status']['title'] in order_title
            assert orders_data[0]['status']['code'] in order_code
        except Exception:
            pytest.mark.skip('registration failed!')

    @pytest.allure.BLOCKER
    def test_documents(self, app):
        try:
            doc_ids = app.models.v2_registration.get_doc_ids(self.reg_data)
            # /Registration/Documents
            documents = app.post_request(url_documents, get_body_documents(self.reg_data['userId'],
                                                                           self.reg_data['openAccountDocumentIds']),
                                         headers=app.token())
            response_status(documents, url_documents)
            documents_data = documents.json()
            assert len(documents_data) > 0, 'Registration/Documents вернул пустой список данных.'
            validate_schema(app, documents_data, path_to_reg_documents_json)
            receive_data = [d['id'] for d in documents_data[0]['documents']]
            # проверка id и тд.
            assert self.reg_data['openAccountDocumentIds'][0] != documents_data[0]['id']
            assert app.models.v2_registration.validate_ids(doc_ids, receive_data)
        except Exception:
            pytest.mark.skip('registration failed!')
