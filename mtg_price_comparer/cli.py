import re
import sys

import mtg_price_comparer.card_kingdom.card_kingdom as ck
import mtg_price_comparer.core as core


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
        cards.append(core.CardEntry(tokens[1], tokens[0]))

    return cards


def main():
    filepath = sys.argv[1]
    input_cards = get_cards_from_file(filepath)
    ck.get_cards(input_cards)


if __name__ == "__main__":
    main()
