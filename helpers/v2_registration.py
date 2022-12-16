from random import randint, choice
from data_for_tests.v2_registration import alphabet, status_list


class V2Registration:

    @staticmethod
    def validate_status(received_ids):
        error_count = 0

        if received_ids in status_list:
            pass
        else:
            print('received ids | {0} | not in status list {1}'.format(received_ids, status_list))
            error_count += 1

        if error_count > 0:
            return False
        else:
            return True

    @staticmethod
    def validate_ids(approved_ids, received_ids):
        error_count = 0

        for d in received_ids:
            if d in approved_ids:
                pass
            else:
                print('received ids | {0} | not in approved list {1}.'.format(d, approved_ids))
                error_count += 1

        if error_count > 0:
            return False
        else:
            return True

    @staticmethod
    def get_fio():
        tmp = []
        for i in range(3):
            tmp.append(choice(alphabet))
        return tmp

    @staticmethod
    def get_numbers(n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)

    @staticmethod
    def get_doc_ids(data):
        res = []
        documents = data['documents'][0]['documents']
        res.extend([d['id'] for d in documents])
        res.append(data['smsConfirmationDocument']['id'])
        return res
