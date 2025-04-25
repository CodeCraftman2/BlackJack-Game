import random

SUITS = ("hearts", "diamonds", "clubs", "spades")
RANKS = ("two", "three", "four", "five", "six", "seven", "eight", "nine",
         "ten", "jack", "queen", "king", "ace")

VALUES = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
          "eight": 8, "nine": 9, "ten": 10, "jack": 10, "queen": 10,
          "king": 10, "ace": 11}

class Card:
    '''Represents a playing card.'''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]
        self.face_up = True

    def __str__(self):
        return f"Card(suit={self.suit}, rank={self.rank})" if self.face_up else "Card(Face Down)"

    def turn_card_over(self):
        '''Flips the card face up or face down.'''
        self.face_up = not self.face_up


class Deck:
    '''Represents a deck of 52 cards.'''

    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        '''Shuffles the deck.'''
        random.shuffle(self.all_cards)

    def deal(self):
        '''Deals a card from the deck.'''
        return self.all_cards.pop()

    def restack(self):
        '''Restocks the deck when there are less than 10 cards remaining.'''
        if len(self.all_cards) <= 10:
            self.all_cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
            self.shuffle()


class Hand:
    '''Represents a player's or dealer's hand.'''

    def __init__(self, name='Anonymous'):
        self.name = name
        self.cards = []

    def add_card(self, new_card):
        '''Adds a card to the hand.'''
        self.cards.append(new_card)

    def clear_hand(self):
        '''Removes all cards from the hand.'''
        self.cards = []

    def value(self):
        '''Calculates the total value of the hand.'''
        aces = sum(1 for card in self.cards if card.rank == 'ace')
        total = sum(card.value for card in self.cards)

        while aces and total > 21:
            total -= 10
            aces -= 1

        return total

    @classmethod
    def ask_name(cls):
        name = input('Please enter your name: ')
        return cls(name)


class Chip:
    '''Represents a player's chip balance.'''

    def __init__(self, balance=0):
        self.balance = balance
        self.bet = 0

    def add_balance(self, amount):
        '''Increases chip balance.'''
        self.balance += amount

    def remove_balance(self, amount):
        '''Decreases chip balance.'''
        self.balance -= amount

    def clear_bet(self):
        '''Resets the bet amount.'''
        self.bet = 0

    @classmethod
    def ask_balance(cls):
        while True:
            try:
                balance = int(input("Please enter your available balance: "))
                if balance < 0:
                    raise ValueError("Balance cannot be negative!")
            except ValueError as e:
                print(e)
            else:
                return cls(balance)

    def ask_bet(self, round_num):
        while True:
            try:
                bet = int(input(f"How much would you like to bet for Round {round_num}?: "))
                if bet > self.balance or bet <= 0:
                    raise ValueError("Bet must be within your balance!")
            except ValueError as e:
                print(e)
            else:
                self.bet = bet
                break
