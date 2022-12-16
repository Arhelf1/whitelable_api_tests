import requests
from jsonschema import validate
from data_for_tests.quotes_test_data import (url, quotes_list, tqbr_increase, mct_increase)
from notify.email_robot import logger
import lxml.etree


# возвращает актуальную цену на котировку + надбавка
def get_actual_qoute_price(board, app):

    quotes = app.get_request(url, app.token())
    assert quotes.status_code == requests.codes.ok, 'Status code : ' + str(quotes.status_code)
    quotes_data = quotes.json()
    assert len(quotes_data) > 0

    for d in quotes_data:
        if d['securityBoard'] == board:
            # актуальная цена котировки + надбавка tqbr_increase
            if d['securityCode'] == quotes_list[0]:
                return float(d['askFormula'][:3]) + tqbr_increase

            # актуальная цена котировки + надбавка mct_increase
            if d['securityCode'] == quotes_list[1]:
                price = float(d['askFormula'][:4])
                exchange_rates = float(d['askFormula'][-11:-9])
                return (price * exchange_rates) + mct_increase


def validate_schema(app, data, path_to_schema):
    # валидация схем проходящих как список диктов
    for i in data:
        validate(i, app.get_json_schema(path_to_schema))


def response_status(response_data, target_url, requests_codes=requests.codes.ok):
    if response_data.status_code != requests_codes:
        raise AssertionError(logger(response_data, target_url))


def set_env(allure_env: str, name: str, val: str) -> None:
    """Add entry to environment.xml."""
    parser = lxml.etree.XMLParser(remove_blank_text=True)
    tree = lxml.etree.parse(allure_env, parser)
    env = tree.getroot()

    exist = tree.xpath(
        f"/environment/parameter[key[text()='{name}'] "
        f"and value[text()='{val}']]"
    )

    if not exist:
        parameter = lxml.etree.SubElement(env, "parameter")
        name_node = lxml.etree.SubElement(parameter, "key")
        name_node.text = name
        value_node = lxml.etree.SubElement(parameter, "value")
        value_node.text = val

        with open(allure_env, "w") as env_xml:
            env_xml.write(lxml.etree.tounicode(env, pretty_print=True))
