import random

class Card:
    """
    Represents a single playing card with a rank and suit.
    """
    # Possible ranks and suits
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS = ['♠', '♣', '♦', '♥']

    def __init__(self, rank, suit):
        """
        Initialize a Card with a rank and a suit.

        :param rank: A string representing the rank
        :param suit: A string representing the suit
        :raises ValueError: If rank or suit is invalid.
        """
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        """Get the rank of the card."""
        return self._rank

    @property
    def suit(self):
        """Get the suit of the card."""
        return self._suit

    def __str__(self):
        """
        Return a string representation of the card.
        """
        return f"{self._rank} {self._suit}"

    def __repr__(self):
        """
        Return a string suitable for debugging and display in lists.
        """
        return f"{self._rank} {self._suit}"

    def __eq__(self, other):
        """
        Define equality based on rank only (not suit).

        :param other: Another card instance.
        :return: True if ranks are equal.
        """
        return self.rank == other.rank

    def __lt__(self, other):
        """
        Define less-than comparison based on rank order.

        :param other: Another card instance.
        :return: True if this card's rank is less than the other's.
        """
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)


class Deck:
    """
    Represents a standard 52-card deck.
    """

    def __init__(self):
        """
        Initialize the deck with 52 unique cards (one for each rank-suit combination).
        """
        self._cards = [Card(r, s) for r in Card.RANKS for s in Card.SUITS]

    @property
    def cards(self):
        """
        Get the list of cards in the deck.
        """
        return self._cards

    def __str__(self):
        """
        Return a string representation of the entire deck.
        """
        return str(self._cards)

    def shuffle(self):
        """
        Shuffle the deck in place using Python's built-in random.shuffle().
        """
        random.shuffle(self._cards)

    def deal(self):
        """
        Deal the top card from the deck.
        :return: A Card object.
        """
        return self.cards.pop(0)

    def __len__(self):
        """
        Return the number of cards remaining in the deck.
        """
        return len(self._cards)

    def __getitem__(self, position):
        """
        Enable indexing into the deck.
        :param position: Index of the card to retrieve.
        :return: A Card object.
        """
        return self._cards[position]

# Example
if __name__ == '__main__':
    # Create a card: Ace of Spades
    c1 = Card('A', '♠')
    print(c1)
    print(c1.suit)

    deck = Deck() # Create a deck and print it
    print(deck.cards)  # Prints the entire unshuffled deck

    deck.shuffle() # Shuffle the deck
    print(deck)  # Prints the shuffled deck

    print(deck.deal())  # Deals the top card and prints it

    print(deck) # Print the deck after dealing one card