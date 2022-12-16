url_get_access = 'PartnerAuth/RefreshToken'
headers = {
  'Content-Type': 'application/json'
}
path_to_access_schema = 'json_schemes/access.json'
update_get_access_token = {
        'description': 'Обновление Access токена (и одновременно Refresh токена)',
        'objective': 'Проверяем работу получение access token. Сравнимаем результат с БД и валидацию',
        'precondition': 'Создаем refresh token',
        'priority': 'High',
        'links': 'INTRA-T100',
        'steps': [{"description": "POST url = PartnerAuth/RefreshToken",
                   "testData": "refreshToken, AccessToken", "expectedResult": "refreshToken, AccessToken"}]
        }

update_create_refresh_token = {
    'description': 'Получение Refresh токена с использованием globalId',
    'objective': '',
    'precondition': '',
    'priority': 'High',
    'links': 'WHTLBL-T33',
    'steps': [{"description": "POST url = v1/Token/CreateRefresh",
               "testData": '', "expectedResult": ''}]
}

update_get_auth_token = {
    'description': ' Получение токена авторизации'
}