# Number Guessing Game

This is a simple number guessing game implemented in Python. The game generates a random three-digit number, and the player has to guess the number within a certain number of chances.

The game provides the following feedback for each guess:

- 'Fermi' when a guessed digit is correct and in the correct place
- 'Pico' when a guessed digit is correct but in the wrong place
- 'Bagels' if no digits in the guess are correct

## How to Play

1. Run the script using a Python interpreter.
2. The game will generate a random three-digit number.
3. Enter your 3 digited guess  when prompted.
4. The game will provide feedback based on your guess.
5. Keep guessing until you guess the correct number or run out of chances.

## Example Gameplay

```
Enter your Guess: 123
   Fermi Pico      
Enter your Guess: 456
   Pico      
Enter your Guess: 789
   Bagel
...
```

## Dependencies

The code uses the `random` module from the Python standard library to generate random numbers.

