# Prime Number Finder

This Python script finds and displays prime numbers within a specified range. Prime numbers are numbers that are only evenly divisible by one and themselves.

## Usage

- When you run the script, it will prompt you to enter a starting and stopping number for prime number searching. Ensure that you input valid positive integers for both start and stop.

- The script will then calculate and display all prime numbers within the given range.

- The program provides a brief pause between displaying each prime number using the `sleep(0.1)` function. This is done to make the output more readable.

- You can interrupt the script at any time by pressing `Ctrl + C`.

## Function Explanation

The script defines an `is_prime` function that determines whether a given number is prime or not. It uses a basic trial division method by checking divisibility from 2 to the square root of the number.
