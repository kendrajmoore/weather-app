from random import shuffle

class Deck:
    def_init_(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', ]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def deal(self):
        if len(self.card) == 0:
            print("sorry no cards")
        return self.cards.pop()

    def shuffle(self):
        if len(self.cards) < 52:
            print("You messed up")
        shuffle(self.card)
        return self


class Card:
    def_init_(self, suit, value):
        self.suit = suit
        self.value = value
