# Forest Fire Simulation 

## Overview
This Python program simulates the spread of fire in a forest using the curses library. The forest is represented as a grid, and trees are denoted by 'A', while burned trees are represented as 'W'. The simulation includes two key factors: growth chance and lightning chance. 

- **Growth Chance**: This represents the likelihood of a tree growing in an empty space. You can adjust the growth chance to control the rate at which trees appear in the forest.

- **Lightning Chance**: This represents the likelihood of a tree catching fire due to lightning. You can adjust the lightning chance to control the frequency of trees catching fire.

## Requirements
-curses (window curses for window users)

## Customization
You can customize the simulation by adjusting the following parameters in the code:

- `Grow_Chance`: This variable controls the growth chance. Increase or decrease its value to change how often trees grow.

- `Ligtening_Chance`: This variable controls the lightning chance. Adjust its value to change how frequently trees catch fire due to lightning.

## Important Notes
- The simulation is purely for educational purposes and provides a visual representation of how fires can spread in a forest.

- The forest grid is displayed using curses, which is a text-based library for terminal-based user interfaces. You will see the grid and the trees' growth and burning in the terminal window.

- To exit the simulation, press `CTRL+C`.
