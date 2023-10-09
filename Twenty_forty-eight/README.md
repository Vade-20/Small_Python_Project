# 2048 Game Readme

## Description:

The "2048 Game" is a Python script that implements the popular puzzle game "2048" in a text-based, console environment. The objective of the game is to combine numbered tiles on a 4x4 grid to create a tile with the number 2048.

## How to Play:

1. Run the program.
2. You will see a 4x4 grid with two initial tiles, each with a value of '2'.
3. Use the following keys to move the tiles:
   - `W` or `w`: Move tiles upwards
   - `S` or `s`: Move tiles downwards
   - `A` or `a`: Move tiles to the left
   - `D` or `d`: Move tiles to the right
   - `Q` or `q`: Quit the game
4. After each move, a new tile with a value of '2' or '4' will appear on the grid at a random empty spot.
5. When two tiles with the same number collide while moving in a direction, they will merge into one tile with a value equal to the sum of the two original tiles.
6. The game continues until you create a tile with the number '2048', which means you win the game, or until the grid is full, resulting in a loss.

### Scoring:

- Your score is calculated based on the value of the tiles you combine. Each merge adds the value of the merged tiles to your score. For example, merging two '4' tiles would give you 8 points.

### Winning and Losing:

- You win the game when you create a tile with the number '2048' by merging tiles.
- The game ends when the grid is full, and you cannot make any more moves, resulting in a loss.

### Game Over/Winning Message:

- When you win the game, you will see a "YOU WIN!!!" message along with your final score. Press Enter to exit.
- When you lose the game, you will see a "GAME OVER, YOU LOSE!!!" message along with your final score. Press Enter to exit.
