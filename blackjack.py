# blackjack.py

import os
import Card
import game

def main():
    '''
    This function contains the game logic.
    '''
    print('Welcome to BlackJack!')

    hand_player = Card.Hand.ask_name()
    hand_dealer = Card.Hand('Dealer')
    chips_player = Card.Chip.ask_balance()

    new_deck = Card.Deck()
    new_deck.shuffle()

    round_on = True
    round_num = 0

    while round_on:
        os.system('cls' if os.name == 'nt' else 'clear')

        if chips_player.balance <= 0:
            print("You're out of balance! Game over!")
            break

        hand_player.clear_hand()
        hand_dealer.clear_hand()
        chips_player.clear_bet()

        new_deck.restack()
        round_num += 1
        print(f"Round {round_num} begins!")
        print(f"Available Balance: {chips_player.balance}")

        chips_player.ask_bet(round_num)

        for _ in range(2):
            hand_player.add_card(new_deck.deal())
            hand_dealer.add_card(new_deck.deal())

        hand_dealer.cards[1].turn_card_over()

        game.display_cards(hand_player, hand_dealer)

        if game.player_turn(hand_player, hand_dealer, chips_player, new_deck):
            game.dealer_turn(hand_player, hand_dealer, chips_player, new_deck)

        round_on = game.choice_to_continue()

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Thank you for playing! Your final balance is {chips_player.balance}")

if __name__ == '__main__':
    main()
    input("Press ENTER to exit.......")