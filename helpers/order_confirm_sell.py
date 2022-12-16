from sql.sql_wl import *
from sql.query import check_sms


class OrderConfirmSell:

    @staticmethod
    def get_sms_code(document_id):
        cursor = connect_db()
        row = run_sql(cursor, check_sms, document_id)

        if len(row[0]) > 0:
            print('\n************ SMS code ************ : ', row[0][0])
            return row[0][0]
        else:
            print('SMS in [FinamEDO.Security].[Sended:SMS] not found!')
            return False
