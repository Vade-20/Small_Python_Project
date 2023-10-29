# Sudoku 

This README file provides an overview of a Python-based Sudoku game created using the Tkinter library. The game allows players to play Sudoku puzzles and provides functionalities for generating new games, validating user inputs, and checking for a winning condition.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [How to Play](#how-to-play)
- [Code Explanation](#code-explanation)
- [Requirements](#requirements)


## Introduction

This Sudoku game is a graphical user interface (GUI) application implemented in Python. It uses the Tkinter library for creating the game interface and provides a classic Sudoku experience. The game includes functionalities such as generating new Sudoku puzzles, validating user inputs, highlighting errors, and checking for a winning condition.

## Features

- **New Game:** Start a new Sudoku game with a randomly selected puzzle from a file.
- **Input Validation:** Validates user input to ensure it follows Sudoku rules.
- **Error Highlighting:** Highlights errors in user inputs, making it easier to correct mistakes.
- **Numbers on the Board:** Displays a count of each number on the board.
- **Winning Condition:** Detects when the player has successfully completed the Sudoku puzzle.
- **Graphical User Interface:** Provides an interactive and user-friendly interface for playing Sudoku.

## How to Play

1. Run the Sudoku game by executing the Python script.
2. The game interface will appear, showing a blank Sudoku grid with cells that you can fill in.
3. Click on a cell to select it, and then type a number (1-9) to enter your guess.
4. Use the 'New Game' button to start a new Sudoku puzzle at any time.
5. The game will validate your input, highlighting errors in red and preventing you from entering incorrect numbers.
6. As you progress, you can check the 'Numbers on the Board' to see the count of each number on the Sudoku grid.
7. The game will automatically detect if you have completed the puzzle and display a congratulatory message.

## Code Explanation

The Sudoku game code is well-organized and includes various functions to handle game logic. Here are some key components:

- **User Input Validation:** The `validate_input_entry` function checks if user input is valid, ensuring it is a digit from 1 to 9 or an empty string.

- **New Game Function:** The `new_game` function reads Sudoku puzzles from a file, selects a random puzzle, and populates the game grid. It also sets some cells as readonly to represent the initial puzzle.

- **Error Highlighting:** The `show_row_column` function is responsible for highlighting errors by checking rows, columns, and boxes for duplicate numbers. It changes the background color of cells with the same number, making it easier for the player to identify and correct mistakes.

- **Winning Condition:** The `winning_condition` function checks if the player has successfully completed the Sudoku puzzle by ensuring all cells are filled with valid numbers.

- **GUI Creation:** The code uses Tkinter to create the graphical user interface, including buttons, labels, and the Sudoku grid.

## Requirements

To run the Sudoku game, you need:

- Python 3.x (with Tkinter installed)
- A text file containing Sudoku puzzles (e.g., 'sudokupuzzles.txt').

