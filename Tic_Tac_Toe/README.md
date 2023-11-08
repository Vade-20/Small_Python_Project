# Tic Tac Toe Game

This is a simple implementation of the classic Tic Tac Toe game using Python and the Tkinter library for the GUI.

## Features

- Player vs Player mode
- Player vs Computer mode (with easy and hard difficulty levels)
- Graphical User Interface using Tkinter

## How to Run

1. Ensure you have Python installed on your system.
2. Clone this repository or download the python file.
3. Run the python file in your terminal or command prompt with the command `python filename.py`.

## Game Rules

- The game is played on a grid that's 3 squares by 3 squares.
- You are X, your friend (or the computer in this case) is O. Players take turns putting their marks in empty squares.
- The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
- When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

## Implementation Details

The game uses the Tkinter library to create the GUI. The game logic is implemented in Python. The computer's moves are determined using the minimax algorithm in the hard difficulty level.
