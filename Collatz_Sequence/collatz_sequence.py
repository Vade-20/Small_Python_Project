from time import sleep
while True:
    try:
        n = int(input('Please enter a positive integer : '))
        if n<=0:
            continue
    except ValueError:
        continue
    
    while n!=1:
        sleep(0.1)
        print(n,end=',',flush=True)
        if n%2==0:
            n = int(n/2)
        else:
            n = n*3+1
    print(1)
    ch = input('Would you like to continue(Y/N) : ')
    if not ch.lower().startswith('y'):
        print('Thank You')
        break