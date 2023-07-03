# Birthday Paradox Probability

This Python script calculates the probability of having a common birthday in a group of individuals using the concept of the Birthday Paradox. The Birthday Paradox states that in a relatively small group of people, the likelihood of two or more individuals sharing the same birthday is higher than expected.

## How it Works

The script uses the following steps to calculate the probability:

1. The user is prompted to enter the number of birthdays to consider.
2. The script generates random birthdays for the specified number of individuals.
3. The generated birthdays are checked to see if there are any duplicates.
4. The process is repeated for a large number of iterations (100,000 times) to obtain an accurate probability estimate.
5. The script calculates the percentage of iterations where duplicates were found.
6. The calculated probability is displayed to the user.

## Dependencies

The script requires the following Python modules:

- `random`: Used to generate random numbers for the birthdays.
- `tqdm`: Used to display a progress bar during the calculation iterations.

Make sure you have these modules installed before running the script. You can install them using `pip`:

```
pip install tqdm
```

## Usage

1. Run the script using a Python interpreter.
2. The script will prompt you to enter the number of birthdays you want to consider.
3. Enter an integer value less than 100.
4. The script will calculate the probability of having a common birthday in the specified group size.
5. The calculated probability will be displayed.
6. You can choose to try again or exit the program.

## Example

```
BIRTHDAY PARADOX

Please enter the number of birthdays you want to find the percentage: 30
In a group of 30 individuals, the probability of having a common birthday is 70.285%.

Would you like to try again? (Y/N) y
Please enter the number of birthdays you want to find the percentage: 50
In a group of 50 individuals, the probability of having a common birthday is 97.037%.

Would you like to try again? (Y/N) n
```

