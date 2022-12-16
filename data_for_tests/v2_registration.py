url_reg = 'v2/Registration'
url_sms = 'Sms/Send'
url_sms_confirm = 'Sms/Confirm'
url_get_status = 'Registration/GetStatus/?userId='
url_orders = 'v2/Registration/Orders'
url_documents = 'Registration/Documents'

path_to_json = 'json_schemes/registration.json'
path_to_sms_send_json = 'json_schemes/sms_send.json'
path_to_sms_confirm_json = 'json_schemes/sms_confirm.json'
path_to_reg_orders_json = 'json_schemes/reg_orders.json'
path_to_reg_documents_json = 'json_schemes/reg_documents.json'

# response list
order_title = ['Получено системой ЭДО', 'Ожидает']
order_code = ['Received', 'Waiting']

# client phone number
phone = '5894'

# client registration status
status_list = ['EXECUTED', 'PROCESS']

# user data.
alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О',
            'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']


# documents body
def get_body_documents(user_id, document_id):
    return {
        "UserId": user_id,
        "Ids": document_id
    }


# order body
def get_body_order(user_id, document_id):
    return {
        "UserId": user_id,
        "Ids": document_id,
        "DateBegin": "",
        "DateEnd": "",
        "From": "",
        "TakeCount": "",
        "Sort": ""
    }


# sms send body data
def get_body_sms(user_id, document_ids_list):
    return {
        "OperationType": 0,
        "UserId": user_id,
        "DocumentIds": document_ids_list
    }


# sms confirmation body data
def get_body_sms_confirm(sms, user_id, document_ids_list):
    return {
        "Code": sms,
        "UserId": user_id,
        "DocumentIds": document_ids_list
    }


# registration body data
def get_body(first_name, last_name, middle_name, serial=4016, number=456523):
    return {
            "LastName": last_name,
            "FirstName": first_name,
            "MiddleName": middle_name,
            "GenderCode": "F",
            "Birthdate": "1987-11-02 04:00:00Z",
            "BirthPlace": "г. Москва",
            "CitizenshipCode": [{"Code": "RUS"}],
            "Inn": "500100732259",
            "Snils": "112-233-445 95",
            "Addresses": [{
                "TypeCode": "REGISTRATION",
                "CountryCode": {"Code": "RUS"},
                "Region": "Ленинградская область",
                "Area": "Всеволожский р-н",
                "City": "деревня Кудрово",
                "PlanStructCode": "мкр Новый Оккервиль",
                "PlanStruct": "",
                "Stead": "",
                "PostalIndex": "127643"
            },
                {
                    "TypeCode": "FACTUAL",
                    "CountryCode": {
                        "Code": "RUS"
                    },
                    "Region": "Тульская, Область",
                    "Area": "Данковский, Район",
                    "City": "Данков, Город",
                    "Street": "Совхозная, Улица",
                    "House": "10",
                    "Part": "1",
                    "Room": "22",
                    "PostalIndex": "399854"
                },
                {
                    "TypeCode": "POSTAL",
                    "CountryCode": {
                        "Code": "RUS"
                    },
                    "RegionCode": 48,
                    "Region": "Липецкая, Область",
                    "AreaCode": 201,
                    "Area": "Данковский, Район",
                    "CityCode": 405,
                    "City": "Данков, Город",
                    "StreetCode": 529,
                    "Street": "Совхозная, Улица",
                    "House": "10",
                    "Part": "1",
                    "Room": "22",
                    "PostalIndex": "399854"
                }],
            "IdentityDocuments": [{
                "TypeCode": "PSRF",
                "Serial": serial,
                "Number": number,
                "IssueDate": "2002-02-24 00:00:00Z",
                "IssueId": "117-451",
                "IssuedBy": "ОВД г. Москва"
            }],
            "Contacts": {
                "Emails": [{
                    "TypeCode": "PERSONALEMAIL",
                    "Value": "Vsemau2@mail.ru",
                    "Verified": 'true'
                }],
                "Phones": [{
                    "TypeCode": "SMSPHONE",
                    "CountryCode": "7",
                    "PhoneCode": "824",
                    "Number": "9262625894",
                    "Verified": 'true'
                }]
            },
            "Scans": [
                "SGVsbG8=",
                "V29ybGQ=",
                "0KLQtdGB0YLQvtCy0YvQuSDQutC+0L3RgtC10L3Rgg=="
            ]
    }
