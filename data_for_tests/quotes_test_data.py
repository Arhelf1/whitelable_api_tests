# fields names
security_code = 'securityCode'
security_board = 'securityBoard'

# globals
url = 'Quotes'
path_to_json = 'json_schemes/quotes.json'

# Годовой интервал торгов
interval_list = [{"max": 290.00, "min": 200.00},
                 {"max": 90000.0000, "min": 75000.0000}]

# список полей для проверки на диапазон
fields_list = ['ask', 'bid']

# список полей для проверки на дубли
doubles_fields_list = ['securityCode', 'title']

# Список котировок
quotes_list = ['SBER', 'GOOG']

# надбавки для цен котировок
tqbr_increase = 20
mct_increase = 6000

# список кодов бирж доступных для партнеров
partners_approve_exchanges = ["TQBR", "MCT", "SPFEQ"]


security_settings_approve_quotes = ["T", "BAC", "AAPL", "MSFT", "EBAY", "TSLA", "CVX", "FB", "MS", "AMZN", "BA", "CSCO", "KO",
                                    "XOM", "FSLR", "SBUX", "NEM", "MCD", "PFE", "WMT", "PG", "JNJ", "DIS", "GE", "F", "AA",
                                    "MU", "TIF", "INTC", "IBM", "GILD", "QCOM", "NFLX", "V", "CME", "ETFC", "MET", "DAL", "CAT",
                                    "NRG", "EXC", "PM", "VZ", "CHK", "VLO", "CBS", "ABBV", "PYPL", "GOOG", "GAZP", "LKOH",
                                    "SBER", "ROSN", "MTSS", "RTKM", "AVAZ", "ALRS", "APTK", "AFKS", "AFLT", "VTBR", "BSPB",
                                    "BANE", "SIBN", "GMKN", "LSRG", "IRAO", "KMAZ", "MGNT", "MTLR", "MAGN",
                                    "MOEX", "MSTT", "MSNG", "MRKC", "NLMK", "NVTK", "OGKB", "PIKK", "PLZL", "PRTK",
                                    "RASP", "RSTI", "HYDR", "SBERP", "CHMF", "SVAV", "SNGSP", "SNGS", "TATN", "URKA", "PHOR",
                                    "FEES", "UPRO", "GCHE", "VZRZ", "MFON", "PSBR"]


# список кодов котировок доступный для партнера
partners_approve_quotes = ["T", "BAC", "AAPL", "MSFT", "EBAY", "TSLA", "CVX", "FB", "MS", "AMZN", "BA", "CSCO", "KO",
                           "XOM", "FSLR", "SBUX", "NEM", "MCD", "PFE", "WMT", "PG", "JNJ", "DIS", "GE", "F", "AA",
                           "MU", "TIF", "INTC", "IBM", "GILD", "QCOM", "NFLX", "V", "CME", "ETFC", "MET", "DAL", "CAT",
                           "NRG", "EXC", "PM", "VZ", "CHK", "VLO", "CBS", "ABBV", "PYPL", "GOOG", "GAZP", "LKOH",
                           "SBER", "ROSN", "MTSS", "RTKM", "AVAZ", "ALRS", "APTK", "AFKS", "AFLT", "VTBR", "BSPB",
                           "BANE", "SIBN", "GMKN", "LSRG", "IRAO", "KMAZ", "MGNT", "MTLR", "MAGN",
                           "MOEX", "MSTT", "MSNG", "MRKC", "NLMK", "NVTK", "OGKB", "PIKK", "PLZL", "PRTK",
                           "RASP", "RSTI", "HYDR", "SBERP", "CHMF", "SVAV", "SNGSP", "SNGS", "TATN", "URKA", "PHOR",
                           "FEES", "UPRO", "GCHE"]

# список полного названия бумаги
tiker_title = ["AT&T INC.", "Bank of America Corporation", "Apple Inc.", "Microsoft Corporation", "eBay Inc.",
               "Tesla Motors, Inc.", "Chevron Corporation", "Facebook, Inc.", "Morgan Stanley", "Amazon.com, Inc.",
               "THE BOEING COMPANY", "Cisco Systems, Inc.", "THE COCA-COLA COMPANY", "Exxon Mobil Corporation",
               "First Solar, Inc.", "Starbucks Corporation", "NEWMONT MINING CORPORATION", "Mc'DONALDS CORPORATION",
               "Pfizer Inc.", "Wal-Mart Stores, Inc.", "The Procter & Gamble Company", "Johnson & Johnson",
               "The Walt Disney Company", "General Electric Company", "Ford Motor Company", "Alcoa Inc",
               "Micron Technology, Inc.", "Tiffany & Co.", "Intel Corporation",
               "INTERNATIONAL BUSINESS MACHINES CORPORATION", "GILEAD SCIENCES, INC.", "QUALCOMM Incorporated",
               "Netflix, Inc.", "Visa Inc.", "CME GROUP INC.", "E*TRADE Financial Corporation", "MetLife, Inc.",
               "Delta Air Lines, Inc.", "Caterpillar Inc.", "NRG Energy, Inc.", "Exelon Corporation",
               "Philip Morris International Inc.", "Verizon Communications Inc.", "Chesapeake Energy Corporation",
               "Valero Energy Corporation", "CBS Corporation", "AbbVie Inc.", "PayPal Holdings, Inc.",
               "Alphabet Inc. Class C", "ГАЗПРОМ", "ЛУКойл НК", "Сбербанк", "Роснефть НК", "МТС", "Ростелеком",
               "АВТОВАЗ ао", "АЛРОСА ао", "Аптечная сеть 36,6 ао", 'АФК "Система" ао', "Аэрофлот ао", "Банк ВТБ ао",
               "Банк Санкт-Петербург", "Башнефть ао", "Газпром нефть ао", "ГМК НорНикель ао", "Группа ЛСР ао",
               "Группа Черкизово ао", "Интер РАО ао", "КАМАЗ ао", "Магнит ао", "Мечел ао", "ММК ао",
               "Московская Биржа ао", "МОСТОТРЕСТ ао", "МосЭнерго ао", "МосЭнерго ао", "НЛМК ао", "НОВАТЭК ао",
               "ОГК-2 ао", "ПИК ао", "Полюс ао", "ПРОТЕК ао", "Распадская ао", "Российские сети ао", "РусГидро ао",
               "Сбербанк ап", "Северсталь ао", "СОЛЛЕРС ао", "Сургутнефтегаз ап", "Сургутнефтегаз ао", "Татнефть ао",
               "Уралкалий ао", "ФосАгро ао", "ФСК ЕЭС ао", "Юнипро ао", "МРСК Центра ао"]
