import os


url_get_securities = 'Account/GetSecurities/?userId='
url_security_settings = 'Account/SecuritySettings'
url_registation = 'Account/Register'
url_register_confirm = 'Account/RegisterConfirm'
url_is_registered = 'Account/isRegistered'
url_get_passport = 'Account/AddIdentityDocument'
url_get_inn = 'Account/AddInn'
url_get_snils = 'Account/AddSnils'
url_set_identity_documents = 'Account/ResetIdentityDocuments'
url_get_address = 'Account/SetUserAddress'
url_get_custom_address = 'Account/SetNonResidentAddress'
url_get_personal_info = 'Account/UpdatePersonalInfo'
url_get_create_sms_sign = 'Account/CreateSmsSignAgreement'
url_get_sign_sms_sign = 'Account/SignSmsSignAgreement'
url_confirm_sms_sign = "Account/ConfirmSmsSignAgreement"
url_create_connect_client_to_product = 'Account/CreateConnectClientToProduct'
url_sign_connect_client_to_product = 'Account/SignConnectClientToProduct'
url_confirm_connect = 'Account/SmsSignConnectClientToProduct'
url_add_passport_scans = 'Account/AddPassportScans'
path_to_client_schema = 'json_schemes/client_schema.json'
path_to_passport_schema = 'json_schemes/passport.json'
path_to_inn_schema = 'json_schemes/inn.json'
path_to_snils_schema = 'json_schemes/snils.json'
path_to_reset_documents_schema = 'json_schemes/reset_identity_documents.json'
path_to_personal_info_schema = 'json_schemes/personal_info.json'
path_to_create_sms_sign_schema = 'json_schemes/create_sms_sign.json'
path_to_sign_sms_sign_schema = 'json_schemes/sign_sms_sign_agreement.json'
path_confirm_sms_sign_schema = 'json_schemes/confirm_sms_sign_schema.json'
path_to_create_connect_client_to_product_schema = 'json_schemes/create_connect_client_to_product.json'
path_to_sign_connect_client_to_product_schema = 'json_schemes/sign_connect_client_to_product.json'
path_to_confirm_connect = 'json_schemes/confirm_client_to_product.json'
user_is_registered = {
"email": "iv5dd@yandex.ru",
"phone": "+79775987914"
}
headers = {
'Content-Type': 'application/json',
}
tiker_id = 'code'
board_id = 'board'

approved_quotes = ['AAPL', 'SBER']
approved_exchanges = ['MCT', 'TQBR']

path_to_security_settings_json = 'json_schemes/security_settings.json'
path_to_get_securities_json = 'json_schemes/get_securities.json'
PartnerId = 4

documents_create_connect_client_to_product = ["Статус физического лица", "Заявление о получении доступа к TRANSAQ", "Копия паспорта", "Заявка CRM", "Сведения о связанных лицах", "Заявление о присоединении к Деп. договору",
                                              "Заявление о присоединении к регламенту", "Заявление о выборе условий обслуживания", "Поручения на открытие счетов ДЕПО", "Акт о получении идентификационного кода", "Акт о получении доступа в ЛК",
                                              "Анкета физического лица"]
data_for_address = {'Karachev_pushkin': ("6f39b866-1fed-4add-aa00-e76992516660", "Карачев", "Пушкина", "13", "2", "1", "2", "21", "242500", "Success", "Registration"),
                    'Astrahan_lenina': ("a101dd8b-3aee-4bda-9c61-9df106f145ff", "Астрахань", "Ленина", "22", "4", "2", "15", "77", "414000", "Success", "Actual"),
                    'Novgorod_Niznii': ("555e7d61-d9a7-4ba6-9770-6caa8198c483", "Нижний Новгород", "Горькая", "34", "3", "3", "78", "665", "603000", "Success", "Postal")}

data_for_custom_address = {'Bash': ("Респ Башкортостан, г Ишимбай, ул Есенина 2 кв 5", "Postal", "Success"),
                           'Bel_mayk': ("г Белгород, ул Маяковского 22 кв 8", "Actual", "Success")}

data_for_reg = {'john_smith': ("john_smith666@yandex.ru", "+79810912212", "ios", "10.10.10.10"),
                'john_wayne': ("john_wayne666@google.ru", "+79992315612", "android", "185.102.11.200"),
                'john_white': ("john_white666@mail.ru", "+79602785512", "web-chrome", "2001:db8:3333:4444:5555:6666:1.2.3.4")}

data_for_personal_info = {'dmitriy': ("male", "Дмитрий", "Анатольевич", "Медведев", "1999-12-21T00:00:00", "RUS", 1),
                          'nastya': ("female", "Анастасия", "Сергеевна", "Мельникова", "1995-03-04T00:00:00", "RUS", 2),
                          'leon': ("male", "Леон", "Максимович", "Захаров", "2001-01-05T00:00:00", "RUS", 1)}

url_get_documents_files = 'Documents/GetDocumentFiles'
file_path_jpg = os.path.abspath('..//data_for_tests/passport-1.jpg')
file_path_png = os.path.abspath('..//data_for_tests/passport-2.png')
file_path_pdf = os.path.abspath('..//data_for_tests/passport-3.pdf')
file_path_passport_test = os.path.abspath('..//data_for_tests/passport-test.jpeg')
file_passport_jpg = {'MainPage': open(file_path_jpg, 'rb')}
file_passport_png = {'MainPage': open(file_path_png, 'rb')}
file_passport_pdf = {'MainPage': open(file_path_pdf, 'rb')}
file_passport_test = {'MainPage': open(file_path_passport_test, 'rb')}
passport_data_after_request = {
    "LastName": "ТРАМП",
    "FirstName": "ДОНАЛЬД",
    "MiddleName": "ДЖОН",
    "Gender": 1,
    "BirthDate": "1946-06-14T00:00:00",
    "BirthPlace": "ГОР. КУИНС ШТАТ НЬЮ-ЙОРК США",
    "Serial": "4507",
    "Number": "123456",
    "IssueDepartment": "ПАСПОРТНО-ВИЗОВЫМ ОТДЕЛЕНИЕМ ОВД ПРЕСНЕНСКОГО РАЙОНА УВД ЦАО ГОРОДА МОСКВЫ",
    "IssueDepartmentCode": "772-112",
    "IssueDate": "2016-11-09T00:00:00"
}

passport_data_after_request_pdf = {
    "LastName": "ТВЕРДОХЛЕБОВ",
    "FirstName": "АНДРЕЙ",
    "MiddleName": "НИКОЛАЕВИЧ",
    "Gender": 1,
    "BirthDate": "1975-08-02T00:00:00",
    "BirthPlace": "С. ВОРОНЦОВКА ПАВЛОВСКОГО Р-НА ВОРОНЕЖСКОЙ ОБЛ.",
    "Serial": "2099",
    "Number": "218139",
    "IssueDepartment": "ПАВЛОВСКИМ РОВД ВОРОНЕЖСКОЙ ОБЛ.",
    "IssueDepartmentCode": "362-028",
    "IssueDate": "2000-02-12T00:00:00"
}
path_to_passport_scans_schema = 'json_schemes/add_passport_scans.json'

update_create_user = {
        'description': 'Регистрация учетной записи клиента',
        'objective': 'Регистрируем УЗ клиента на PartnerId и проверяем ответ с данными из БД',
        'precondition': 'create access token, header={Partner-Authorization=access token, Authorization = Bearer jwt-token}',
        'priority': 'High',
        'links': 'WHTLBL-T19',
        'steps': [{"description": "POST url = Account/Register",
                   "testData": "client[email = string, phone=string], consentToPersonalDataProcessing=true\n consentToOfferForProvidingInformationServices=true\nip=string\ndevice=string", "expectedResult": "UserId, AuthId"}]
        }

update_check_register = {
        'description': 'Подтверждение регистрации через СМС',
        'objective': 'Подтверждаем регистрацию тестового пользователя',
        'precondition': 'Регистрируем тестового пользователя в ЕДОКС',
        'priority': 'High',
        'links': 'INTRA-T78',
        'steps': [{"description": "POST url = Account/RegisterConfirm",
                   "testData": "userid, code", "expectedResult": "Success"}]
        }

update_is_register = {
        'description': 'Проверка существования учетной записи',
        'objective': 'Проверяем персону в Едоксе по почте и телефону',
        'precondition': 'Nope',
        'priority': 'High',
        'links': 'INTRA-T111',
        'steps': [{"description": "POST url = Account/IsRegister",
                   "testData": "email: iv5dd@yandex.ru, phone: +79775987914", "expectedResult": "true"}]
        }

update_add_passport = {
        'description': 'Добавление паспортных данных в УЗ клиента',
        'objective': 'Добавляем пользователю паспорт',
        'precondition': 'Создаем тест. пользователя, получаем ему токен',
        'priority': 'High',
        'links': 'INTRA-T112',
        'steps': [{"description": "POST url = Account/AddIdentityDocument",
                   "testData": "passport, number, serial, issueDate, issueAuthority, birthPlace, departmentCode, birthCountryId, files,  userId", "expectedResult": "DocumentKind, Number"}]
        }

update_add_inn = {
        'description': 'Указание ИНН в УЗ клиента',
        'objective': 'Добавляем пользователю ИНН',
        'precondition': 'Создаем тест. пользователя, получаем ему токен',
        'priority': 'High',
        'links': 'INTRA-T83',
        'steps': [{"description": "POST url = Account/AddInn",
                   "testData": "inn, userid", "expectedResult": "DocumentKind, Number"}]
        }

update_add_snils = {
        'description': 'Указание СНИЛС в УЗ клиента',
        'objective': 'Добавляем пользователю СНИЛС',
        'precondition': 'Создаем тест. пользователя, получаем ему токен',
        'priority': 'High',
        'links': 'INTRA-T81',
        'steps': [{"description": "POST url = Account/AddSnils",
                   "testData": "snils, userid", "expectedResult": "DocumentKind, Number"}]
        }

update_add_address = {
        'description': 'Указание адреса клиента',
        'objective': 'Добавляем пользователю Адресс',
        'precondition': 'Создаем тест. пользователя, получаем ему токен',
        'priority': 'High',
        'links': 'INTRA-T85',
        'steps': [{"description": "POST url = Account/SetUserAddress",
                   "testData": "fiasid, cityArea, planStruct, street, stead, house, part, building, flat, postalCode, userid", "expectedResult": "Success"}]
        }
update_reset_documents = {
        'description': 'Редактирование документов пользователя',
        'objective': 'Редактируем документы(паспорт, ИНН, СНИЛС)',
        'precondition': 'Создаем тест. пользователя, получаем ему токен, добавляем ему документы',
        'priority': 'High',
        'links': 'INTRA-T125',
        'steps': [{"description": "POST url = Account/ResetIdentityDocuments",
                   "testData": "Passport: serial, number, departmentCode, issueAuthority, issueDate, birthPlace, birthCountryId,  "
                               "inn, snils, userId", "expectedResult": "Documents: RussianPassport, INN, SNILS(Id, Number)"}]
        }
update_add_custom_address = {
        'description': 'Указание адреса клиента нерезидента',
        'objective': 'Добавляем адресс нерезиденту',
        'precondition': 'Создаем тест. пользователя, получаем ему токен',
        'priority': 'High',
        'links': 'INTRA-T86',
        'steps': [{"description": "POST url = Account/SetNonResidentAddress",
                   "testData": "customAddress, addressType, countryId, userId", "expectedResult": "Success"}]
        }

update_update_personal_info = {
        'description': 'Обновление персональных данных',
        'objective': 'Добавляем, обновляем персональные данные клиенту',
        'precondition': 'Создаем тест. пользователя, получаем ему токен',
        'priority': 'High',
        'links': 'INTRA-T84',
        'steps': [{"description": "POST url = Account/UpdatePersonalInfo",
                   "testData": "userId, personalInfo; gender, firstName, lastName, middleName, dateOfBirth, citizenship", "expectedResult": "Success"}]
        }

update_create_sms_sign_agreement = {
        'description': 'Создание документов присоединения к регламенту Моревиль',
        'objective': 'Формируем документы на подпись',
        'precondition': 'Создаем тест. пользователя, получаем ему токен, добавляем документы(пасспорт, инн, снилс), адресс и перс. данные',
        'priority': 'High',
        'links': 'INTRA-T87',
        'steps': [{"description": "POST url = Account/CreateSmsSignAgreement",
                   "testData": "userId", "expectedResult": "creationTime, description, parentId, id, name, fileId, fileName"}]
        }

update_sign_sms_sign = {
        'description': 'Подписание регламента Моревиль (отправка смс)',
        'objective': 'Отправляем смс, которое надо подтвердить',
        'precondition': 'Создаем тест. пользователя, получаем ему токен, добавляем документы(пасспорт, инн, снилс), адресс и перс. данные. Формируем документы',
        'priority': 'High',
        'links': 'INTRA-T88',
        'steps': [{"description": "POST url = Account/SignSmsSignAgreement",
                   "testData": "Id, userId, code", "expectedResult": "Id, UserId, LastAttemptTime, Seconds, Nanos, CodeLength, DocumentsToSign[], description, parentId, id, name, fileId, fileName"}]
        }

update_confirm_sms_sign = {
        'description': 'СМС подтверждение присоединения о присоединении к регламенту Моревиль',
        'objective': 'Подтверждаем подписание документов о присоединении',
        'precondition': 'Создаем тест. пользователя, получаем ему токен, добавляем документы(пасспорт, инн, снилс), адресс и перс. данные. Формируем документы, подписываем их',
        'priority': 'High',
        'links': 'INTRA-T119',
        'steps': [{"description": "POST url = Account/ConfirmSmsSignAgreement",
                   "testData": "Id, userId, code", "expectedResult": "IsApproved, Id, UserId, LastAttemptTime, Seconds, Nanos"}]
        }

update_create_connect_client_to_product = {
        'description': 'Создает пакет документов для подключения продукта клиенту',
        'objective': 'Формируем документы на подпись для подключения продукта',
        'precondition': 'Создаем тест. пользователя, получаем ему токен, добавляем документы(пасспорт, инн, снилс), адресс и перс. данные. Подключаем его к регламенту Моревиль и подтверждаем присоединение',
        'priority': 'High',
        'links': 'INTRA-T90',
        'steps': [{"description": "POST url = Account/CreateConnectClientToProduct",
                   "testData": "productId, userId", "expectedResult": "CreationTime, Seconds, Nanos, Description, ParentId, Id, Name, FileId, FileName"}]
        }

update_sign_connect_client_to_product = {
        'description': 'Подписание пакета документов для подключения продукта (отправка смс)',
        'objective': 'Отправляем смс для подписания документов на добавление продукта',
        'precondition': 'Создаем тест. пользователя, получаем ему токен, добавляем документы(пасспорт, инн, снилс), адресс и перс. данные. Подключаем его к регламенту Моревиль, формируем документы на подпись',
        'priority': 'High',
        'links': 'INTRA-T120',
        'steps': [{"description": "POST url = Account/SignConnectClientToProduct",
                   "testData": "documentsId, userId", "expectedResult": "Id, UserId, LastAttemptTime, CodeLength, DocumentsToSign, CreationTime, Description, ParentId, Id, Name"}]
        }

update_confirm_connect_client_to_product = {
        'description': 'Подпись документов по подключению продукта клиенту',
        'objective': 'Подключаем продукт клиенту. Формируем документы на подпись. Отправляем смс для подписи, подписываем их',
        'precondition': 'Создаем тест. пользователя, получаем ему токен, добавляем документы(пасспорт, инн, снилс), адресс и перс. данные. Подключаем его к регламенту Моревиль и подтверждаем присоединение. Подключаем его к продукту',
        'priority': 'High',
        'links': 'INTRA-T91',
        'steps': [{"description": "POST url = Account/SmsSignConnectClientToProduct",
                   "testData": "Id, userId, code", "expectedResult": "IsApproved[True], Id, UserId, LastAttemptTime, Seconds, Nanos"}]
        }

update_add_passport_scans = {
        'description': 'Производит распознование сканов страниц паспорта',
        'objective': 'Расспознаем по файлам значения полей паспорта',
        'precondition': 'Создаем тест. пользователя, получаем ему токен.',
        'priority': 'High',
        'links': 'INTRA-T101',
        'steps': [{"description": "POST url = Account/AddPassportScans",
                   "testData": "MainPage[*png, *jpg, *pdf]", "expectedResult": "lastName, firstName, middleName, gender, birthDate, birthPlace, serial, number, issueDepartment, issueDepartmentCode, issueDate, suspiciousFields[]"}]
        }

update_check_passport_scan_in_documents = {
        'description': 'Добавление скана паспорта и проверка документов пользователя',
        'objective': 'Проверить что отсканированный паспорт добавился в документы пользователя',
        'precondition': 'Создаем тест. пользователя, добавляем ему документы, подключаем АСП и продукт 126, получаем ему токен.',
        'priority': 'High',
        'links': 'INTRA-T124',
        'steps': [{"description": "POST url = /Documents/GetDocumentFiles",
                   "testData": "documentId, userId", "expectedResult": "Id, FileName, Type"}]
        }