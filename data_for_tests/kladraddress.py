url_get_country = 'Fias/AvailableCountries'
url_search_address = 'Fias/SearchAddress'
url_search_details = 'Fias/AddressDetails/a185ae76-7b94-4458-ae55-66f9e83f303e'
search_address = {
"searchText": "Санкт-Петербург ул Политехническая 6 стр 1"
}
founded_address = [
    {
        "Id": "8b567ec2-69f5-4d7d-b88a-86ea4942f288",
        "Address": "г Санкт-Петербург, ул Политехническая,  дом 6 стр 1",
        "PostalCode": "",
        "AddressLevel": "House"
    }
]

kladrId = {
  "kladrId": "8b567ec2-69f5-4d7d-b88a-86ea4942f288"
}

founded_kladr = {
    "Region": {
        "Id": "c2deb16a-0330-4f05-821f-1d09c93331e6",
        "Title": "г Санкт-Петербург"
    },
    "Street": {
        "Id": "c7c5b5c3-322f-4cb5-8205-a2d6a3afe17c",
        "Title": "ул Политехническая"
    },
    "House": {
        "Id": "a185ae76-7b94-4458-ae55-66f9e83f303e",
        "House": "6",
        "Part": "",
        "Building": ""
    },
    "PostalCode": "194021"
}
path_to_schemes_address = 'json_schemes/address.json'
path_to_schemes_kladdr = 'json_schemes/kladdr.json'
path_to_schemes_countries = 'json_schemes/countries.json'

update_get_country = {
        'description': 'Справочник стран',
        'objective': 'Возвращает справочник стран и их коды',
        'precondition': 'Нет',
        'priority': 'Normal',
        'links': 'INTRA-T96',
        'steps': [{"description": "GET url = Fias/AvailableCountries",
                   "testData": "no data", "expectedResult": "[Id, Name]"}]
        }
update_search_address = {
        'description': 'Поиск адресов',
        'objective': 'Возвращает список адресов подходящих под запрос',
        'precondition': 'Нет',
        'priority': 'Normal',
        'links': 'INTRA-T97',
        'steps': [{"description": "POST url = Fias/SearchAddress",
                   "testData": "searchText: string", "expectedResult": "[Id, Address, AddressLevel]"}]
        }
update_get_details_fias = {
        'description': 'Получить детализацию адреса по идентификатору FIAS',
        'objective': 'Возвращает детализацию адреса по полям',
        'precondition': 'Нет',
        'priority': 'Normal',
        'links': 'INTRA-T98',
        'steps': [{"description": "GET url = Fias/Details/{fiasid}",
                   "testData": "no data", "expectedResult": "Region: Id, Title; City: Id, Title; PostalCode"}]
        }
