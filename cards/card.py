class Card:
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}")


class Deck:
    def __init__(self, count):
        self.cards = []
