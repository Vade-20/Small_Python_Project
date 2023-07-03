from random import randint

def start_game(chances = 10,number_of_digits=3):
    dict_of_number = {1:str(randint(1,9)),2:str(randint(10,99)),3:str(randint(100,999)),4:str(randint(1_000,9_999)),5:str(randint(10000,99999)),6:str(randint(100000,999999)),7:str(randint(1000000,9999999)),
                      8:str(randint(10000000,99999999)),9:str(randint(100000000,999999999)),10:str(randint(1000000000,9999999999))}
    rand_num = dict_of_number.get(number_of_digits)
    while chances>0:
        print('Number of Guesses left:',chances)
        ans = input('Enter your Guess: ')      
        if len(ans)!=len(rand_num) or ans[0]=='0':
            print(f'Please enter a {number_of_digits} digited number')
            continue
            
        if ans==rand_num:
            print('Your Win!! the number is',rand_num)
            break
        
        bagel = 0
        for j,i in enumerate(ans,start=0):
            if i in rand_num:
                bagel = 1
                if rand_num[j]==i:
                    print('Fermi',end=' ')
                else:
                    print('Pico',end=' ')
            else:
                print('    ',end='')
        print('')
        
        if bagel==0:
            print('Bagel')
        chances-=1
    else:
        print('Your Lose!! The answer is',rand_num)
          
if __name__=='__main__':
    print('WELCOME TO NUMBER GUESSING GAME')
    number_of_digits = int(input("Please indicate the desired number of digits for your guess, within the range of 3 to 10: "))
    chances = int(input('Please specify the desired number of chances you would like to have: '))
    while True:
        while not str(chances).isdigit() or not str(number_of_digits).isdigit():
            print('Error please enter a number')
            number_of_digits = int(input("Please indicate the desired number of digits for your guess, within the range of 3 to 10: "))
            chances = int(input('Please specify the desired number of chances you would like to have: '))
        start_game(chances,number_of_digits)
        if not  input('Would you like to play again (Y/N)? ').lower().startswith('y'):
            break