url_get_client_products_statuses = "Client/GetProductsStatuses"
path_to_products_statuses = "json_schemes/GetProductsStatuses.json"
statuses = ['ProductOrderStatusUnknown', 'Received', 'Accepted', 'Executed', 'Rejected', 'Canceled', 'Delayed',
            'Creating', 'DocumentsFormed', 'Waiting']
update_get_products_statuses = {
        'description': 'Получение статусов продуктов клиента',
        'objective': 'Получаем статус продуктов клиента',
        'precondition': 'Создаем тест. пользователя, получаем ему токен. Добавляем документы, перс. данные, адрес, присоединяем к Моревиль и добавляем продукт.',
        'priority': 'High',
        'links': 'INTRA-T93',
        'steps': [{"description": "POST url = Client/GetProductsStatuses",
                   "testData": "userId", "expectedResult": "OrderId, productId, productName, status, StatusName"}]
        }
