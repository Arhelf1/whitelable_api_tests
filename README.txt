Клонировать репозиторий.
В git консоли наберите команду:
git clone https://git.finam.ru/scm/qa/whitelable_api_tests.git

Для запуска тестов из командной строки используйте команду вида:
%virtualenv_path%\py.test -s -n4 %test_dir%\tests

где :
%virtualenv_path% - абослютный путь к папке с виртуальным окружением,
%test_dir% - абослютный путь к папке с тестами


Пример :
D:\BuildAgent_1\work\80c7c5c4409fbef0\wl-api-env\Scripts\py.test -s -n4 D:\BuildAgent_1\work\80c7c5c4409fbef0\tests

Версия Python 3.5.2
