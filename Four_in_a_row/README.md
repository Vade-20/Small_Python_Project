# Four in a Row Game

This is a Python implementation of the classic "Four in a Row" game, also known as "Connect Four," using the curses library for the terminal interface.

## Overview

"Four in a Row" is a two-player game where players take turns dropping tiles into a grid of n number of  columns. The objective is to be the first player to connect four of their tiles horizontally, vertically, or diagonally.

## Features

- Two-player gameplay with alternating turns (Player X and Player O).
- A grid with n number columns and  n number rows.
- Simple terminal-based user interface using curses.
- Win condition detection for both Player X and Player O.
- A tie condition when the board is full.
- Rules explanation displayed at the start of the game.

## Prerequisites

- Python 3.x (The game was developed using Python 3)
- The `curses` library (window-curse for window users)

## Customization

You can customize the game by modifying the `NUM_OF_COL` constant to change the grid's width  and height and `PLAYER_TURN` to specify which player goes first.
