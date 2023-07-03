# Bagels

This is a simple number guessing game implemented in Python. The player is given a certain number of chances to guess a randomly generated number within a specified range of digits.


## How to Play

1. Run the code in your preferred Python environment.
2. You will be prompted to enter the desired number of digits for your guess.
3. Next, specify the desired number of chances you would like to have.
4. Enter your guesses when prompted. Each guess should be a number with the same number of digits as the specified range.
5. Based on your guess, you will receive feedback in the form of "Fermi" or "Pico" clues:
    - "Fermi" indicates that a digit in your guess is in the correct position.
    - "Pico" indicates that a digit in your guess is present in the number but in the wrong position.
    - "Bagel" indicates that none of the digits in your guess are present in the number.
6. Continue guessing until you run out of chances or correctly guess the number.
7. If you guess the number correctly, you win the game! Otherwise, you lose, and the correct number will be revealed.

## Code Explanation

The code begins by importing the `randint` function from the `random` module. It defines the `start_game` function, which takes two optional arguments: `chances` (the number of chances to guess the number) and `number_of_digits` (the desired number of digits for the random number).

The `rand_num` variable is assigned the corresponding randomly generated number based on the `number_of_digits` argument.

The player is then prompted to enter their guesses. The code validates the input, ensuring that the guess has the correct number of digits and does not start with zero. If the guess matches the random number, the player wins the game. Otherwise, the code provides feedback by checking each digit of the guess against the random number and printing "Fermi" or "Pico" clues accordingly.

If the player exhausts all their chances without guessing the correct number, they lose the game. Finally, the code allows the player to choose whether to play again or exit the game.

In the main section of the code, the player is first greeted with a welcome message. Then, they are prompted to enter the desired number of digits and chances. The code validates the input and calls the `start_game` function. After each game, the player is given the option to play again.

## Example Gameplay

```command
WELCOME TO Bagels the number guessing game

Please indicate the desired number of digits for your guess, within the range of 1 to 10: 3
Please specify the desired number of chances you would like to have: 10
Number of Guesses left: 10
Enter your Guess: 123
Pico

Number of Guesses left: 9
Enter your Guess: 456
        Pico 

Number of Guesses left: 8
Enter your Guess: 789
Fermi

Number of Guesses left: 7
Enter your Guess: 715
Fermi Pico    

Number of Guesses left: 6
Enter your Guess: 761

Your Win!! the number is 761
Would you like to play again (Y/N)?
...
```