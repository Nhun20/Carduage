import random

class Deck:
    def __init__(self):
        suits = ['S', 'H', 'D', 'C']  
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [f"{rank}{suit}" for suit in suits for rank in ranks]
        self.cards += ["J1", "J2", "J3"]  
        random.shuffle(self.cards)  

    def move_top_to_bottom(self, n=1):
        if n > 0 and n <= len(self.cards):
            self.cards = self.cards[n:] + self.cards[:n]

    def flip_deck(self):
        self.cards.reverse()

    def cut_deck(self, n):
        if n >= 0 and n <= len(self.cards):
            new_deck = self.cards[:n]
            self.cards = self.cards[n:]
            return new_deck

    def peek_top(self, n=1):
        return self.cards[:n] if n > 0 else []

    def take_top(self, n=1):
        if n > 0 and n <= len(self.cards):
            top_cards = self.cards[:n]
            self.cards = self.cards[n:]
            return top_cards

    def count_cards(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def insert_deck(self, new_deck, pos):
        if 0 <= pos <= len(self.cards):
            self.cards = self.cards[:pos] + new_deck + self.cards[pos:]

    def __str__(self):
        return ", ".join(self.cards)
