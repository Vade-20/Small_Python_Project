from random import randint

while True:
    rand = randint(1,100)
    print('I am thinking of a number between 1 and 100.')
    for i in range(10,0,-1):
        print(f'You have {i} guesses left. Take a guess.')
        while True:
            try:
                n = int(input('>'))
            except ValueError:
                continue
            break
        if n>rand:
          print('Your guess is too high.')
        elif n<rand:
            print('Your guess is too low.')
        elif n==rand:
            print('Yay! You guessed my number!')
            break
    else:
        print('Game over. The number I was thinking of was 71')
    
    if not input('Would you like to play again (Y/N) : ').lower().startswith('y'):
        break

print('Thank you for playing')
        
        
        