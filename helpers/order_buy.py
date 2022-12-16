from sql.sql_wl import *
from sql.query import order_buy
from data_for_tests.order_buy import *


class OrderBuy:

    @staticmethod
    def validate_after_operation(order_id, price):

        error_count = 0

        cursor = connect_db()
        row = run_sql(cursor, order_buy, order_id)
        print('\n[WhiteLabelDev].[Trade].[Orders] : ', row)

        # тут копились значения с предыдущего прохода тестов
        user_data.clear()
        user_data.append(order_id)
        user_data.append(price)
        user_data.extend(tmp)

        for i in range(len(user_data)):
            if user_data[i] in row[0]:
                pass
            else:
                print('| {0} | not in approved list.'.format(user_data[i]))
                error_count += 1

        if error_count > 0:
            return False
        else:
            return True
