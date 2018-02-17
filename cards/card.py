class Card:
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}")


'''Each instance of Deck should have a cards attribute with all 52 possible instances of Card.
Deck should have an instance method called count which returns a count of how many cards remain in the deck.
Deck's __repr__ method should display information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
Deck should have an instance method called _deal which accepts a number and removes at most that many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError with the message "All cards have been dealt".
Deck should have an instance method called shuffle which will shuffle a full deck of cards. If there are cards missing from the deck, this method should return a ValueError with the message "Only full decks can be shuffled".
Deck should have an instance method called deal_card which uses the _deal method to deal a single card from the deck.
Deck should have an instance method called deal_hand which accepts a number and uses the _deal method to deal a list of cards from the deck.'''




class Deck:
    def __init__(self):
        self.cards = []
