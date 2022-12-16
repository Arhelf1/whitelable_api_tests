url_get_documents_files = 'Documents/GetDocumentFiles'
url_get_file_content = 'Documents/GetFileContent'
path_json_scheme_get_documents_files = 'json_schemes/get_documents_files.json'

update_get_documents_files = {
        'description': 'Получить информацию о списке файлов документа',
        'objective': 'Получаем список документов доступных клиенту',
        'precondition': 'Создаем тест. пользователя, получаем ему токен. Добавляем документы, перс. данные, адрес, присоединяем к Моревиль и добавляем продукт',
        'priority': 'High',
        'links': 'INTRA-T94',
        'steps': [{"description": "POST url = Documents/GetDocumentFiles",
                   "testData": "documentId, userId", "expectedResult": "[Id, Filename, Type]"}]
        }
update_get_file_content = {
        'description': 'Получить содержимое файла',
        'objective': 'Получаем содержимое файла',
        'precondition': 'Создаем тест. пользователя, получаем ему токен. Добавляем документы, перс. данные, адрес, присоединяем к Моревиль и добавляем продукт. Получаем ID документа',
        'priority': 'High',
        'links': 'INTRA-T95',
        'steps': [{"description": "POST url = Documents/GetDocumentFiles",
                   "testData": "fileId, userId", "expectedResult": "string binary file"}]
        }