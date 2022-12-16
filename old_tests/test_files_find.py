import allure
import pytest
import requests
from data_for_tests.files_find import *
from helpers.common import validate_schema, response_status


@allure.feature('White Label API: Files')
class TestFiles:

    @pytest.allure.BLOCKER
    def test_files_attach(self, app):

        # /Files/Attach
        files_attach = app.post_request(url_file_attach, get_body_attach(user, document), headers=app.token())
        response_status(files_attach, url_file_attach)
        files_attach_data = files_attach.json()
        assert len(files_attach_data) > 0, logger(key='files_attach_len')
        validate_schema(app, files_attach_data, path_to_files_attach)

        document_id = files_attach_data[0]['documentId']
        name = files_attach_data[0]['name']
        id_attach = files_attach_data[0]['id']

        assert document_id == document, logger(key='documentId', left=document_id, right=document)
        assert name == jpeg_name, logger(key='name', left=name, right=jpeg_name)
        assert id_attach > 0, logger(key='id', left=id_attach)

        # проверка что файл прикрепился через вызов Files/FindByDoc
        check_doc = app.post_request(url_find_by_doc, get_body_by_doc(user, (document,)), headers=app.token())
        assert check_doc.status_code == requests.codes.ok
        check_doc_data = check_doc.json()
        assert len(check_doc_data) > 0, logger(key='attach_check')

        check_document_id, check_id = app.models.files.get_response_data(check_doc_data)
        _document_id, _id = app.models.files.get_response_data(files_attach_data)

        assert app.models.v2_registration.validate_ids(check_document_id, _document_id)
        assert app.models.v2_registration.validate_ids(check_id, _id)
        assert app.models.files.validate_file_data(check_doc_data)

    @pytest.allure.BLOCKER
    def test_files_find(self, app):

        # Вызов /Files/Attach для  получения  "id": 96407173
        files_attach = app.post_request(url_file_attach, get_body_attach(user, document), headers=app.token())
        assert files_attach.status_code == requests.codes.ok
        files_attach_data = files_attach.json()
        assert len(files_attach_data) > 0, logger(key='len')

        id_attach = files_attach_data[0]['id']

        # /Files/Find
        files_find = app.post_request(url_files_find, get_body_find(user, (id_attach, )), headers=app.token())
        response_status(files_find, url_files_find)
        files_find_data = files_find.json()
        assert len(files_find_data) > 0, logger(key='files_find_len')
        validate_schema(app, files_find_data, path_to_files_find)
        assert len(files_find_data[0]['data']) > 0, logger(key='data')
        assert files_find_data[0]['id'] == id_attach, logger(key='files_find_id')

    @pytest.allure.BLOCKER
    def test_files_find_by_doc(self, app):
        # /Files/FindByDoc
        # посылаем список documentId, в ответе приходят data - (файл в base64), его id и documentId и тд.
        find_by_doc = app.post_request(url_find_by_doc, get_body_by_doc(user, (document,)), headers=app.token())
        response_status(find_by_doc, url_find_by_doc)
        find_by_doc_data = find_by_doc.json()
        assert len(find_by_doc_data) > 0, 'Files/FindByDoc вернул пустой список данных.'
        validate_schema(app, find_by_doc_data, path_to_files_find)
        assert app.models.quotes.validate_all(field_list, find_by_doc_data)
        assert app.models.files.validate_file_data(find_by_doc_data)
