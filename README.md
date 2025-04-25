# Blackjack Card Game Framework

## Overview

This repository contains a basic framework for creating and playing card games, with a focus on implementing a simple Blackjack game. The framework is designed to be extendable and reusable, making it suitable for supporting other card games in the future. 

Blackjack is a popular card game where the goal is to achieve a hand value as close to 21 as possible without exceeding it. Players compete against a dealer, following specific rules for drawing cards.

---

## Features

### 1. Card and Deck Management
- **Card Class**: Represents a single playing card with a suit (Hearts, Diamonds, Clubs, Spades) and a rank (Ace, 2-10, Jack, Queen, King).
- **Deck Class**:
  - Generates a full deck of 52 cards.
  - Includes functionality to shuffle the deck randomly.
  - Allows drawing cards from the deck, removing them after each draw.

---

### 2. Simple Blackjack Game
- **Game Rules**:
  - Players aim to get as close to 21 points as possible without exceeding it (bust).
  - Face cards (King, Queen, Jack) are worth 10 points.
  - Aces can be worth 1 or 11 points, depending on the player's benefit.
- **Gameplay**:
  - Both the dealer and the player start with two cards.
  - Players can choose to "hit" (draw another card) or "stand" (stop drawing cards).
  - The dealer must follow fixed rules:
    - Hit on 16 or below.
    - Stand on 17 or above.
  - The player wins if their hand's total is higher than the dealer's without exceeding 21.

---

### 3. Multiplayer Support
- Extend the game to include multiple players.
- Players take turns making decisions (hit or stand).
- Turn-based system for managing player actions and game progression.
- Display player hands and game status after each round.

---

### End Conditions
1. **Immediate Loss**: A player busts (hand value exceeds 21).
2. **Immediate Win**: The dealer busts (hand value exceeds 21).
3. **Final Comparison**: After all players stand, the dealer plays their turn, and results are compared.

---

## Basic Rules of Blackjack
- The goal is to get as close to 21 as possible without going over.
- Face cards (King, Queen, Jack) = 10 points.
- Aces (A) = 1 or 11 points, depending on what benefits the player.
- If your total is higher than the dealer’s without busting, you win.
- If you go over 21, you automatically lose (bust).
- The dealer must hit if they have 16 or less and stand on 17 or more.

---

## Example Scenarios
### Single Player
- **Player’s Hand**: [Card(Hearts, 10), Card(Clubs, 7)]  
  **Total**: 17  
- **Dealer’s Hand**: [Card(Spades, 8), Card(Diamonds, 10)]  
  **Total**: 18  
- **Result**: Dealer wins.

---

### Multiplayer
- **Player 1 Hand**: [Card(Hearts, 7), Card(Spades, 5)]  
- **Player 2 Hand**: [Card(Diamonds, 9), Card(Clubs, 6)]  
- **Player 1 Hits**: Receives Card(Hearts, 3).  
  **Updated Hand**: [Card(Hearts, 7), Card(Spades, 5), Card(Hearts, 3)] (Total = 15).

---

## Setup and Running the Game
### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/CodeCraftman2/BlackJack-Game
   ```
2. Navigate to the project directory:
   ```bash
   cd BlackJack-Game
   ```

### Running the Game
- Execute the main game file:
  ```bash
  python blackjack.py
  ```
  or
  ```bash
  python3 blackjack.py
  ```

---

## Future Enhancements
- Add support for other card games like Poker or Rummy.
- Include a graphical user interface (GUI) for improved user interaction.
- Implement betting mechanics and player leaderboard.

---

## Contributing
Contributions are welcome! If you have ideas for improving the framework or adding new features, feel free to fork the repository and submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
This project was developed as part of a learning exercise at the **Institute of Technical Education & Research, SOA, Deemed to be University**.
