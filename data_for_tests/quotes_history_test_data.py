url = 'Quotes/GetHistory'
path_to_json = 'json_schemes/quotes_history.json'

# количество свечек
CandleCount = 3

# Список полей ответа который проверяем на пустоту
receive_field_list = ["open", "high", "low", "close", "date"]


# get body for post request
def get_body(board, tiker, time, candle_count=-3, count=1):
    return {"SecurityBoard": board,
            "SecurityCode": tiker,
            "CandleCount": candle_count,
            "TimeFrame": {
                "Count": count,
                "TimeUnit": time
                }
            }
