# Flooder Game

This readme provides an overview of a Python game called "Flooder," which is implemented using the curses library. The game's objective is to fill the entire game board with a single color/shape by strategically choosing colors.

## Game Rules

1. **Objective**: The goal of the game is to make the entire game board the same color/shape.

2. **Starting Point**: The game begins with a color/shape in the upper left corner, which will fill all adjacent squares of the same color/shape.

3. **Player Input**: The player selects a color/shape by pressing a corresponding key:

   - (R)ed
   - (Y)ellow
   - (B)lue
   - (G)reen
   - (P)urple
   - (C)yan
   - (Q)uit: To exit the game

4. **Filling Adjacent Squares**: When the player chooses a color/shape, all adjacent squares of the same color/shape will also be filled with the chosen color/shape.

5. **Limited Chances**: The player has a limited number of chances to change colors and fill the board. You will have a certain number of chances to change colors and continue playing.

6. **Winning**: The game is won when the entire game board is filled with the same color/shape.

7. **Losing**: The game is lost if the player runs out of chances before filling the entire board.

## Controls

- To select a color/shape, press the corresponding key (e.g., (R) for red).
- To quit the game, press (Q).

## System Requirements

- Python 3.x
- curses library (window-curses for window users)

## Running the Game

To play the game, execute the Python script containing the game code. The game will run in the terminal, and you can interact with it using the provided controls.

Enjoy playing the Color Fill game and have fun strategizing to fill the board with a single color/shape!