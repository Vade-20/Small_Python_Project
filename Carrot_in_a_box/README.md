# Carrot in a Box Game

The **Carrot in a Box** game is a simple bluffing game for two human players. Each player has a box, and one of the boxes contains a carrot. The goal of the game is to have the box with the carrot in it. The game involves players taking turns and making decisions based on their knowledge and intuition.

## Game Rules

1. The game is played in the terminal using the curses library.
2. The game requires a terminal width of at least 98 columns.
3. Player 1 and Player 2 will each have a box in front of them.
4. Player 1 will look into their box while Player 2 closes their eyes.
5. Player 1 will then make a statement about the contents of their box:
   - "There is a carrot in my box"
   - "There is not a carrot in my box"
6. Player 2 will decide whether they want to swap boxes with Player 1 or not.
7. Depending on the decision and the actual contents of the boxes, the winner will be determined.

## Prerequisites

- Python 3.x
- curses library (window-curses library for window users)

## How to Run

1. Open your terminal.
2. Navigate to the directory containing the script.
3. Run the script using the command: `python script_name.py`

**Note:** Ensure that your terminal width is sufficient for the game to be displayed properly.
