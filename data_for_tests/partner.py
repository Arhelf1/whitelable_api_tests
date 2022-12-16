url_get_products = "Partner/AvailableProducts"
path_to_get_products = 'json_schemes/get_products_of_partner.json'
update_get_products = {
        'description': 'Получение списка доступных продуктов',
        'objective': 'Получаем список доступных продуктов Партнера по его Partner-Authorization',
        'precondition': ' ',
        'priority': 'High',
        'links': 'INTRA-T99',
        'steps': [{"description": "GET url = Partner/AvailableProducts",
                   "testData": "no data", "expectedResult": "Id, Description"}]
        }
