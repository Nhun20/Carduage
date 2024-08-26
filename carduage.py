import random

class Deck:
    def __init__(self):
        self.cards = self.generate_standard_deck()

    def generate_standard_deck(self):
        suits = ['H', 'D', 'C', 'S']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return [value + suit for suit in suits for value in values]

    def get_card(self, index):
        if 0 <= index < len(self.cards):
            return self.cards[index]
        else:
            raise IndexError(f"Index {index} out of range for deck of size {len(self.cards)}.")

    def move_top_to_bottom(self, n):
        self.cards = self.cards[n:] + self.cards[:n]

    def flip_deck(self):
        self.cards.reverse()

    def cut_deck(self, n):
        top_half = self.cards[:n]
        self.cards = self.cards[n:]
        return top_half

    def peek_top(self, n):
        return self.cards[:n]

    def take_top(self, n):
        taken = self.cards[:n]
        self.cards = self.cards[n:]
        return taken

    def count_cards(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def insert_deck(self, new_deck, pos):
        self.cards = self.cards[:pos] + new_deck + self.cards[pos:]

    def __str__(self):
        return ', '.join(self.cards)
