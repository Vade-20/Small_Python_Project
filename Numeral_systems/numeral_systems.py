
print('''Numeral System Counters

This program shows you equivalent numbers in decimal (base 10),
hexadecimal (base 16), and binary (base 2) numeral systems.

(Ctrl-C to quit.)
''')

while True:
    start = input('Enter the starting number (e.g. 0) > ')
    if start == '':
        start = 0
    elif start.isdecimal():
        start = int(start)
    if start>=0:
        break
    print('Please enter a number between 0 and 10000')

while True:
    finish = input('Enter how many numbers to display (e.g. 1000) > ')
    if finish == '':
        finish = 1000
    elif finish.isdecimal():
        finish = int(finish)
    
    if finish>= start:
        break
    else:
        print(f'Please eneter a number between {start} and 1000')
        
for i in range(start,finish+1):
    num = i
    hex_ = hex(i)[2:].upper()
    bin_ = bin(i)[2:]
    print(f"Number: {str(num).ljust(10)} Hex: {str(hex_).ljust(10)} Bin:{bin_}")