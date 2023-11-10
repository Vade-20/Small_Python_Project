import string
from pyperclip import copy 
from math import modf

alphabets = ''.join([i for i in string.ascii_lowercase])

def encrypt(key,word):
    key_shift = [alphabets.find(i) for i in key]
    key_var = 0
    encrypted_text = ''
    for i in word:
        if i.isupper():
            i = alphabets.find(i.lower())
            index_word = (i+key_shift[key_var])%26
            encrypted_text += alphabets[index_word].upper()
        elif i.islower():
            i = alphabets.find(i)
            index_word = (i+key_shift[key_var])%26
            encrypted_text += alphabets[index_word]
        else:
            encrypted_text += i
            
        key_var += 1
        if key_var == len(key):
            key_var = 0
    return encrypted_text      
            
def decrypt(key,word):
    key_shift = [alphabets.find(i) for i in key]
    key_var = 0
    decrypted_text = ''
    for i in word:
        if i.isupper():
            i = alphabets.find(i.lower())
            index_word = abs(i-key_shift[key_var])%26
            decrypted_text += alphabets[index_word].upper()
        elif i.islower():
            i = alphabets.find(i)
            index_word = abs(i-key_shift[key_var])%26
            decrypted_text += alphabets[index_word]
        else:
            decrypted_text += i
            
        key_var += 1
        if key_var == len(key):
            key_var = 0
    return decrypted_text      
    

print('''Vigenère Cipher
The Viegenère cipher is a polyalphabetic substitution cipher that was
powerful enough to remain unbroken for centuries.''')

print('Do you want to (e)ncrypt or (d)ecrypt?')
while True:
    choice = input('> ')
    if choice.lower().startswith('e') or choice.lower().startswith('d'):
        choice = choice[0]
        break
    print('Please enter the letter e or d.')
    
while True:
    print('''Please specify the key to use.\nIt can be a word or any combination of letters withouse spaces:''')
    key = input('> ').lower()
    if key.isalpha():
        break

print(f"Enter the message to {'encrypt' if choice=='e' else 'decrypt'}.")
imp_word = input('> ')
if choice == 'e':
    ans = encrypt(key,imp_word)
    print(f'Encrypted message:\n{ans}')
    print('Full encrypted text copied to clipboard.')
else:
    ans = decrypt(key,imp_word)
    print(f'decrypted message:\n{ans}')
    print('Full decrypted text copied to clipboard.')

copy(ans)
