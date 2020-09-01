import typing as t

import mtg_price_comparer.card_kingdom.models as ck
import mtg_price_comparer.models as core


def get_url(cards_list: t.List[core.CardEntry]) -> str:
    url = 'https://www.cardkingdom.com/builder/mtg?maindeck='
    for (i, card_entry) in enumerate(cards_list):
        url += f"{card_entry.quantity}+{card_entry.name.replace(' ', '+')}"
        if i < len(cards_list) - 1:
            url += '%0D%0A'
    return url + '&format=all'


def get_cards(cards: t.List[core.CardEntry]) -> t.List[ck.Card]:
    pass


def get_cards_from_html(html: str) -> t.List[ck.Card]:
    pass
