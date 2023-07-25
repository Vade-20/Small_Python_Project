import random

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}
total_money=5000

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
''')

while True:
    if total_money<0:
        print('')
        print('You run out of mon')
        quit()
        
    bet = input(f'You have {total_money} mon. How much do you bet? (or QUIT) : ')
    if bet.lower().startswith('q'):
        print('\n')
        print('Thank you for Playing')
        print(f"Your end total is {total_money}")
        quit()
    elif not bet.isdigit():
        print(f'Please enter a proper value for betting')
        continue
    elif int(bet)>total_money or int(bet)<0:
        print(f'Please enter you bet in the range (1-{total_money})')
        continue
    bet = int(bet)
    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    ans = input('(C)HO (even) or (H)AN (odd) : ')
    while not ans.lower().startswith('c') and not ans.lower().startswith('h'):
        print('Please enter CHO for even and HAN for odd number') 
        ans = input('(C)HO (even) or (H)AN (odd) : ')
    dice_1 = random.randint(1,6)  
    dice_2 = random.randint(1,6)
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice_1], '-', JAPANESE_NUMBERS[dice_2])
    print('    ', dice_1, '-', dice_2)
  
    dealer_dice =  dice_1 + dice_2
    
    if dealer_dice%2==0:
        dealer_ans = 'c'
    else:
        dealer_ans = 'h'
    
    if ans.lower()[0]==dealer_ans:
        print('You won! You take', bet, 'mon.')
        total_money = total_money + bet  # Add the pot from player's total_money.
        print('The house collects a', bet // 10, 'mon fee.')
        total_money = total_money - (bet // 10)  # The house fee is 10%.
    else:
        total_money = total_money - bet  # Subtract the pot from player's total_money.
        print('You lost!')
    
