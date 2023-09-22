from string import ascii_uppercase
from random import shuffle
from pyperclip import copy

print('''Simple Substitution Cipher\n
A simple substitution cipher has a one-to-one translation for each
symbol in the plaintext and each symbol in the ciphertext.\n''')

while True:
    mode = input('Do you want to (e)ncrypt or (d)ecrypt : ')
    mode = ' ' if mode == '' else mode[0]
    if mode not in ['e','d']:
        print("Please enter e for encryption or d for decryption")
        continue
    break

print('Please specify the key to use.')

if mode == 'e':
    print('Or enter RANDOM to have one generated for you.')
    
while True:
    key = input('KEY: ').upper()
    #generate a random key
    if key == 'RANDOM':
        alpha = [i for i in ascii_uppercase]
        shuffle(alpha)
        key = ''.join(alpha)
        print(f'The key is {key} . KEEP THIS SECRET!')        
    #check if the key is valid or not
    if len(key) != len(ascii_uppercase):
        print('Please enter a valid key which contains all the alphabetic characters')
        continue
    
    for i in key:
        if i not in ascii_uppercase:
            print('Please enter a valid key which only contains alphabetic characters')
            break
    else:
        break
    
    continue

print('\n')
mode__ = 'encrypted' if mode == 'e' else 'decrypted'
message = input(f'Enter the message to {mode__} : ')
if mode == 'e':
    order = {ascii_uppercase[i]:key[i] for i in range(0,26)}
elif mode == 'd':
    order = {key[i]:ascii_uppercase[i] for i in range(0,26)}

translated = ''
for i in message:
    if i.isupper():
        translated += order.get(i)
    elif i.islower():
        translated += order.get(i.upper()).lower()
    else:
        translated += i

print(f'The {mode__} message is:{translated}')
copy(translated)
print(f'\nFull {mode__} text copied to clipboard.')

    

    

        