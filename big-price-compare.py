import sys

import bs4
import requests


def main():
    filepath = sys.argv[1]
    cards = get_cards_from_file(filepath)
    print(cards)
    card_kingdom_url = 'https://www.cardkingdom.com/builder/mtg?maindeck=4+Ancient+Den%0D%0A2+Arcbound+Ravager%0D%0A4+Welding+Jar%0D%0A4+Ornithopter&format=all'
    print(card_kingdom_url)
    response = requests.get(card_kingdom_url)
    print(response.status_code)
    # print(response.text)


def get_cards_from_file(filepath):
    cards = []
    with open(filepath) as f:
        lines = f.readlines()

    for line in lines:
        tokens = line.strip().split(' ', 1)
        cards.append((tokens[0], tokens[1]))

    return cards


def get_card_kingdom_url(cards_list):
    url = 'https://www.cardkingdom.com/builder/mtg?maindeck='
    for (i, card) in enumerate(cards_list):
        url += f"{card[0]}+{card[1].replace(' ', '+')}"
        if (i < len(cards_list) - 1):
            url += '%0D%0A'
    return url + '&format=all'


if __name__ == "__main__":
    main()
