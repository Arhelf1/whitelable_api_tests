url_files_find = 'Files/Find'
url_find_by_doc = 'Files/FindByDoc'
url_file_attach = 'Files/Attach'

path_to_registration = 'json_schemes/registration.json'
# Этот же json используется для валидации схемы у метода Files/FindByDoc
path_to_files_find = 'json_schemes/path_to_files_find.json'
path_to_files_attach = 'json_schemes/path_to_files_attach.json'

# Aртура данные
user = '10BA465C-D6AE-4EFD-9F6D-8F7927A35237'
document = 52134145

# файл картинки
jpeg_name = 'TestDc.jpg'

field_list = ['data', 'id', 'documentId', 'name']


def get_body_attach(user_id, document_id):
    return {
        "userId": user_id,
        "Files": [{"DocumentId": document_id,
                   "Name": "TestDc.jpg",
                   "Data": "iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAADdgAAA3YBf"
                           "dWCzAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAA/sSURBVHic7Z17dBTXfcc/s1q90AsBAoQ"
                           "wUGNsHwIBbMCPYsaCkKQ2dV3XD8wpznFPE9fHU/u4B6cGN8ekbkySpqZpJnFSN84BN8GAAnYhDhzbmDGKcWxikCVeE"
                           "sK8JRB6IAm9VqvbP2a0CGm1mpmd2QfM55w9q13d1+797p07v9+9vysJIbjakBQtF7gRuMl4TAaGA7lATr9nCWgN86g"
                           "FjgJVvc9ClS/E9IPEACnZBSApWhYwD1gAzEXv8EKXqmsCPgNKjcceocqtLtUVE5JOAJKipXG5w4uBOUBqnJoTBPYDG"
                           "rAF+INQ5aT6QpNGAJKi3Q4sA5YAI+LcnME4C5QAG4GPkkEMCS0ASdEmonf6MvRrejJxBlgL/FSo8tl4N2YwElIAkqL"
                           "NBlYC96NP0pKZAPqIsEao8p/i3Zj+JJQAJEW7C3gB+Fq82+ISu4EfClXeFu+G9JIQApAUbSHwInBXvNsSIz4ElgtV/"
                           "jTeDYmrACRFGw+sAR6MWyPih0C/NKwQqvxFvBoRFwFIiuYHngFWAdkxb0Bi0YX+I3hRqHJnrCuPuQAkRZsHvApMi2n"
                           "Fic9B4BtClffGstKYCUBStBTgJeB5kn9m7xbdwPeBfxWqHIhFhTERgHGtX49uwfMYmjLgUaHKh9yuyOd2BZKi3YNuL"
                           "vU63zwzgI8lRVvsdkWujQCSoknAauDbeEO+XXqAfxGqvNqtClwRgOGwWYtut/eIng3A40KV250u2HEBSIqWDWwGFjl"
                           "asMceYJFQ5UtOFuroHEBStALgA7zOd4M7gLclRUt3slDHBCAp2gT0RRKznSrTYwALgY2GIc0RHBGA8ct/l+Rz2SYj9"
                           "wFrJUVzpO+iLsS45r+D1/mxZCnwMycKikoAxmx/M96wHw+ekBTth9EWYlsAxn3+WrwJXzx5TlK0F6IpIJoRYDXefX4"
                           "i8G+Sov2j3cy27ACGeXcbnoUvURDAEqHKG61mtCwAw7GzHxhptbJE5Zn5YxiXl2Yq7QdVzWw/fNHlFtmiGZghVPm4l"
                           "UyW7icNl+56rqLOB3h4Zj7TC4eZStsR6ElUAeQCv5EUbb5Q5W6zmazOAV7C8+olMnegr600jWkBGCt5nrfaIo+Ys1J"
                           "StPlmE5sSgGF6fBVv0pcM+IDXzfoMzI4Az+Ct4UsmJgPLzSQcUgDGrH9VlA3yiD0rJUW7bqhEZkaANXhLt5ORYcB/D"
                           "JUoogCMHTvX4qaNq4WHJEVbECnBUCOApVsKj4Tk5Uj/HNQQZGzUvCb26h2o7aCz25xF9PTFLpdb4zi3SYq2QKjyznD"
                           "/jGQJjMrLlEx8a+PxeDfBbVYAYQUQ1hdg7M+P+85VD0e5TajyJ/3fHGwEWOlyYwZlfF4qt0/KMZ2+pKwBgIxUH4unD"
                           "jedT6tupq5VN5kvnJJL/jBzbpHD59upqHF8dXYsWAH8df83B4wARliWL4iT1e/BGSN4fckk0+lzV3wGwJicVKpWTje"
                           "d797Xqth9rAWAPzx9s2ln0BrtHC9uP2O6ngRCAH8mVPlE3zfD3QUswzP5Xo1IwGP93xxMAB4JwpwJWWx/4kYemz2SY"
                           "WlRr+GNLAAjFJu3ujdBmDwqnc2P38Cdk7JR/2Yi5c9NY86ErGiKvEFStDv7vtFfUt6vP4F45b7ryMtICb0uyPbzu29"
                           "O4S+/ZH6yG4Zv9H0REoCxxNtb5JkgPPDlfIqn5A54P8Pv4+cPTWRMju3gqA9LihbK3HcEmEfiRuC8pshK8/HyveMH/"
                           "X9Oegov/UWR3eKHA7f3vugrgIhOA4/Y8VzxWMblRv6FL5k1gjsm2XbSfrX3j74CKLZbmodzSBI8eou5Nbc/uu86Uny"
                           "27thDAvBDKOT6HDslOU2wR9DZ3WM5nxBYytfTxwDWFTSfNxC03jYr3Do+i8Ihfv29TC/M5MEZ+WzY12C1mtmSouULV"
                           "W7stX/OI34h169gS3kjW8obLec73xqg4Dv7bdVZ/NPDtvK5wb1T8yylf2C6LQH40Leal/ReArzrf4JwY0GGpfQLpuS"
                           "SnZ4ydMKBzIPLzqC5dkqIxOjsVIZnmmtYW1eQ0xf1sHjZ6T7G5ZrbpQNQWdcBQIpPYvJI88EzTjV10h7QLwMT8tPI8"
                           "JuzsjW0dXPhku5EKsj2k59pzonUHujhVNPQawmKTO5Q6iXdL/H1m3MpKbM8ak6DywK4yWruoVj5lUL+7rZRptKWHmvh"
                           "nteqAPj6zcNtOYNGZfnZ+09TTefr6wxav+x6W86g5cWFPHlngal8e09dYsHPjgyZblye9Svx4qnDbQvAZxyw5NYZOx"
                           "4WGWHSLd2XuRNtmYfHSIo20o9n+08o6lq7KbI4CozPS2PFwkKGZ6ZQkJ3K6Bw/2WkpXGzvpqE9SGNbN+U17bxf1czJ"
                           "xisuQ9P8uDD8e9intrnLsgAAVnzF3CBefaGT96ua2VnVzL4zbbd6AkgwalrcjRE9eVQ6k0cV8K07Cth6oOlhH/o2Io"
                           "8E4ezFmAQJByAz1ZfvQ3cOeCQIWnVLzOoalurL9qEHFvBIEN6rbKY94K65uZesdF+WD/0MXY8EoT3Qw86q2IwCWWkp"
                           "6d4IkIBsPdAUk3pyM1LSJJ7aVQeYM9lZoCgvjZFZ5owarZ1BjtXr5yXlZaQwcYR5k+7nZ9sA8Pskpo7NNJ2v+kIHl7"
                           "r0oXZKQQaZqeZMwedbA9Q26xO1cXlpjDL5GS91BqmuN3cm1IT8NCq+7X44hs7uHiSe2tUJWDNAe7jGlIIMXnt4EreM"
                           "N2eatkuPgKc3n7AWJayX/GF+bnW5gdcCOekpjMryMzLLz6gsP/Mn53DzaGveQDt09wie2HSCTfsbuvzo8eUsXQJmFg"
                           "1j8+M3uNM6D1c5dK6DZ7ac5OMTrQDNfqAFiwLI8Hsbh5KN2pYAP/+ojp/sPkcgGFoN1dI7AljCrO/cI76cawnwdkUT"
                           "W8ob2XO8lZ6BG8FDI4Al0rwRIOE43xrgeEMXJxo6OdbQiXa0hY/Cd3pfvBEgmdl2sIlvbjhOICjoCto6/KvZD1i2Ot"
                           "hZtevhPG9XNIVsGTZp8gHVVnPVt5mORezhEoGgYPuhqINWV/uAoReq9aP+kieAeFN6rIWLHcFoizniCSBJ2XrQkZD1"
                           "R3xApdVc9W1RK88jCtoDPbxlY/NMGCp9QpWbgRoruVo7gzHzWXsMZN2n9aG9CVFQI1S5ufd+zvJl4GBtUkbKSnoCQc"
                           "GPPzznRFFH4PLu4AHx44Zi/1lPAPFg/b4Gp6KVfgKXBRA2imQkys60OdEIDwsEewSv7Kp1qridcFkApYCl5aj7z3oC"
                           "iDX/vacutHAmSgLofa4LwDiT3lJo2IO17X29Sh4uc7yhk1U7zjpV3KdGn18RIeQDKyV0BQWHznc41SCPCAgBT/32pJ"
                           "N3XqG+7isAy/OAXUct+5E8bPDLP9aFdjI7RKiv+wqgFLAUauLXf6p3qkEeg1B9oZPv/N7R2MQNGNd/6CMAocpdwJtW"
                           "Sjp0roN9p73JoFs0tHXz4Nqj0Xr8+rPB6GtgYKTQN6yW9uvPvFHADTq7BY++cYzqC47M+vuyru+LKwQgVPljLPoGNp"
                           "U1mj5uxcMcQsCTJcfZc7zV6aIrjT4OEW5pj6VRoLGtm98n5mHKScuqHWfshHwxw4C+HUwAln7S3mTQGYSA57aeYo3m"
                           "iK1/QPGYEYBxosRbVkp+98hFypPzGJWEIRAU/P3G4/ziozq3qnir/2khMPi5gRHPmutPj4Dnt5221SoPaOvq4ZF11W"
                           "zabzngoxXC9mlYAQhV3gvssFL67mMt/F+MdrVeTZy5GGDx/1TxXqWrRrUdRp8OINL67u9ZrWXl707T0umtFjLL9sMX"
                           "+fP/OsTeU5fcrmrQvhxUAEKVdwO7rdRysrGLpzeftJLlmiQQFLzwzhkeWVdNg/srrHcbfRmWoXZ4fNdqbb/9vJHX/3"
                           "jBarZrhi/qO/nqLyr5ye5zhDmz0w0i9mHYk0OvSKBom7B4gniG38eOJ25klreFPERnt2CNVssru87REbuNNSVClR+K"
                           "lMDMHq9nAUsmqY7uHu7/1VHKvEUjgB746bb/PMjL79XEsvNb0fsuIkMKQKjyaWCV1dob27q575fXtghONHbxt/97jA"
                           "d+ddSplTxWWGX0XUTM7vL8MVBhtQW9InDBpp3QHKvv5MmSE8z60YF43RpXoPfZkAw5BwglVLR5wIfYOFY2xSexYmEh"
                           "y4vHYu+Im+Sgsq6Df/+glpKyRoJD7Mt2EQHMF6pcOmRKLAgAQFK0l9FPobbF/OtzeO2RSabPxEkGOrp72HG4mQ37Gn"
                           "jnUNNQ+/FjwWqhyqZPf7cqgBRgF8ZxI3YYnpnCs/JY/uHOAtOh2RKNYI9g19EWNpU1svVAUyIZv0qBu4Uqm26QJQEA"
                           "SIo2HtgPmDvbbBBGZ6eyvHgMj88tID0JIo4IAZ+cvMSmsga2lDdS15pwG2TrgZlmJn59sSwAAEnR7gG24cAx80V5qSy"
                           "9ZST3T89neqH5QI+xoqK2nU37GygpazR15k+cEMBiocrvWM1oSwAAkqJ9H/hnW5kH4YZR6Tzw5Xz+alo+XxqbGfMJY2"
                           "1LgIqadj4/20ZFbTufnW6Lx+2bHX4gVPl5OxmjEYAE/AaXDpzOTk9hxrhMZhYNY1bRMGYWDeP6ken4HVBFICiorOugv"
                           "Kad8pp2KmraKK9pd2LHbTx4E1gqVNlWR9oWAIROHN8GLLJdiAV8EozJSaUwN5WivDQKc1MZnZ2KQBAIilCwpEAw/Ouu"
                           "oKC2uYvD5zvsBlVKNN5FH/ptX5uiEgCApGjZ6DtNZkdVkIdV9gLFQpWjsrJFLQAASdEK0G9BvBPIYkMlME+octTrxx"
                           "y5ETcasggb4WY8LFMJLHKi88EhAQAIVT6JbiAKu/TIwxH2ov/yHVt146gpzlBlMfrkxMNZ3kW/5ju6bNhxW6wxKVmM"
                           "xX2GHhF5E32277hb1RVjvHFbshT4ARY3mXhcgUD/DpdGc6sXCUfuAiJWoJuN1xGl7+AapB54zI551wquCwBCDqT1RO"
                           "FFvMYoBR616tixQ0z8scYHuRtYjXdJiIRA/47ujkXnQ4xGgCsq1FcWvQq4fy5aclEBPGl2JY9TxHxFhvEBZwHLsbja"
                           "+CqlFf27mBXrzoc4jABXVK7PDdZgcd/BVUQJ8GyshvtwxFUAoUYo2kLgReCueLclRuwGvitU+f14NyQhBNCLpGh3AS"
                           "8AX4t3W1xiB/C9SHv1Yk1CCaAXSdFmAyuB+3Fg2VmcEegBN14ebIt2PElIAfQiKdpEYJnxSDZXcyV6SJY3wkXmSBQS"
                           "WgB9kRTtdnQhLAFGxLk5g9GAbrd/o380rkQlaQTQi7EMbR6wAN3zOAeI106TAHqQ7Z3oq6JK3bLZu0XSCaA/kqJlc"
                           "VkQc4GbgEKXqqtBP2njE/ROL+2Nup2sJL0AwiEpWi76nOEm4zEZGA7kAjn9nkE/PbWl33MT+pmKR4xHpXG+0lXF/wP"
                           "3D793xGpPkQAAAABJRU5ErkJggg=="}]
    }


def get_body_find(user_id, file_id):
    return {
        "userId": user_id,
        "FileIds": file_id
    }


def get_body_by_doc(user_id, file_id):
    return {
        "userId": user_id,
        "DocumentIds": file_id
    }


def logger(**kwargs):

    file_errors = {
            'documentId': 'ERROR: полученный от метода /Files/Attach DocumentId ' + str(kwargs.get('left', '')) + ' не равен отправленному ' + str(kwargs.get('right', '')),
            'name': 'ERROR: полученный от метода /Files/Attach name ' + str(kwargs.get('left', '')) + ' не равен отправленному ' + str(kwargs.get('left', '')),
            'id': 'ERROR: полученный от метода /Files/Attach id ' + str(kwargs.get('left', '')) + ' пуст',
            'files_attach_len': 'ERROR : Files/Attach вернул пустой список данных.',
            'attach_check': 'Проверка аттача файла. Получили пустой список данных.',
            'files_find_len': 'Files/Find вернул пустой список данных.',
            'data': 'Files/Find вернул пустой файл.',
            'files_find_id': 'Files/Find вернул пустой id файла.'
    }

    return file_errors.get(kwargs['key'], 'На данный случай не предусмотрено сообщение об ошибке.')
