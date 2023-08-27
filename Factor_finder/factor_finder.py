print('''Factor Finder, by Al Sweigart al@inventwithpython.com

A number's factors are two numbers that, when multiplied with each
other, produce the number. For example, 2 x 13 = 26, so 2 and 13 are
factors of 26. 1 x 26 = 26, so 1 and 26 are also factors of 26. We
say that 26 has four factors: 1, 2, 13, and 26.

If a number only has two factors (1 and itself), we call that a prime
number. Otherwise, we call it a composite number.

Can you discover some prime numbers?
''')

while True:
    n = input("Enter a positive whole number to factor or (Q)UIT : ")
    
    if n.lower().startswith('q'):
        break
    
    if not n.isdigit():
        print('Please enter a number')
        continue
    
    n = int(n)

    num_of_factors = []
    for i in range(1,int(n/2)+2):
        if n%i == 0:
            num_of_factors.append(i)
    
    print('The Factors are: ',end='')
    for i in num_of_factors:
        print(i,end=',')
    print(n)
    print('\n')
