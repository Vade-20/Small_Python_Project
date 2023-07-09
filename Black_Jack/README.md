# Blackjack Game

This is a simple text-based implementation of the Blackjack game in Python.

## Rules

The rules of the Blackjack game are described in the `rules()` function. You can read the rules by running the `rules()` function.

## Classes

### Members

- The `Members` class represents the base class for both the dealer and the player. It contains common attributes and methods used by both.

### Dealer

- The `Dealer` class represents the dealer in the Blackjack game. It inherits from the `Members` class and includes additional methods specific to the dealer's actions.

### Player

- The `Player` class represents the player in the Blackjack game. It also inherits from the `Members` class and includes methods for the player's actions.

## Functions

- `random_card()`: This function returns a randomly selected card from the deck.

- `printing_format()`: This function prints the current state of the game, including the dealer's and player's cards.

## How to Play

1. Run the code.
2. If you want to read the rules, enter 'Y' or 'y' when prompted.
3. The game starts with a default total money of $10,000.
4. Enter the amount you want to bet. The valid range is from 1 to your total money.
5. Follow the prompts to choose your action:
   - 'H' or 'h' for Hit (draw another card)
   - 'S' or 's' for Stand (end your turn)
   - 'D' or 'd' for Double Down (double your bet and draw one more card)
   - 'Y' or 'y' for Yield (surrender and get back half of your bet)
6. The game will continue until you run out of money or choose to quit.
7. If you decide to quit, the game will display your final total money.

## Note

This implementation uses a text-based interface and simulates the game with a simplified deck of cards. The game follows the basic rules of Blackjack but may not include all the features found in a real casino game.

