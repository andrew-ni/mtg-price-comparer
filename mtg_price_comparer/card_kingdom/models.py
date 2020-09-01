import enum
import re
import typing as t

import bs4

_price_regex = re.compile(r'(\d+) @([.\d]+)')


class Quality(str, enum.Enum):
    NM = 'NM'
    EX = 'EX'
    VG = 'VG'
    G = 'G'


class CardEntry:
    def __init__(self, name: str, set_name: str, quality: Quality, quantity: int, price: float):
        self.name = name
        self.set_name = set_name
        self.quality = quality
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"({self.name} | {self.set_name} | {self.quality} | {self.quantity} | {self.price})"

    def __repr__(self):
        return f"({self.name} | {self.set_name} | {self.quality} | {self.quantity} | {self.price})"


class Card:
    name: str = None
    prices: t.Dict[Quality, t.List[CardEntry]] = {}

    def __init__(self, name: str, entries: t.List[CardEntry] = []):
        self.name = name
        self.prices = {
            Quality.NM: [],
            Quality.EX: [],
            Quality.VG: [],
            Quality.G: [],
        }
        for entry in entries:
            self.add_price_entry(entry)

    def add_price_entries(self, *args: CardEntry):
        for entry in args:
            self.prices[entry.quality].append(entry)

    def get_lowest_price(self, qualities: t.List[Quality] = [], quantity: int = 1):
        pass

    def __str__(self):
        return f"{self.prices}"

    def __repr__(self):
        return f"{self.prices}"


class PriceData:
    def __init__(self, quality: Quality, quantity: int, price: float):
        self.quality = quality
        self.quantity = quantity
        self.price = price

    @classmethod
    def from_td_tag(cls, quality: Quality, tag: bs4.element.Tag):
        try:
            s = tag.find('table').find('tr').find_all('td')[1].find('div').text
            matches = _price_regex.match(s)
            return PriceData(quality=quality, quantity=int(matches[1]), price=float(matches[2]))
        except Exception:
            pass

    def __str__(self):
        return f"{self.quality} {self.quantity} @ {self.price}"
