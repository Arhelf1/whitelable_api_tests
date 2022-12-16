from helpers.quotes import Quotes
from helpers.order_buy import OrderBuy
from helpers.order_create_sell import OrderCreateSell
from helpers.order_confirm_sell import OrderConfirmSell
from helpers.v2_registration import V2Registration
from helpers.files import Files


class Model:
    def __init__(self):
        self.quotes = Quotes()
        self.order_buy = OrderBuy()
        self.order_create_sell = OrderCreateSell()
        self.order_confirm_sell = OrderConfirmSell()
        self.v2_registration = V2Registration()
        self.files = Files()
