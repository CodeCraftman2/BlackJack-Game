# game.py

def player_turn(hand_player, hand_dealer, chip, deck):
    '''Handles the player's turn, checking for busts or decisions.'''
    while True:
        choice = player_choice(hand_player, chip)

        if choice == 'S':
            print("You decided to Stand.")
            return True

        if choice == 'H':
            hand_player.add_card(deck.deal())
            print("You decided to Hit!")
            display_cards(hand_player, hand_dealer)

            if hand_player.value() > 21:
                print(f"{hand_player.name} busted! Dealer wins!")
                chip.remove_balance(chip.bet)
                return False

        if choice == 'DD':
            chip.bet *= 2
            hand_player.add_card(deck.deal())
            print("You chose Double Down!")
            display_cards(hand_player, hand_dealer)

            if hand_player.value() > 21:
                print(f"{hand_player.name} busted! Dealer wins!")
                chip.remove_balance(chip.bet)
                return False

            return True

def player_choice(hand_player, chip):
    '''Prompts the player to make a choice: Hit, Stand, or Double Down.'''
    while True:
        choice = input(f"{hand_player.name}, would you like to (H)it, (S)tand, or (DD)ouble Down? ").upper()
        if choice in ['H', 'S', 'DD']:
            return choice
        else:
            print("Invalid choice! Please choose 'H' for Hit, 'S' for Stand, or 'DD' for Double Down.")

def display_cards(hand_player, hand_dealer):
    '''Displays the cards of the player and the dealer.'''
    print("\nPlayer's Hand:")
    print([str(card) for card in hand_player.cards])
    print(f"Total value: {hand_player.value()}")

    print("\nDealer's Hand:")
    print([str(card) for card in hand_dealer.cards])
    print(f"Total value: {hand_dealer.value() if hand_dealer.cards[1].face_up else 'Hidden'}")
# to continue the game

def choice_to_continue():
    '''Prompts the player to decide whether to continue playing or not.'''
    while True:
        choice = input("Would you like to play another round? (Y/N): ").upper()
        if choice in ['Y', 'N']:
            return choice == 'Y'
        else:
            print("Invalid choice! Please choose 'Y' for Yes or 'N' for No.")

def dealer_turn(hand_player, hand_dealer, chip, deck):
    '''Handles the dealer's turn, enforcing the 16/17 rule.'''
    hand_dealer.cards[1].turn_card_over()
    display_cards(hand_player, hand_dealer)

    while hand_dealer.value() < 17:
        hand_dealer.add_card(deck.deal())
        print("Dealer hits!")
        display_cards(hand_player, hand_dealer)

    if hand_dealer.value() > 21:
        print("Dealer busts! Player wins!")
        chip.add_balance(chip.bet)
    elif hand_dealer.value() > hand_player.value():
        print("Dealer wins!")
        chip.remove_balance(chip.bet)
    elif hand_dealer.value() < hand_player.value():
        print("Player wins!")
        chip.add_balance(chip.bet)
    else:
        print("It's a push!")