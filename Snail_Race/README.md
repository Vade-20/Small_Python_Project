# Snail Race Simulation

This Python script simulates a snail race using the `curses` library for creating a simple text-based graphical interface. Players can specify the number of snails to participate in the race, and the snails move across the screen until one of them reaches the finish line.

## Prerequisites

curses (widow-curses for window users)

## Usage

- Upon running the script, you will be prompted to enter the number of snails that will participate in the race. Enter a number between 2 and 12.

- The snails are represented by the characters ".@v" and will move across the screen from left to right.

- The snail that reaches the finish line first will be declared the winner.

- After the race is finished, the winning snail's name will be displayed, and the program will wait for a key press before quitting.

## Customization

You can customize the following aspects of the simulation:

- Snail names: The script comes with predefined snail names. You can modify the `names` list to include your own snail names.

- Race duration: The sleep time between snail movements can be adjusted by modifying the `sleep(0.1)` parameter. A smaller value will make the snails move faster.
