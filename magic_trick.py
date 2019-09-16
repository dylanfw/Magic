""" A Python implementation of the "21 Card Trick" """
import random


class Card:
    suits = ["Clubs", "Hearts", "Spades", "Diamonds"]

    def __init__(self, value, suit):
        if value not in range(1, 14):
            raise ValueError("Card value must be integer from 1 to 13")
        if suit not in self.suits:
            raise ValueError(f"Suit must be one of {self.suits}")

        self.value = value
        self.suit = suit

    @property
    def display_value(self):
        named_values = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        return named_values.get(self.value, self.value)

    def __repr__(self):
        return f"{self.display_value} of {self.suit}"


def perform_trick():
    """
    Twenty one cards are displayed in three rows of seven.
    A spectator mentally selects a card and reveals only which row their card is in.
    The three rows are gathered together and laid back down in a new order.
    The spectator reveals again which row their card has been moved into.
    After three times, the magician (or computer) reveals the identity of the
    spectator's thought of card.
    """
    deck = [Card(val, suit) for val in range(1, 14) for suit in Card.suits]
    random.shuffle(deck)

    packet = deck[:21]

    for _ in range(3):
        first_packet = []
        second_packet = []
        third_packet = []
        for i in range(0, 21, 3):
            first_packet.insert(0, packet[i])
            second_packet.insert(0, packet[i + 1])
            third_packet.insert(0, packet[i + 2])
        packet = []

        print("\n\n")
        print("In which row does your card appear?")
        print("1: " + ", ".join([str(card) for card in first_packet]) + "\n")
        print("2: " + ", ".join([str(card) for card in second_packet]) + "\n")
        print("3: " + ", ".join([str(card) for card in third_packet]) + "\n")

        selection = int(input("> "))
        packet = collect_packets(selection, first_packet, second_packet, third_packet)

    print("You are thinking of the %s" % packet[10])


def collect_packets(row, *packets):
    """
    Given a row (1, 2, or 3) and three packets:
    assemble them such that the selected packet is sandwiched in the middle.
    Return the new complete packet of cards.
    """
    if len(packets) != 3 or 1 > row > 3:
        raise ValueError(
            "collect_packets expects a 'row' value from 1-3 and three packets"
        )

    if row == 1:
        return packets[1] + packets[0] + packets[2]
    if row == 2:
        return packets[0] + packets[1] + packets[2]
    return packets[0] + packets[2] + packets[1]


if __name__ == "__main__":
    perform_trick()
