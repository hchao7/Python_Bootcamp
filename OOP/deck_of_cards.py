import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    def __init__(self):
        self.cards = [Card(suit, value) for suit in Deck.suits for value in Deck.values]
        
    def __repr__(self):
        return f"Deck of {self.count()} cards"
        
    def count(self):
        return len(self.cards)
        
    def _deal(self, num_of_cards):
        if self.count() == 0:
          raise ValueError("All cards have been dealt.")
        elif num_of_cards >= self.count():
          cards = self.cards.copy()
          self.cards.clear()
          return cards
        else:
          cards = self.cards[self.count()-num_of_cards:]
          del self.cards[self.count()-num_of_cards:]
          return cards
        
    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled.")
        random.shuffle(self.cards)
        return self
        
    def deal_card(self):
        return self._deal(1)[0]
        
    def deal_hand(self, num_per_hand):
        return self._deal(num_per_hand)
    
deck1 = Deck()
print(deck1.deal_card())