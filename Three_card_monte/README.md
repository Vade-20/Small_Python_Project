# Three-Card Monte Game

This is a simple text-based implementation of the classic Three-Card Monte game using Python's curses library. The goal of the game is to find the Queen of Hearts among three shuffled cards.

## How to Play

1. Run the Python script to start the game.
2. You will be presented with three face-down cards on the screen, and one of them is the Queen of Hearts (the others are random cards).
3. The cards will be shuffled and moved around on the screen.
4. Pay close attention to the movements of the cards and try to keep track of the Queen of Hearts.
5. After the shuffling, you will be prompted to enter the number of the card that you believe is the Queen of Hearts (1, 2, or 3).
6. If you choose correctly, you win and proceed to the next level with increased speed.
7. If you choose incorrectly, the game will end, and you can try again.

## Game Controls

- Use any key to start the game.
- Use the number keys (1, 2, 3) to make your guess when prompted.

## Game Features

- The game starts with a speed level of 1 and increases with each successful guess.
- The cards are shuffled and moved randomly to increase the challenge.
- The game keeps track of your score, and you can see your progress as you win levels.

## Dependencies

This game uses the `curses` library, which is typically available by default on most Unix-based systems. You may need to install additional dependencies if you are using Windows.

## Code Structure

The code is divided into several functions for readability and maintainability. Here's a brief overview:

- `random_card()`: Generates a random list of three cards with one Queen of Hearts.
- `resting(cards=None)`: Formats and displays the cards on the screen.
- `printing_cards(stdsrc)`: Displays the initial cards with instructions.
- `printing_moving_cards(stdsrc)`: Displays the cards during shuffling.
- `main(stdsrc)`: The main game loop that handles gameplay logic, card movements, and user input.

