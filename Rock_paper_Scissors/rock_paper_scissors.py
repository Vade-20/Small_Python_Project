from random import choice
from time import sleep

print('''Rock, Paper, Scissors
- Rock beats scissors.
- Paper beats rocks.
- Scissors beats paper.
''')

options = {'r':'ROCK', 's':'SCISSORS', 'p':'PAPER'}
WINS = 0
LOSSES = 0
TIES = 0
PAUSE = 0.5

def who_wins(user,comp):
    global WINS,LOSSES,TIES
    if (user=='r' and comp=='s') or (user=='s' and comp=='p') or (user=='p' and comp=='r'):
        WINS += 1
        print('You win!')
    elif (user=='r' and comp=='p') or (user=='s' and comp=='r') or (user=='p' and comp=='s'):
        LOSSES += 1
        print('You lose!')
    elif user==comp:
        TIES += 1
        print('It\'s a tie!')
        
while True:
    print(f'{WINS} Wins, {LOSSES} Losses, {TIES} Ties')
    while True:
        user = input('Enter your move: (R)ock,(P)aper,(S)cissors or (Q)uit : ')
        user = ' ' if user == '' else user[0].lower()
        if user =='q':
            print('Thank you')
            quit()
        if user not in ['r', 'p', 's']:
            continue
        break
    print(f'{options.get(user)} versus...')
    for i in range(1,4):
        sleep(PAUSE)
        print(f'{i}...')
    comp = choice(list(options.keys()))
    print(options.get(comp))
    who_wins(user,comp)
    print('-'*54)
