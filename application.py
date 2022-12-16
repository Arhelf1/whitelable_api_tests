import base64
import json
import os
import shutil

import lxml.etree
import requests
import csv
import random
from random import choice
from string import digits
import time
import codecs
from path import Path

from data_for_tests.auth import url_refresh, full_url_access, auth_headers
from data_for_tests.documents import url_get_file_content

class Application(object):
    def __init__(self, base_url, limit_time):
        self.base_url = base_url
        self.limit_time = int(limit_time)

    def get_request(self, url, headers=None):
        response = requests.get(self.base_url + url, headers=headers, timeout=self.limit_time)
        return response

    def get_request_params(self, url, params=None):
        response = requests.get(self.base_url + url, params=params, timeout=self.limit_time)
        return response

    def post_request(self, url, data, headers=None, cookies=None, result=True, files=None, flag=True):
        if flag:
            response = requests.post(self.base_url + url, json=data, headers=headers, cookies=cookies, files=files,
                             timeout=self.limit_time, allow_redirects=True)
        else:
            response = requests.post(url, json=data, headers=headers, cookies=cookies, files=files,
                                     timeout=self.limit_time, allow_redirects=True)
        if result:
            return response

    def delete_request(self, url, headers=None, cookies=None):
        response = requests.delete(self.base_url + url, headers=headers, cookies=cookies, timeout=self.limit_time)
        return response

    def response_body_get(self, markets):
        response_body = self.get_request(markets).json()
        return response_body

    def get_json_schema(self, json_name):
        current_dir = os.path.dirname(__file__)
        path_to_json = os.path.join(current_dir, json_name)
        json_schema = json.loads(open(path_to_json).read())
        return json_schema

    def get_dict(self, response_body, key, message):
        if type(response_body) == dict:
            result = response_body
            for el in key:
                try:
                    result = result[el]
                except BaseException:
                    raise ValueError(message)
            return result
        else:
            raise ValueError("Переданный" + type(response_body) + "не является словарем")

    def access_token(self):
        response = requests.request("POST", url_refresh, headers={}, data={})
        refresh_token = response.text
        body = json.dumps({
            "RefreshToken": refresh_token,
            "AccessToken": ""
        })
        print("BODY = ", body)
        response = requests.request("POST", full_url_access, data=body, headers=auth_headers)
        print("Response Access token = ", response.json())
        access_token = response.json()['AccessToken']
        headers = {
            'Content-Type': 'application/json',
            'Partner-Authorization': access_token
        }
        return headers

    def get_personal_data(self):
        from russian_names import RussianNames
        fio = RussianNames(count=1, output_type='dict').get_person()
        return fio

    def remove_files_from_dir(self, folder):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    def remove_file_by_name(self, abs_path):
        try:
            os.remove(abs_path)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

    def find_file_id_by_name(self, request, name):
        if type(request) == list:
            for el in request:
                if el['Name'] == name:
                    try:
                        file_id = el['FileId']
                    except:
                        raise ValueError('Документ ' + name + ' по имени не найден')
            return file_id
        else:
            raise ValueError("Переданный объект не является листом")

    def download_file_by_id(self, file_id, file_name, user_id, header):
        data = {
            "fileId": file_id,
            "userId": user_id
        }
        response = self.post_request(url_get_file_content, data=data, headers=header)
        open('documents_for_parse//' + file_name + '.pdf', 'wb').write(response.content)
        time.sleep(3)

    @staticmethod
    def get_random(_from, to):
        return random.randint(_from, to)

    def get_random_tel(self):
        return '+7' + str(self.get_random(9000000000, 9999999999))

    @staticmethod
    def random_email():
        letters_eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'l', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                       'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        return "{0}@{1}.rr".format(''.join(str(e) for e in random.choices(letters_eng, k=5)),
                                   ''.join(str(e) for e in random.choices(letters_eng, k=5)))

    def get_random_city(self):
        address = []
        path = Path('csv/city.csv').abspath()
        # if 'tests' in os.getcwd():
        #     path = os.path.abspath('..\csv')
        # else:
        #     path = os.path.abspath('csv')
        with codecs.open(path, "r", "utf_8_sig") as f:
            csv_reader = csv.reader(f)
            next(csv_reader)
            for row in csv_reader:
                address.append(row[9])
        city = random.choice(address)
        return city

    def get_random_kladrid(self):
        kladrid = []
        path = Path('csv/city.csv').abspath()
        with open(path, "r") as f:
            csv_reader = csv.reader(f)
            next(csv_reader)
            for row in csv_reader:
                kladrid.append(row[13])
        kladrid = random.choice(kladrid)
        return kladrid

    def get_random_number(self, n):
        return (''.join(choice(digits) for i in range(n)))

    def get_passport_data(self, user_id):
        number = self.get_random_number(6)
        serial = self.get_random_number(4)
        data = {
            "passport": {
                "number": number,
                "serial": serial,
                "issueDate": self.random_date("2019-12-251:30:14", "2020-12-254:50:14", random.random()),
                "issueAuthority": "Полиция",
                "birthPlace": self.get_random_city(),
                "departmentCode": self.get_random_number(3) + "-" + self.get_random_number(3),
                "birthCountryId": 1,
                "files": [{
                    "fileName": "bbbtestbb",
                    "content": "SGVsbG8="
                }]
            },
            "userId": user_id
        }
        return data

    def get_set_identity_documents_data(self, user_id):
        number = self.get_random_number(6)
        serial = self.get_random_number(4)
        inn = self.inn_gen()
        snils = self.snils()
        data = {
            "passport": {
                "number": number,
                "serial": serial,
                "issueDate": self.random_date("2019-12-251:30:14", "2020-12-254:50:14", random.random()),
                "issueAuthority": "Миллеровским РОВД Ростовской области",
                "birthPlace": self.get_random_city(),
                "departmentCode": self.get_random_number(3) + "-" + self.get_random_number(3),
                "birthCountryId": 1
            },
            "snils": snils,
            "inn": inn,
            "userId": user_id
        }
        return data

    @staticmethod
    def inn_ctrl_summ(nums, type):
        """
        Подсчет контрольной суммы
        """
        inn_ctrl_type = {
            'n2_12': [7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
            'n1_12': [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
            'n1_10': [2, 4, 10, 3, 5, 9, 4, 6, 8],
        }
        n = 0
        l = inn_ctrl_type[type]
        for i in range(0, len(l)):
            n += nums[i] * l[i]
        return n % 11 % 10

    def inn_gen(self, l=12):
        """
        Генерация ИНН (10 или 12 значный)
        На входе указывается длина номера - 10 или 12.
        Если ничего не указано, будет выбрана случайная длина.
        """
        if not l:
            l = list((10, 12))[random.randint(0, 1)]
        if l not in (10, 12):
            return None
        nums = [
            random.randint(1, 9) if x == 0
            else random.randint(0, 9)
            for x in range(0, 9 if l == 10 else 10)
        ]
        if l == 12:
            n2 = self.inn_ctrl_summ(nums, 'n2_12')
            nums.append(n2)
            n1 = self.inn_ctrl_summ(nums, 'n1_12')
            nums.append(n1)
        elif l == 10:
            n1 = self.inn_ctrl_summ(nums, 'n1_10')
            nums.append(n1)
        return ''.join([str(x) for x in nums])

    @staticmethod
    def snils():
        nums = [
            random.randint(1, 1) if x == 0
            else '-' if x == 3
            else '-' if x == 7
            else ' ' if x == 11
            else random.randint(0, 9)
            for x in range(0, 12)
        ]
        cont = (nums[10] * 1) + (nums[9] * 2) + (nums[8] * 3) + \
               (nums[6] * 4) + (nums[5] * 5) + (nums[4] * 6) + \
               (nums[2] * 7) + (nums[1] * 8) + (nums[0] * 9)
        if cont in (100, 101):
            cont = '00'
        elif cont > 101:
            cont = (cont % 101)
            if cont in (100, 101):
                cont = '00'
            elif cont < 10:
                cont = '0' + str(cont)
        elif cont < 10:
            cont = '0' + str(cont)
        nums.append(cont)
        return ''.join([str(x) for x in nums])

    def get_inn_data(self, user_id):
        data = {
            "inn": self.inn_gen(l=12),
            "userId": user_id
        }
        return data

    def get_snils_data(self, user_id):
        data = {
            "snils": self.snils(),
            "userId": user_id
        }
        return data

    @staticmethod
    def decompress(content):
        import gzip
        import binascii
        try:
            decompress = gzip.decompress(content)
        except binascii.Error:
            raise binascii.Error('Ошибка распаковки данных из токена')
        return decompress

    @staticmethod
    def base64encode(context):
        import binascii
        lenx = len(context) % 4
        if lenx > 0:
            context = context + ('=' * (4 - lenx))
        try:
            decode = base64.b64decode(context.encode())
        except binascii.Error:
            raise binascii.Error('Ошибка перекодировки данных из токена')
        return decode

    @staticmethod
    def base64decode(context):
        context = context.replace('-', '+').replace('_', '/')
        lenx = len(context) % 4
        if lenx > 0:
            context = context + ('=' * (4 - lenx))
        return base64.b64decode(context).decode('utf-8')

    def str_time_prop(self, start, end, format, prop):
        """Get a time at a proportion of a range of two formatted times.

        start and end should be strings specifying times formated in the
        given format (strftime-style), giving an interval [start, end].
        prop specifies how a proportion of the interval to be taken after
        start.  The returned time will be in the specified format.
        """

        stime = time.mktime(time.strptime(start, format))
        etime = time.mktime(time.strptime(end, format))

        ptime = stime + prop * (etime - stime)

        return time.strftime(format, time.localtime(ptime))

    def random_date(self, start, end, prop):
        s = self.str_time_prop(start, end, '%Y-%m-%d%H:%M:%S', prop)
        s = s[:10] + 'T' + s[10:] + 'Z'
        return s

    def filter_value_in_list(self, my_list, key_in_list, value_in_dict):
        dict_list = list(filter(lambda document: document[key_in_list] == value_in_dict, my_list))
        d = {k: v for element in dict_list for k, v in element.items()}
        return d

