from deck import Deck, Card

class Hand:
    """
    Represents a hand of 5 cards dealt from a deck.
    """

    def __init__(self, deck):
        """
        Initializes the hand by dealing 5 cards from the given deck.

        :param deck: An instance of Deck from which to deal cards.
        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())  # Deal one card at a time
        self._cards = cards

    @property
    def cards(self):
        """
        :return: The list of 5 Card objects in the hand.
        """
        return self._cards

    @property
    def is_flush(self):
        """
        Checks if all cards have the same suit.

        :return: True if the hand is a flush, False otherwise.
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def num_matches(self):
        """
        Counts the number of rank matches in the hand.

        For example:
            - 1 pair → 2 matches
            - 2 pair → 4 matches
            - trips → 6 matches
            - full house → 8 matches
            - quads → 12 matches

        :return: Total number of rank matches in the hand.
        """
        matches = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        :return: True if the hand contains exactly one pair.
        """
        return self.num_matches == 2

    @property
    def is_2_pair(self):
        """
        :return: True if the hand contains exactly two pairs.
        """
        return self.num_matches == 4

    @property
    def is_trips(self):
        """
        :return: True if the hand contains three cards of the same rank.
        """
        return self.num_matches == 6

    @property
    def is_quads(self):
        """
        :return: True if the hand contains four cards of the same rank.
        """
        return self.num_matches == 12

    @property
    def is_full_house(self):
        """
        :return: True if the hand contains a full house (3 of a kind + a pair).
        """
        return self.num_matches == 8

    @property
    def is_straight(self):
        """
        Checks if the hand contains five consecutive ranks and no duplicates.

        :return: True if the hand is a straight, False otherwise.
        """
        if self.num_matches != 0:
            return False  # Straights cannot contain duplicate ranks

        self.cards.sort()  # Sorts by rank
        start_index = Card.RANKS.index(self.cards[0].rank)
        end_index = Card.RANKS.index(self.cards[4].rank)
        return start_index + 4 == end_index

    def __str__(self):
        """
        :return: String representation of the hand.
        """
        return str(self._cards)


# Example

matches = 0  # Count how many straights are found
count = 0    # Total number of hands checked

while matches < 10000:
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)  # Deal a new hand of 5 cards
    count += 1

    if hand.is_straight:
        print(hand)  # Print the straight hand
        matches += 1
        break  # Stop after finding 1 straight

print(f"The probability of a straight is: {100 * matches / count}%") # Print estimated probability