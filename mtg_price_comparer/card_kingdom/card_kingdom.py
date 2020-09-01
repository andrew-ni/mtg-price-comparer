import typing as t

import bs4
import requests

import mtg_price_comparer.card_kingdom.models as ck
import mtg_price_comparer.core as core


def get_cards(cards: t.List[core.CardEntry]) -> t.Dict[str, ck.Card]:
    url = _get_url(cards)
    response = requests.get(url)
    return _get_cards_from_html(cards, response.text)


def _get_url(cards: t.List[core.CardEntry]) -> str:
    url = 'https://www.cardkingdom.com/builder/mtg?maindeck='
    for (i, card_entry) in enumerate(cards):
        url += f"{card_entry.quantity}+{card_entry.name.replace(' ', '+')}"
        if i < len(cards) - 1:
            url += '%0D%0A'
    return url + '&format=all'


def _get_cards_from_html(input_cards: t.List[core.CardEntry], html: str) -> t.Dict[str, ck.Card]:
    soup = bs4.BeautifulSoup(html, 'html.parser')
    rows = soup.find(class_="table").find('tr', recursive=False).find('tr', recursive=False).find_all('tr', recursive=False)
    table = []
    for row in rows:
        table.append(row.findAll('td', recursive=False))

    cards = {}
    card: ck.Card = None
    row: t.List[bs4.element.Tag]
    for row in table:
        card_name = row[1].text.strip()     # can be ''
        set_name = row[5].text.strip()      # always exists
        nm = ck.PriceData.from_td_tag(ck.Quality.NM, row[7])    # can be None
        ex = ck.PriceData.from_td_tag(ck.Quality.EX, row[8])    # can be None
        vg = ck.PriceData.from_td_tag(ck.Quality.VG, row[9])    # can be None
        g = ck.PriceData.from_td_tag(ck.Quality.G, row[10])     # can be None

        if card_name != '':
            card = cards[card_name] = ck.Card(card_name)

        entries = _get_entries(card_name, set_name, nm, ex, vg, g)
        card.add_price_entries(*entries)

    from pprint import pprint
    pprint(cards)
    return cards


def _get_entries(name, set_name, *args: ck.PriceData) -> t.List[ck.CardEntry]:
    entries = []
    for data in args:
        if data is not None:
            entries.append(ck.CardEntry(
                name=name,
                set_name=set_name,
                quality=data.quality,
                quantity=data.quantity,
                price=data.price))
    return entries
