from collections import Counter


class Quotes:

    @staticmethod
    def validate_exchanges(field_name, approved_data, received_data):
        error_count = 0

        for d in received_data:
            if d[field_name] not in approved_data:
                print('received exchange | {0} | not in approved list.'.format(d[field_name]))
                error_count += 1

        if error_count > 0:
            return False
        else:
            return True

    @staticmethod
    def validate_quotes(field_name, approved_data, received_data):
        error_count = 0

        for d in received_data:
            if d[field_name] in approved_data:
                pass
            else:
                print('received quotes | {0} | not in approved list.'.format(d[field_name]))
                error_count += 1

        if error_count > 0:
            return False
        else:
            return True

    @staticmethod
    def validate_title(approved_data, received_data):
        error_count = 0

        for d in received_data:
            if d['title'] not in approved_data:
                print('received title | {0} | not in approved list.'.format(d['title']))
                error_count += 1

        if error_count > 0:
            return False
        else:
            return True

    @staticmethod
    def validate(field, received_data):
        error_count = 0

        for d in received_data:
            if d[field] <= 0:
                print('received data | {0} | < 0 or None.'.format(d[field]))
                error_count += 1

        if error_count > 0:
            return False
        else:
            return True

    @staticmethod
    def validate_all(field, received_data):
        error_count = 0

        for i in range(len(field)):
            for d in received_data:
                if len(str(d[field[i]])) <= 0:
                    print('received data | {0} | {1} |'.format(d[field[i]], field[i]))
                    error_count += 1

        if error_count > 0:
            return False
        else:
            return True

    @staticmethod
    def comparator(quotes, interval_list, received_data):

        error_count = 0

        # проверка на вхождение в интервал
        for d in received_data:
            if d['securityCode'] == quotes:
                # ВАЖНО !!! На бою полей askFormula, bidFormula не будет! Будет ошибка!
                if quotes == 'SBER':
                    # берем цену котировки для SBER\TQBR
                    quotes_price = float(d['askFormula'][:3] + '.00')
                else:
                    # берем цену котировки GOOG\MCT
                    quotes_price = float(d['askFormula'][:4] + '.0000')
                    # берем курс котировки GOOG\MCT
                    quotes_price *= float(d['askFormula'][-11:-9])

                if interval_list['min'] <= quotes_price <= interval_list['max']:
                    pass
                else:
                    error_count += 1
                    print('received value out of year range | min {0} | {1} | max {2} |'.format(
                        interval_list['min'], quotes_price, interval_list['max']))

        return error_count

    @staticmethod
    def validate_interval(quotes_list, interval_list, received_data):

        error_count = 0

        # есть ли искомая котировка в выдаче вообще?
        assert [d for d in received_data if 'SBER' in d['securityCode']]
        assert [d for d in received_data if 'GOOG' in d['securityCode']]

        # проверка на вхождение в интервал
        for i in range(2):
            error_count = Quotes.comparator(quotes_list[i], interval_list[i], received_data)

        if error_count > 0:
            return False
        else:
            return True

    @staticmethod
    def validate_quotes_larger(approved_data, received_data):

        # проверяем что пришло нужное количество котировок
        if len(approved_data) > len(received_data):
            print('the length of the data larger!\n')

            # выбираем все пришедшие котировки
            received_quotes = [d['securityCode'] for d in received_data]

            # находим отсутствующие котировки, выводим, падаем с ошибкой
            _approved_data = set(approved_data)
            _difference = _approved_data.difference(received_quotes)
            print('difference between data sets\n')
            print('approved_data {0} \n'.format(approved_data))
            print('received_data {0} \n'.format(received_quotes))
            print('difference_data {0} \n'.format(_difference))

            return False

        return True

    @staticmethod
    def validate_doubles(field, received_data):

        error_count = 0
        error_message = []

        c = Counter()

        for i in range(2):

            for q in [d[field[i]] for d in received_data]:
                c[q] += 1

            for q in [d[field[i]] for d in received_data]:
                if c[q] != 1:
                    error_count += 1
                    error_message.append('Next field | {0} | have doubles | {1} | {2} |'.format(field[i], q, c[q]))

        for mes in list(set(error_message)):
            print(mes, sep='\n')

        if error_count > 0:
            return False
        else:
            return True
