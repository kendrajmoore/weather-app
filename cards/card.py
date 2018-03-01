from random import shuffle


class Card:
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(value, suit) for suit in suits for value in values]
        print(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
