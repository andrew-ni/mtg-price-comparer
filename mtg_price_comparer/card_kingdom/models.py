import enum
import typing as t


class Quality(str, enum.Enum):
    NM = 'NM'
    EX = 'EX'
    VG = 'VG'
    G = 'G'


class CardEntry:
    set_name: str = None
    quality: Quality = None
    quantity: int = None
    price: float = None

    def __init__(self, set_name: str, quality: Quality, quantity: int, price: float):
        self.set_name = set_name
        self.quality = quality
        self.quantity = quantity
        self.price = price


class Card:
    name: str = None
    prices: t.Dict[Quality, t.List[CardEntry]] = {}

    def get_lowest_price(self, quality=None, quantity=1):
        pass
