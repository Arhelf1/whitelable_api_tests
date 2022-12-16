from sql.sql_wl import *


class OrderCreateSell:

    @staticmethod
    def validate_sms(query, document_id):
        cursor = connect_db()
        row = run_sql(cursor, query, document_id)
        if len(row[0]) > 0:
            # print('\n[FinamEDO.Security].[Sended:SMS] : ', row)
            return row
        else:
            print('\nSMS in [FinamEDO.Security].[Sended:SMS] not found!')
            return False
