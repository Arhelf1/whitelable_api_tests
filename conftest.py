import json
import time

import pytest
from application import Application
from data_for_tests.partner_auth import url_get_access
from protos.access_ import Access
from protos.session_pb2 import Session
from sql.config import *
from data_for_tests.account import *
from data_for_tests.auth import *
import pymssql
import lxml.etree
import requests
import os
fixture = None
from shutil import copyfile
from helpers import common
from russian_names import RussianNames
import allure


@pytest.fixture(scope="session")
def allure_env(tmpdir_factory):
    """Provide access to environment file."""
    env = tmpdir_factory.mktemp("allure").join("environment.xml")
    environment = lxml.etree.Element("environment")
    with open(env, "a") as env_xml:
        env_xml.write(lxml.etree.tounicode(environment, pretty_print=True))
    return str(env)


@pytest.fixture(scope="session", autouse=True)
def write_allure_env(request, allure_env):
    """Copy environment to alluredir."""
    yield
    alluredir = request.config.getoption("--alluredir")
    if alluredir != None:
        if os.path.isdir(alluredir):
            copyfile(allure_env, os.path.join(alluredir, "environment.xml"))


# -- Set default parametrs for run
def pytest_addoption(parser):
    parser.addoption("--base_url", action="store", default="http://wl-test-shared.entapp.work/v1/", help="Type base url of service like https://myservice.ru Default is http://wl-test-shared.entapp.work/")
    parser.addoption("--limit_time", action="store", default=500, help="Type time limit to requests. Default is 500")
    parser.addoption("--env", action="store", default="test", help="Type a environment. Default is Test")


@pytest.fixture(scope="session")
def base_env(request, allure_env):
    env = request.config.getoption("--env")
    if env == "test":
        common.set_env(allure_env, "Environment", "Test: http://wl-test-shared.entapp.work/v1/")


@pytest.fixture(scope="function")
def base_url(request):
    base_url = request.config.getoption("--base_url")
    return base_url


@pytest.fixture(scope="function")
def limit_time(request):
    limit_time = request.config.getoption("--limit_time")
    return limit_time


@pytest.fixture(scope="function")
def app(base_url, limit_time):
    global fixture
    fixture = Application(base_url, limit_time)
    return fixture


@pytest.fixture(scope='function')
def grpc_channel():
    from grpc import insecure_channel
    return insecure_channel


@pytest.fixture(scope='function')
def access_stub(grpc_channel):
    from protos.access_api_pb2_grpc import AccessApiStub
    return AccessApiStub(grpc_channel('msa-edot01-ap02:5555'))


@pytest.fixture(scope='function')
def reg_function(app, access_stub, db_cursor, get_access_token):
    registration_data = {'phone': app.get_random_tel(),
                         'email': app.random_email(),
                         'password': 'Vfhn2019',
                         }
    user_id = Access.registration(Access(), data=registration_data, stub=access_stub).user_id
    Access.confirm(Access(), user_id, access_stub)
    time.sleep(10)
    original = registration_data['phone']
    phone = original.replace("+", "")
    response = requests.request("POST", url="https://txdev.finam.ru/grpc-json/txauth/v3/auth/EDO_DEV/" + phone, headers=auth_headers, data=data)
    token = response.json()['token']
    payload = token.split('.')[1]
    parse = json.loads(app.base64decode(payload))
    session = parse["sess"]
    create_session = Session()
    if parse["zipped"]:
        session = app.decompress(app.base64encode(session))
        create_session.ParseFromString(session)
    auth_id = create_session.authentication_id
    db_cursor['db_cursor'].execute(f"""
            INSERT INTO dbo.Clients (GlobalId, AuthId, PartnerId)
            VALUES ('{user_id}', '{auth_id}', '{PartnerId}')
            """)
    db_cursor['conn'].commit()
    access_token = get_access_token['Partner-Authorization']
    header_json = {
        'Content-Type': 'application/json',
        'Partner-Authorization': access_token,
        'Authorization': 'Bearer ' + token
    }
    header_file = {
        'Partner-Authorization': access_token,
        'Authorization': 'Bearer ' + token
    }
    my_d = {
        'user_id': user_id,
        'phone': phone,
        'header': header_json,
        'header_f': header_file,
        'auth_id': auth_id
    }
    return my_d


@pytest.fixture()
def setup_set_identity_documents(reg_function, get_personal_data, app):
    with allure.step("Добавляем пользователю паспорт"):
        old_passport_data = app.get_passport_data(user_id=reg_function['user_id'])
        app.post_request(url_get_passport, data=old_passport_data,
                     headers=reg_function['header'], result=False)
    with allure.step("Добавляем пользователю ИНН"):
        old_inn_data = app.get_inn_data(user_id=reg_function['user_id'])
        app.post_request(url_get_inn, data=old_inn_data,
                     headers=reg_function['header'], result=False)
    with allure.step("Добавляем пользователю СНИЛС"):
        old_snils_data = app.get_snils_data(user_id=reg_function['user_id'])
        app.post_request(url_get_snils, data=old_snils_data, headers=reg_function['header'])
    with allure.step("Готовим данные для тестового метода"):
        data = app.get_set_identity_documents_data(user_id=reg_function['user_id'])
    return data


@pytest.fixture()
def get_personal_data(reg_function, app):
    str_fio = RussianNames(gender=1).get_person()
    name, middle, last = str_fio.split()
    str_fio = last + " " + name + " " + middle
    short_fio = f'{last} {name[0]}.{middle[0]}.'.format(**vars())
    personal_info_data = {
        "personalInfo": {
            "gender": "Male",
            "firstName": name,
            "lastName": last,
            "middleName": middle,
            "dateOfBirth": "1999-02-19",
            "citizenship": "RUS"
        },
        "userId": reg_function['user_id']
    }
    app.post_request(url_get_personal_info, data=personal_info_data, headers=reg_function['header'], result=False)


@pytest.fixture()
def setup_create_connect_client_to_product(reg_function, app):
    str_fio = RussianNames(gender=1).get_person()
    name, middle, last = str_fio.split()
    str_fio = last + " " + name + " " + middle
    short_fio = f'{last} {name[0]}.{middle[0]}.'.format(**vars())
    personal_info_data = {
        "personalInfo": {
            "gender": "Male",
            "firstName": name,
            "lastName": last,
            "middleName": middle,
            "dateOfBirth": "1999-02-19",
            "citizenship": "RUS"
        },
        "userId": reg_function['user_id']
    }
    app.post_request(url_get_personal_info, data=personal_info_data, headers=reg_function['header'], result=False)
    passport_data = app.get_passport_data(user_id=reg_function['user_id'])
    app.post_request(url_get_passport, data=passport_data,
                     headers=reg_function['header'], result=False)
    inn_data = app.get_inn_data(user_id=reg_function['user_id'])
    app.post_request(url_get_inn, data=inn_data,
                     headers=reg_function['header'], result=False)
    address_data = {
        "fiasId": "8b567ec2-69f5-4d7d-b88a-86ea4942f288",
        "addressType": "Registration",
        "cityArea": "",
        "planStruct": "",
        "street": "Политехническая",
        "stead": "",
        "house": "6",
        "part": "",
        "building": "",
        "flat": '777',
        "postalCode": "194021",
        "userId": reg_function['user_id']}
    response = app.post_request(url_get_address, data=address_data, headers=reg_function['header'])
    assert response.text == '"Success"', f"Адрес не добавлен, из-за {response.text}"
    address_data = {
        "fiasId": "8b567ec2-69f5-4d7d-b88a-86ea4942f288",
        "addressType": "Actual",
        "cityArea": "",
        "planStruct": "",
        "street": "Политехническая",
        "stead": "",
        "house": "6",
        "part": "",
        "building": "",
        "flat": '777',
        "postalCode": "194021",
        "userId": reg_function['user_id']
    }
    response = app.post_request(url_get_address, data=address_data, headers=reg_function['header'])
    assert response.text == '"Success"', f"Адрес не добавлен, из-за {response.text}"
    response = app.post_request(url_get_create_sms_sign, data={'userId': reg_function['user_id']},
                                headers=reg_function['header'])
    file_id_asp = response.json()[0]['FileId']
    document_id_asp = response.json()[0]['Id']
    data = {
        "documentIds": [document_id_asp],
        "userId": reg_function["user_id"]
    }
    response = app.post_request(url_get_sign_sms_sign, data=data, headers=reg_function['header'])
    data = {
        "id": response.json()['Id'],
        "userId": reg_function['user_id'],
        "code": "000000"
    }
    app.post_request(url_confirm_sms_sign, data=data,
                     headers=reg_function["header"], result=False)
    result = {"header": reg_function['header'],
              "user_id": reg_function['user_id'],
              "fio": str_fio}
    return result


@pytest.fixture()
def setup_get_document_asp(reg_function, app):
    passport_data = app.get_passport_data(user_id=reg_function['user_id'])
    app.post_request(url_get_passport, data=passport_data,
                     headers=reg_function['header'], result=False)
    inn_data = app.get_inn_data(user_id=reg_function['user_id'])
    app.post_request(url_get_inn, data=inn_data,
                     headers=reg_function['header'], result=False)
    str_fio = RussianNames(gender=1).get_person()
    name, middle, last = str_fio.split()
    str_fio = last + " " + name + " " + middle
    short_fio = f'{last} {name[0]}.{middle[0]}.'.format(**vars())
    personal_info_data = {
        "personalInfo": {
            "gender": "Male",
            "firstName": name,
            "lastName": last,
            "middleName": middle,
            "dateOfBirth": "1992-02-19",
            "citizenship": "RUS"
        },
        "userId": reg_function['user_id']
    }
    app.post_request(url_get_personal_info, data=personal_info_data, headers=reg_function['header'], result=False)
    address_data = {
        "kladrId": "c2deb16a-0330-4f05-821f-1d09c93331e6",
        "addressType": "Registration",
        "cityArea": app.get_random_city(),
        "planStruct": "город",
        "street": "Тверская",
        "stead": app.get_random_number(1),
        "house": app.get_random_number(2),
        "part": app.get_random_number(1),
        "building": app.get_random_number(1),
        "flat": app.get_random_number(1),
        "postalCode": app.get_random_number(7),
        "userId": reg_function['user_id']
    }
    app.post_request(url_get_address, data=address_data, headers=reg_function['header'], result=False)
    response = app.post_request(url_get_create_sms_sign, data={'userId': reg_function['user_id']},
                                headers=reg_function['header'])
    file_id_asp = response.json()[0]['FileId']
    document_id_asp = response.json()[0]['Id']
    result = {
        'data_for_parse': [str_fio, short_fio, passport_data, inn_data, name, middle, last],
        'data_for_request': {'fileId': file_id_asp,
                             'userId': reg_function['user_id']},
        'header': reg_function['header'],
        'document_id': document_id_asp
    }
    return result


@pytest.fixture()
def setup_get_documents_from_product(app, setup_get_document_asp):
    response = app.post_request(url_get_sign_sms_sign, data={'documentIds': [setup_get_document_asp['document_id']],
                                                  'userId': setup_get_document_asp['data_for_request']['userId']}, headers=setup_get_document_asp['header'])
    id_confirm = response.json()['Id']
    response = app.post_request(url_confirm_sms_sign, data={"id": id_confirm,
                                                            "userId": setup_get_document_asp['data_for_request']['userId'],
                                                            "code": "333222"}, headers=setup_get_document_asp['header'])
    data = {
        "productId": 126,
        "userId": setup_get_document_asp['data_for_request']['userId']
    }
    response = app.post_request(url_create_connect_client_to_product, data=data,
                                headers=setup_get_document_asp['header'])
    list_documents = response.json()
    result = {
        'data_for_parse': setup_get_document_asp['data_for_parse'],
        'list_documents': list_documents,
        'header': setup_get_document_asp['header'],
        'user_id': data['userId']
    }
    return result


@pytest.fixture()
def setup_sign_connect_client_to_product(setup_create_connect_client_to_product, app):
    data = {
        "productId": 126,
        "userId": setup_create_connect_client_to_product['user_id']
    }
    response = app.post_request(url_create_connect_client_to_product, data=data,
                                headers=setup_create_connect_client_to_product['header'])
    result = response.json()
    documents_id = []
    for el in result:
        id = el['Id']
        documents_id.append(id)
    result = {"data": {
        "documentIds": documents_id,
        "userId": setup_create_connect_client_to_product['user_id']},
        "header": setup_create_connect_client_to_product['header']
    }
    return result


@pytest.fixture()
def setup_confirm_connect_client(app, setup_sign_connect_client_to_product):
    response = app.post_request(url_sign_connect_client_to_product, data=setup_sign_connect_client_to_product['data'],
                                headers=setup_sign_connect_client_to_product['header'])

    id = response.json()['Id']
    result = {"data": {
        "id": id,
        "userId": setup_sign_connect_client_to_product['data']['userId'],
        "code": "123321"},
        "header": setup_sign_connect_client_to_product['header']
    }
    return result


@pytest.fixture()
def setup_get_product_statuses(reg_function, app):
    str_fio = RussianNames(gender=1).get_person()
    name, middle, last = str_fio.split()
    str_fio = last + " " + name + " " + middle
    short_fio = f'{last} {name[0]}.{middle[0]}.'.format(**vars())
    personal_info_data = {
        "personalInfo": {
            "gender": "Male",
            "firstName": name,
            "lastName": last,
            "middleName": middle,
            "dateOfBirth": "1999-02-19",
            "citizenship": "RUS"
        },
        "userId": reg_function['user_id']
    }
    app.post_request(url_get_personal_info, data=personal_info_data, headers=reg_function['header'], result=False)
    app.post_request(url_get_passport, data=app.get_passport_data(user_id=reg_function['user_id']),
                     headers=reg_function['header'], result=False)
    app.post_request(url_get_snils, data=app.get_snils_data(user_id=reg_function['user_id']),
                     headers=reg_function['header'], result=False)
    app.post_request(url_get_inn, data=app.get_inn_data(user_id=reg_function['user_id']),
                     headers=reg_function['header'], result=False)
    address_data = {
        "fiasId": "8b567ec2-69f5-4d7d-b88a-86ea4942f288",
        "addressType": "Registration",
        "cityArea": "",
        "planStruct": "",
        "street": "Политехническая",
        "stead": "",
        "house": "6",
        "part": "",
        "building": "",
        "flat": '777',
        "postalCode": "194021",
        "userId": reg_function['user_id']}
    response = app.post_request(url_get_address, data=address_data, headers=reg_function['header'])
    assert response.text == '"Success"', f"Адрес не добавлен, из-за {response.text}"
    address_data = {
        "fiasId": "8b567ec2-69f5-4d7d-b88a-86ea4942f288",
        "addressType": "Actual",
        "cityArea": "",
        "planStruct": "",
        "street": "Политехническая",
        "stead": "",
        "house": "6",
        "part": "",
        "building": "",
        "flat": '777',
        "postalCode": "194021",
        "userId": reg_function['user_id']
    }
    response = app.post_request(url_get_address, data=address_data, headers=reg_function['header'])
    response = app.post_request(url_get_create_sms_sign, data={'userId': reg_function['user_id']},
                                headers=reg_function['header'])
    result = response.json()[0]
    data = {
        "documentIds": [result["Id"]],
        "userId": reg_function["user_id"]
    }
    response = app.post_request(url_get_sign_sms_sign, data=data, headers=reg_function['header'])
    data = {
        "id": response.json()['Id'],
        "userId": reg_function['user_id'],
        "code": "000000"
    }
    app.post_request(url_confirm_sms_sign, data=data,
                                headers=reg_function["header"], result=False)
    data = {
        "productId": 126,
        "userId": reg_function['user_id']
    }
    response = app.post_request(url_create_connect_client_to_product, data=data,
                                headers=reg_function['header'])
    result = response.json()
    documents_id = []
    for el in result:
        id = el['Id']
        documents_id.append(id)
    data = {
        "documentIds": documents_id,
        "userId": reg_function['user_id']}
    response = app.post_request(url_sign_connect_client_to_product, data=data,
                                headers=reg_function['header'])
    data = {
        "id": response.json()['Id'],
        "userId": reg_function['user_id'],
        "code": "000000"
    }
    app.post_request(url_confirm_connect, data=data,
                                headers=reg_function['header'], result=False)
    result = {
        'data': {
            "userId": reg_function['user_id']
        },
        'header': reg_function['header'],
        'header_f': reg_function['header_f'],
        'documents_to_sign': documents_id
    }
    return result


@pytest.fixture()
def setup_get_documents_files(app, setup_get_product_statuses):
    documents = setup_get_product_statuses['documents_to_sign']
    document_id = documents[0]
    results = {
        'data': {
        'documentId': document_id,
        'userId': setup_get_product_statuses['data']['userId']},
        'header': setup_get_product_statuses['header'],
        'header_f': setup_get_product_statuses['header_f']
    }
    return results


@pytest.fixture()
def setup_get_file_content(app, setup_get_documents_files):
    response = app.post_request(url_get_documents_files, data=setup_get_documents_files['data'], headers=setup_get_documents_files['header'])
    file_id = response.json()[0]['Id']
    result = {
        'data': {
                "fileId": file_id,
                "userId": setup_get_documents_files['data']['userId']
        },
        'header': setup_get_documents_files['header']
    }
    return result


@pytest.fixture()
def db_cursor():
    conn = pymssql.connect(database=database, server=server, user=username, password=password, charset='UTF-8',
                           as_dict=True)
    db_cursor = conn.cursor()
    db_dict = {
        'conn': conn,
        'db_cursor': db_cursor
    }
    yield db_dict
    conn.close()


@pytest.fixture()
def user_id(app, get_access_token):
    registration_data = {
        "client": {
            "email": app.random_email(),
            "phone": app.get_random_tel()
        },
        "consentToPersonalDataProcessing": True,
        "consentToOfferForProvidingInformationServices": True,
        "ip": "2001:db8:3333:4444:5555:6666:1.2.3.4",
        "device": "ios"
    }
    response = app.post_request(url_registation, data=registration_data, headers=get_access_token)
    user_id = response.json()["UserId"]
    return user_id


@pytest.fixture()
def setup_create_sms_sign(app, reg_function):
    data = {
        "userId": reg_function['user_id']
    }
    str_fio = RussianNames(gender=1).get_person()
    name, middle, last = str_fio.split()
    personal_info_data = {
        "personalInfo": {
            "gender": "Male",
            "firstName": name,
            "lastName": last,
            "middleName": middle,
            "dateOfBirth": "1999-02-19",
            "citizenship": "RUS"
        },
        "userId": reg_function['user_id']
    }
    app.post_request(url_get_personal_info, data=personal_info_data, headers=reg_function['header'], result=False)
    app.post_request(url_get_passport, data=app.get_passport_data(user_id=reg_function['user_id']),
                     headers=reg_function['header'], result=False)
    app.post_request(url_get_inn, data=app.get_inn_data(user_id=reg_function['user_id']),
                     headers=reg_function['header'], result=False)
    app.post_request(url_get_snils, data=app.get_snils_data(user_id=reg_function['user_id']),
                     headers=reg_function['header'], result=False)
    address_data = {
        "fiasId": "8b567ec2-69f5-4d7d-b88a-86ea4942f288",
        "addressType": "Registration",
        "cityArea": "",
        "planStruct": "",
        "street": "Политехническая",
        "stead": "",
        "house": "6",
        "part": "",
        "building": "",
        "flat": '777',
        "postalCode": "194021",
        "userId": reg_function['user_id']}
    response = app.post_request(url_get_address, data=address_data, headers=reg_function['header'])
    assert response.text == '"Success"', f"Адрес не добавлен, из-за {response.text}"
    address_data = {
        "fiasId": "8b567ec2-69f5-4d7d-b88a-86ea4942f288",
        "addressType": "Actual",
        "cityArea": "",
        "planStruct": "",
        "street": "Политехническая",
        "stead": "",
        "house": "6",
        "part": "",
        "building": "",
        "flat": '777',
        "postalCode": "194021",
        "userId": reg_function['user_id']
    }
    response = app.post_request(url_get_address, data=address_data, headers=reg_function['header'])
    result = {
        "data": data,
        "header": reg_function['header'],
        "user_id": reg_function['user_id']
        }
    return result


@pytest.fixture()
def setup_sign_sms_sign(app, setup_create_sms_sign):
    response = app.post_request(url_get_create_sms_sign, data=setup_create_sms_sign["data"], headers=setup_create_sms_sign['header'])
    id = response.json()[0]["Id"]
    result = {
        "header": setup_create_sms_sign['header'],
        "id": id,
        "user_id": setup_create_sms_sign['user_id']
    }
    return result


@pytest.fixture()
def setup_sign_sms_confirm(app, setup_sign_sms_sign):
    data = {
        "documentIds": [setup_sign_sms_sign["id"]],
        "userId": setup_sign_sms_sign["user_id"]
    }
    response = app.post_request(url_get_sign_sms_sign, data=data, headers=setup_sign_sms_sign['header'])
    result = {
        "header": setup_sign_sms_sign["header"],
        "data": {
            "Id": response.json()["Id"],
            "UserId": response.json()["UserId"],
            "code": "000000"
        }
    }
    return result


@pytest.fixture()
def get_data_reg(app):
    import random
    data = {
            "client": {
                "email": app.random_email(),
                "phone": app.get_random_tel()
            },
        "consentToPersonalDataProcessing": True,
        "consentToOfferForProvidingInformationServices": True,
        "ip": ".".join(map(str, (random.randint(0, 255) for _ in range(4)))),
        "device": "web-chrome"
    }
    return data


@pytest.fixture(scope="function", params=('Novgorod_Niznii', 'Astrahan_lenina', 'Karachev_pushkin'))
def get_data_address(request, reg_function):
    data = {
        "fiasId": data_for_address[request.param][0],
        "addressType": data_for_address[request.param][10],
        "cityArea": data_for_address[request.param][1],
        "planStruct": "город",
        "street": data_for_address[request.param][2],
        "stead": data_for_address[request.param][3],
        "house": data_for_address[request.param][4],
        "part": data_for_address[request.param][5],
        "building": data_for_address[request.param][6],
        "flat": data_for_address[request.param][7],
        "postalCode": data_for_address[request.param][8],
        "userId": reg_function['user_id']
    }
    return data


@pytest.fixture(scope="function", params=('Bash', 'Bel_mayk'))
def get_custom_data_address(request, reg_function):
    data = {
        "customAddress": data_for_custom_address[request.param][0],
        "addressType": data_for_custom_address[request.param][1],
        "countryId": 1,
        "userId": reg_function['user_id']
    }
    return data


@pytest.fixture(scope="function", params=('dmitriy', 'nastya', 'leon'))
def get_personal_info(request, reg_function):
    data = {
        "response": {"userId": reg_function['user_id'],
            "personalInfo": {
            "gender": data_for_personal_info[request.param][0],
            "firstName": data_for_personal_info[request.param][1],
            "lastName": data_for_personal_info[request.param][2],
            "middleName": data_for_personal_info[request.param][3],
            "dateOfBirth": data_for_personal_info[request.param][4],
            "citizenship": data_for_personal_info[request.param][5]
        }
    }, "request": {
        "Gender": data_for_personal_info[request.param][6],
        "FirstName": data_for_personal_info[request.param][1],
        "LastName": data_for_personal_info[request.param][2],
        "MiddleName": data_for_personal_info[request.param][3],
        "DateOfBirth": data_for_personal_info[request.param][4],
        "Citizenship": data_for_personal_info[request.param][5]
    }}
    return data


@pytest.fixture()
def setup_get_access_token():
    response = requests.request("POST", url_refresh_finam2, headers={}, data={})
    body = {
        'RefreshToken': response.text,
        'AccessToken': ""
    }
    return body


@pytest.fixture()
def new_refresh_token():
    response = requests.request("POST", url_refresh, headers={}, data={})
    return response


def new_access_token():
    response = requests.request("POST", url_refresh, headers={}, data={})
    refresh_token = response.text
    body = json.dumps({
        "RefreshToken": refresh_token,
        "AccessToken": ""
    })
    response = requests.request("POST", full_url_access, data=body, headers=auth_headers)
    access_token = response.json()['AccessToken']

    headers = {
        'Content-Type': 'application/json',
        'Partner-Authorization': access_token
    }
    return headers


@pytest.fixture(scope='session')
def get_access_token(tmp_path_factory, worker_id, name="new_access_token"):
    from filelock import FileLock
    if not worker_id:
        return new_access_token()
    root_tmp_dir = tmp_path_factory.getbasetemp().parent
    fn = root_tmp_dir / "data.json"
    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            data = json.loads(fn.read_text())
        else:
            data = new_access_token()
            fn.write_text(json.dumps(data))
    return data