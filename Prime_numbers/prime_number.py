from math import sqrt
from time import sleep

print('Prime Numbers')
print('Prime numbers are numbers that are only evenly divisible by one and themselves. ')

while True:
    start = input('Enter a number to start searching for primes from : ').strip()
    if not start.isdigit():
        continue
    start = int(start)
    break

while True:
    stop = input('Enter a number to stop searching for primes from : ').strip()
    if not stop.isdigit():
        continue
    stop = int(stop)
    break

def is_prime(num:int):
    for i in range(2,int(sqrt(num))+1):
        if num%i == 0:
            return False
    else:
        return True

try: 
    for i in range(start, stop+1):
        if is_prime(i):
            print(i,end=',',flush=True)
            sleep(0.1)
except KeyboardInterrupt:
    pass
        