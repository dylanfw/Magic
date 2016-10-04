"""
21 Card Trick in Python
~~~~~~~~~~~~~~~~~~~~~~~~
Think of a card from any of the rows displayed.
Input only the row number that your card is in.
Be amazed.
"""
import random

class Card():
    suits = ['C', 'H', 'S', 'D']
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_name(self):
        if self.value == 1:
            return "A"
        elif self.value == 11:
            return "J"
        elif self.value == 12:
            return "Q"
        elif self.value == 13:
            return "K"
        return str(self.value)

    def __str__(self):
        return "%s%s" % (self.get_name(), self.suit)

class Deck():
    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for value in xrange(13):
                self.cards.append(Card(value+1, suit))

    def shuffle(self):
        random.shuffle(self.cards)

deck = Deck()
deck.shuffle()
packet = deck.cards[:21]

for _ in xrange(3):
    first  = []
    second = []
    third  = []
    for i in xrange(0,21,3):
        first.insert(0, packet[i])
        second.insert(0, packet[i+1])
        third.insert(0, packet[i+2])
    packet = []

    print "1: " + " ".join([str(card) for card in first])
    print "2: " + " ".join([str(card) for card in second])
    print "3: " + " ".join([str(card) for card in third])

    selection = int(raw_input("> "))
    if selection == 1:
        packet.extend(second)
        packet.extend(first)
        packet.extend(third)
    elif selection == 2:
        packet.extend(first)
        packet.extend(second)
        packet.extend(third)
    elif selection == 3:
        packet.extend(first)
        packet.extend(third)
        packet.extend(second)

print "You're thinking of the %s" % packet[10]
