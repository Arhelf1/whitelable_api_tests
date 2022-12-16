import json
import os
import sys
from datetime import datetime

import requests


def create_test_case(data, folder):
    try:
        with open("..//data_for_tests/create_test_case.json", "r") as read_file:
            get_json = json.load(read_file)
        get_json['name'] = data['description']
        get_json['objective'] = data['description']
        get_json['folder'] = "/{0}".format(folder)
        get_json['precondition'] = data['precondition']
        get_json['priority'] = 'Normal'
        i = 0
        get_json['testScript']['steps'] = data['steps']
        response = requests.post(
            'https://jira.finam.ru/rest/atm/1.0/testcase',
            headers={'Authorization': 'Basic {0}'.format('emVwaHlyYm90LXM6eG9TQVdn'),
                     "Content-type": "application/json"
                     }, data=str(get_json).replace("'", '"').encode('utf-8'))
        task = response.text
        if response.status_code == 201:
            task = task[task.find(':') + 2:task.find('}') - 1]
            return task
        else:
            print('Тест кейс {0} не создался'.format(data['description']) + str(response))
    except BaseException:
        print('Тест кейс {0} не создался'.format(data['description']))


def update_test_case(data):
    try:
        with open(os.path.abspath("data_for_tests/update_test_case.json"), "r") as read_file:
            get_json = json.load(read_file)
        get_json['name'] = data['description']
        get_json['objective'] = data['objective']
        get_json['priority'] = 'Normal'
        get_json['precondition'] = data['precondition']
        get_json['testScript']['steps'] = data['steps']
        response = requests.put(
            'https://jira.finam.ru/rest/atm/1.0/testcase/{0}'.format(data['links']),
            headers={'Authorization': 'Basic {0}'.format('emVwaHlyYm90LXM6eG9TQVdn'),
                     "Content-type": "application/json"
                     }, data=str(get_json).replace("'", '"').encode('utf-8'))
        if response.status_code != 200:
            print(response.json())
            print('Тест кейс {0} не обновился'.format(data['description']))
    except BaseException:
        print('Тест кейс {0} не обновился'.format(data['description']))


def get_all_builds(type_build, buid_id, folder):
    build = '{0}/{1}:id'.format(type_build, buid_id)
    get_suites = requests.get(
        'https://ci.finam.ru//repository/download/{0}/allure-report.zip!/allur_report/data/suites.json'.format(build),
        headers={
            'Authorization': "Bearer eyJ0eXAiOiAiVENWMiJ9.VU5BdE5rVGFfelNvTGpuSTY0cHRfU3oyWEhJ.ZWVkZWNkOWMtMDEyNS00YzU4LWJhN2MtNDc5YjZlM2Y3OGRm"})
    tests = get_suites.json()['children'][0]['children'][0]['children']
    case_id_lists = [case['uid'] for case in tests]

    date_run = str(tests[0]['time']['start'])[0:len(str(tests[0]['time']['start'])) - 3]
    date_run = datetime.utcfromtimestamp(int(date_run)).strftime('%d-%m-%y %H:%M:%S')
    list_data = {}
    list_ = []
    for case in case_id_lists:
        test = requests.get(
            'https://ci.finam.ru//repository/download/{0}/allure-report.zip!/allur_report/data/test-cases/{1}.json'.format(
                build,
                case),
            headers={'Content-type': 'text/plain; charset=utf-8',
                     'Authorization': "Bearer eyJ0eXAiOiAiVENWMiJ9.VU5BdE5rVGFfelNvTGpuSTY0cHRfU3oyWEhJ.ZWVkZWNkOWMtMDEyNS00YzU4LWJhN2MtNDc5YjZlM2Y3OGRm"})
        test = test.json()
        links = test['links']
        get_links = [link['name'] if 'EDODEV-T' in link['name'] else None for link in
                     links] if links is not False else []
        if len(links) == 0:
            list_.insert(len(list_), get_links)
        steps = []
        asserts = []
        if 'beforeStages' in test.keys():
            get_before = test['beforeStages']
            precondition = '<table><thead><tr><th>Запрос</th></tr></thead><tbody>'
            for step in range(len(get_before)):
                if len(get_before[step]['steps']) > 0:
                    if len(get_before[step]['steps'][0]['steps'][0]['attachments']) > 0:
                        if len(get_before[step]['steps'][0]['steps'][0]['attachments']) > 0:
                            if 'name' in get_before[step]['steps'][0]['steps'][0]['attachments'][0].keys():
                                if '.attach' in get_before[step]['steps'][0]['steps'][0]['attachments'][0]['name']:
                                    req = str(get_before[step]['steps'][0]['attachments'][0]['name']).replace("'",
                                                                                                              '').replace(
                                        '"', '').replace(
                                        ': ', ':').replace(
                                        '}', '}<Br>')
                                else:
                                    req = str(
                                        get_before[step]['steps'][0]['steps'][0]['attachments'][0]['name']).replace("'",
                                                                                                                    '').replace(
                                        '"', '').replace(
                                        ': ', ':').replace(
                                        '}', '}<Br>')
                        precondition = precondition + '<tr><td><code>{0}</code></td></tr>'.format(req)
            precondition = precondition + '</tbody></table>'
            if 'testStage' in test.keys():
                get_steps = test['testStage']['steps']
                for step in range(len(get_steps)):
                    if len(get_steps[step]['attachments']) > 0:
                        if '[assert]' in get_steps[step]['name']:
                            asserts.insert(len(asserts), get_steps[step]['parameters'])
                        else:
                            steps.insert(len(steps),
                                         {'description': get_steps[step]['name'],
                                          'testData': '<table><thead><tr><th>Запрос</th></tr></thead><tbody>' +
                                                      '<tr><td><code>{0}</code></td></tr>'.format(
                                                          str(get_steps[step]['attachments'][0]['name']).replace("'",
                                                                                                                 '').replace(
                                                              '"', '').replace(
                                                              ': ', ':').replace(
                                                              '}', '}<Br>')) + '</tbody></table>',
                                          'expectedResult': ''})
                            if len(asserts) > 0:
                                steps[len(steps) - 1]['expectedResult'] = steps[len(steps) - 1][
                                                                              'expectedResult'] + '<table><thead><tr><th>Ожидаемый результат</th></tr></thead><tbody>'
                                for get_assert in asserts:
                                    data_ = '<tr><td>{0}</td></tr>'.format(get_assert[0]['value'].replace("'", ''))
                                    steps[len(steps) - 1]['expectedResult'] = steps[len(steps) - 1][
                                                                                  'expectedResult'] + data_
                                steps[len(steps) - 1]['expectedResult'] = steps[len(steps) - 1][
                                                                              'expectedResult'] + ' </tbody></table>'
                                asserts = []
                    if len(get_steps[step]['steps']) > 0:
                        if len(get_steps[step]['steps'][0]['steps']) > 0:
                            for step_ in get_steps[step]['steps'][0]['steps']:
                                if len(step_['attachments']) > 0:
                                    if '[assert]' in step_['name']:
                                        asserts.insert(len(asserts), step_['parameters'])
                                    else:
                                        steps.insert(len(steps),
                                                     {'description': step_['name'],
                                                      'testData': '<table><thead><tr><th>Запрос</th></tr></thead><tbody>' +
                                                                  '<tr><td><code>{0}</code></td></tr>'.format(
                                                                      str(get_steps[step]['attachments'][0][
                                                                              'name']).replace("'", '').replace(
                                                                          '"', '').replace(
                                                                          ': ', ':').replace(
                                                                          '}', '}<Br>')) + '</tbody></table>',
                                                      'expectedResult': ''})
                        else:
                            for step_ in get_steps[step]['steps']:
                                if len(step_['attachments']) > 0:
                                    if '[assert]' in step_['name']:
                                        asserts.insert(len(asserts), step_['parameters'])
                                    else:
                                        if step_['name'] != 'Получение corelationID':
                                            steps.insert(len(steps),
                                                         {'description': step_['name'],
                                                          'testData': '<table><thead><tr><th>Запрос</th></tr></thead><tbody>' +
                                                                      '<tr><td><code>{0}</code></td></tr>'.format(
                                                                          str(get_steps[step]['attachments'][0][
                                                                                  'name']).replace("'", '').replace(
                                                                              '"', '').replace(
                                                                              ': ', ':').replace(
                                                                              '}', '}<Br>')) + '</tbody></table>',
                                                          'expectedResult': '<table><thead><tr><th>Запрос</th></tr></thead><tbody>' +
                                                                            '<tr><td><code>{0}</code></td></tr>'.format(
                                                                                str(get_steps[step]['attachments'][0][
                                                                                        'name']).replace("'",
                                                                                                         '').replace(
                                                                                    '"', '').replace(
                                                                                    ': ', ':').replace(
                                                                                    '}',
                                                                                    '}<Br>')) + '</tbody></table>' if len(
                                                              get_steps[step]['attachments']) > 1 else ''})
                    if len(asserts) > 0:
                        if len(steps) > 0:
                            steps[len(steps) - 1]['expectedResult'] = steps[len(steps) - 1][
                                                                          'expectedResult'] + '<table><thead><tr><th>Ожидаемый результат</th></tr></thead><tbody>'
                            for get_assert in asserts:
                                data_ = '<tr><td>{0}</td></tr>'.format(get_assert[0]['value'].replace("'", ''))
                                steps[len(steps) - 1]['expectedResult'] = steps[len(steps) - 1][
                                                                              'expectedResult'] + data_
                            steps[len(steps) - 1]['expectedResult'] = steps[len(steps) - 1][
                                                                          'expectedResult'] + ' </tbody></table>'
                        asserts = []
            name = test['name']
            if test['name'].find('[') > 0:
                name = name[0:name.find('[')]
            if 'statusTrace' in test.keys():
                statusTrace = test['statusTrace']
            else:
                statusTrace = ''
            data = {
                'name': name,
                'description': test['description'],
                'status': 'Pass' if test['status'] == 'passed' else 'Fail',
                'precondition': precondition,
                'statusTrace': statusTrace,
                'time': test['time']['duration'],
                'links': get_links[0] if len(get_links) > 0 else None,
                'steps': steps
            }
            if len(list_data) > 0:
                if name in list_data.keys():
                    [list_data[name]['steps'].insert(len(list_data[name]['steps']), _step) for _step in steps]
                else:
                    list_data[name] = data
            else:
                list_data[name] = data
    not_case = []
    results = []
    for data in list_data:
        case_id = list_data[data]['links']
        get_steps = []
        # if list_data[data]['statusTrace'] == '':
        if list_data[data]['links'] is not None:
            a = 1
            update_test_case(list_data[data])
        else:
            not_case.insert(len(not_case), list_data[data]['name'])
            case_id = create_test_case(list_data[data], folder)
        i = 0
        while i < len(list_data[data]['steps']):
            get_steps.insert(len(get_steps), {
                "index": i,
                "status": "Pass",
                "comment": list_data[data]['steps'][i]['testData'] + list_data[data]['steps'][i]['expectedResult']
            })
            i += 1
        if case_id is not None:
            results.insert(len(results), {'testCaseKey': case_id,
                                          'status': list_data[data]['status'],
                                          'executionTime': list_data[data]['time'],
                                          'scriptResults': get_steps,
                                          'comment': str(list_data[data]['statusTrace']).replace('"', '')})
    return results


if __name__ == "__main__":
    get_all_builds(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))
