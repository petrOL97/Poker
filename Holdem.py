import random

class Card:
    """playing card object with rank and suit"""

    def __init__(self, rank, suit):
       self.rank = rank
       self.suit = suit
       self.ranks = (None, "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King")
       self.suits = {"d": "Diamonds",
                     "c": "Clubs",
                     "h": "Hearts",
                     "s": "Spades"}

    def __str__(self):
        return "%s of %s" % (self.ranks[self.rank], self.suits.get(self.suit))

    def __lt__(self, other):
        return self.rank < other.rank

    def getRank(self):
        """returns the rank of the card"""
        return self.ranks[self.rank]

    def getSuit(self):
        return self.suits.get(self.suit)

deck = [None]
for i in range(1, 14):
    deck.append(Card(i, "d"))
    deck.append(Card(i, "c"))
    deck.append(Card(i, "h"))
    deck.append(Card(i, "s"))

hand = random.sample(deck, 7)
hand = sorted(hand)
for i in range(0,7):
    print(hand[i])

def combination(hand):
    ranks = [None]
    suits = [None]
    for i in hand:  
        ranks.append(i.getRank())
        suits.append(i.getSuit())

    def high_card(ranks):
        if "Ace" in ranks:
            print("High card: Ace")
        else:
            print("High card: " + ranks[-1])
    high_card(ranks)
combination(hand)
