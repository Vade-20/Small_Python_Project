from random import randint
from tqdm import tqdm


def check_common_bdays(birthday:int):
    bday_list= []
    for _ in range(birthday):
        month = randint(1,12)
        if month ==2:
            days = randint(1,28)
        elif month in [4,6,9,11]:
            days = randint(1,30)
        else:
            days = randint(1,31)
        bday_list.append((month,days))
    
    for i in bday_list:
        if bday_list.count(i)>1:
            return True
    else:
        return False
    
def start(bday):
    c = 0
    print("Counting Duplicates")
    for _ in tqdm(range(100_000)):
        if check_common_bdays(bday):
            c+=1
    percentage = (c/100_000)*100
    
    return percentage

if __name__=='__main__':
    print('Birthday Paradox \n'.upper())
    choice = 'y'
    while choice.lower().startswith('y'):  
        bday = int(input('Please enter number of birthday your want to find percentage:'))     
        while not (str(bday)).isdigit() or bday>100:
            print('Please enter an integer less than 100')
            bday = int(input('Please enter number of birthday your want to find percentage:'))
        ans = start(bday)
        print(f'In a group of {bday} individuals, the probability of having a common birthday is {ans}.')
        choice = input('Would you like to try again? (Y/N) ')

            
    
        
    
    