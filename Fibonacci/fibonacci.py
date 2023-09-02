import sys
sys.set_int_max_str_digits(0)

while True:
    print('Enter the Nth Fibonacci number you wish to')
    print('calculate (such as 5, 50, 1000, 9999), or QUIT to quit:')
    choice = input('>')
    if choice.lower().startswith('q'):
        print('')
        print('Thank you!!')
        quit()
    elif not choice.isdigit():
        print('Please enter a number')
        continue
    elif int(choice)<1 or int(choice)>10_000:
        print('Please enter a number in range 0-10,000')
        
        
    num1 = 0
    num2 = 1
    print('The Fibonacci Sequence : ',end='')
    print(num1,end=', ')
    for i in range(int(choice)-1):
        if i==int(choice)-2:
            print(num2)
            break
        else:
            print(num2,end=', ')
            rough = num2
            num2 = num2+num1
            num1 = rough
        
    ans = int(num2) if int(choice)!=1 else 0
    
    print(f'\n\nThe {choice} Fibonacci number is {ans}\n')
    