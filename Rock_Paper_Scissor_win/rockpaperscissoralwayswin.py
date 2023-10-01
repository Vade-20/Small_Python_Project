from random import randint
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
PAUSE = 0.28
round_count = 1
while True:
    print(f'ROUND-{round_count}')
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
    if user=='r':
        print(options.get('s'))
    elif user=='s':
        print(options.get('p'))
    elif user=='p':
        print(options.get('r'))
    
    print('You Win!!!')
    print('-'*54)
    round_count+=1
    WINS+=1