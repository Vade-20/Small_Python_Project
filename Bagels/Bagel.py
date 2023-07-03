from random import randint

def start_game(chances = 10,number_of_digits=3):
    a = int('1'+'0'*number_of_digits)
    b = int('9'+'9'*number_of_digits)
    rand_num = str(randint(a,b))
    while chances>0:
        print('Number of Guesses left:',chances)
        ans = input('Enter your Guess: ')      
        if len(ans)!=len(rand_num) or ans[0]=='0':
            print(f'Please enter a {number_of_digits+1} digited number\n')
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
        print('')
        chances-=1
    else:
        print('Your Lose!! The answer is',rand_num)
          
if __name__=='__main__':
    print('WELCOME TO NUMBER GUESSING GAME\n')
    number_of_digits = int(input("Please indicate the desired number of digits for your guess: "))
    chances = int(input('Please specify the desired number of chances you would like to have: '))
    while True:
        while not str(chances).isdigit() or not str(number_of_digits).isdigit():
            print('Error please enter a number')
            number_of_digits = int(input("Please indicate the desired number of digits for your guess: "))
            chances = int(input('Please specify the desired number of chances you would like to have: '))
            
        start_game(chances,number_of_digits-1)
        if not  input('Would you like to play again (Y/N)? ').lower().startswith('y'):
            break