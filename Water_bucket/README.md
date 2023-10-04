# Water Bucket Puzzle

This is a Python program that simulates the Water Bucket Puzzle, a classic puzzle in which you must use three buckets to measure a specific amount of water. The goal of the game is to get a certain amount of water into one of the buckets.

## How to Play

### Game Objective
The objective of the game is to fill one of the buckets with a specific amount of water (defined by the `GOAL` variable). You can achieve this by filling, emptying, and pouring water between the three buckets.

### Bucket Actions
You can perform the following actions in the game:

- **(F)ill the bucket**: Fill the selected bucket to its maximum capacity.
- **(E)mpty the bucket**: Empty the selected bucket, removing all its water.
- **(P)our one bucket into another**: Pour water from one bucket into another. You'll need to select both the source and destination buckets.

### Game Controls
- Use the keys `F`, `E`, `P`, and `Q` to choose your action.
  - `F`: Fill the bucket.
  - `E`: Empty the bucket.
  - `P`: Pour water from one bucket into another.
  - `Q`: Quit the game.
- When prompted, select a bucket by typing its size (e.g., 8, 5, or 3) or `Q` to quit the game.

### Winning
You win the game when you have the desired amount of water (specified by `GOAL`) in one of the buckets. The program will display a message congratulating you and the number of steps it took to solve the puzzle.

### Exiting
You can quit the game at any time by pressing `Q`. 
