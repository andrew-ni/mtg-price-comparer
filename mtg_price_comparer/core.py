import re
import sys

import bs4
import requests

import mtg_price_comparer.card_kingdom.card_kingdom as ck


class CardEntry:
    name: str = None
    quantity: int = None

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


def main():
    filepath = sys.argv[1]
    cards = get_cards_from_file(filepath)
    card_kingdom_url = ck.get_url(cards)
    # print(card_kingdom_url)
    response = requests.get(card_kingdom_url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    rows = soup.find(class_="table").find('tr', recursive=False).find('tr', recursive=False).find_all('tr', recursive=False)
    output = []
    for row in rows:
        output.append(row.findAll('td', recursive=False))

    print(len(output), output)
    # print(response.text)
    # print(soup.prettify())


def get_cards_from_file(filepath):
    cards = []
    pattern = re.compile(r"^(\d+) (.*)$")
    with open(filepath) as f:
        lines = f.readlines()

    for line in lines:
        if not pattern.match(line):
            print(f"Not valid: {line}")
            continue
        tokens = line.strip().split(' ', 1)
        cards.append(CardEntry(tokens[1], tokens[0]))

    return cards

# def get_card_kingdom_regex(card_entry: CardEntry, html: str):
#     pattern = re.compile(fr"{card_entry.name}(.|\s)*?(\d+) @(.|\s)*?([\d.]+)")
#     matches = pattern.search(html)
#     quantity = matches.group(2)
#     price = matches.group(4)
#     print(card_entry.name, quantity, price)


if __name__ == "__main__":
    main()
