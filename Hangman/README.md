# Hangman Game 

The Hangman game is a simple word-guessing game where a player tries to guess a hidden word one letter at a time. If the player guesses the word before making too many incorrect guesses, they win. Otherwise, they lose.

## Table of Contents
1. [Introduction](#introduction)
2. [Dependencies](#dependencies)
3. [How to Play](#how-to-play)
4. [Running the Game](#running-the-game)

## Introduction

The provided code is a simple Hangman game implemented in Python using the curses library for creating a text-based user interface. The game loads a random word from a word.json file
and provides the player with a set number of attempts to guess the word correctly. The game also displays the definition of the word to make it more educational.

## Dependencies

- Python
- PyDictionary library (used for retrieving word meanings)
- curses library (window-curse for window users)

## How to Play

1. The game starts by displaying a title "HANGMAN THE GAME" in red at the top of the screen.
2. The hangman figure is displayed on the left, and the missed letters are shown on the right.
3. The loading message is displayed as the game retrieves a random word and its meaning.
4. The game displays the definition of the word at the bottom of the screen.
5. The word to guess is initially represented by underscores. For example, "_ _ _ _ _" for a five-letter word.
6. The player is prompted to guess a letter by entering it and pressing Enter.
7. If the guessed letter is correct, it is revealed in the word, replacing the corresponding underscore.
8. If the guessed letter is incorrect, the hangman figure is progressively drawn.
9. The game continues until the player either successfully guesses the word or runs out of attempts.
10. A win or lose message is displayed at the end, along with the correct word.

## Running the Game

To run the game, follow these steps:

1. Make sure you have the required dependencies installed (Python, PyDictionary, and curses).
2. Save the code to a Python file, e.g., `hangman_game.py`.
3. Make sure you have a JSON file named `words.json` in the same directory with a list of words to choose from.
4. Execute the code using Python.

```bash
python hangman.py
```

