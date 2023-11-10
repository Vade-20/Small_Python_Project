import string
from pyperclip import copy 

alphabets = ''.join([i for i in string.ascii_lowercase])

def main_logic(key,word,mode):
    key_shift = [alphabets.find(i) for i in key]
    key_var = 0
    text = ''
    sign = 1 if mode =='e' else -1
    
    for i in word:
        
        if i.isupper():
            i = alphabets.find(i.lower())
            index_word = (i+(key_shift[key_var]*sign))%26
            text += alphabets[index_word].upper()
        elif i.islower():
            i = alphabets.find(i)
            index_word = (i+(key_shift[key_var]*sign))%26
            text += alphabets[index_word]
        else:
            text += i
            
        key_var += 1
        if key_var == len(key):
            key_var = 0
            
    return text      
    

print('''Vigenère Cipher
The Viegenère cipher is a polyalphabetic substitution cipher that was
powerful enough to remain unbroken for centuries.\n''')

print('Do you want to (e)ncrypt or (d)ecrypt?')
while True:
    choice = input('> ')
    if choice.lower().startswith('e') or choice.lower().startswith('d'):
        choice = choice[0]
        break
    print('Please enter the letter e or d.')
    
while True:
    print('''\nPlease specify the key to use.\nIt can be a word or any combination of letters withouse spaces:''')
    key = input('> ').lower()
    if key.isalpha():
        break

print(f"\nEnter the message to {'encrypt' if choice=='e' else 'decrypt'}.")
imp_word = input('> ')
ans = main_logic(key,imp_word,choice)
copy(ans)

if choice == 'e':
    print(f'\nEncrypted message:\n{ans}')
    print('Full encrypted text copied to clipboard.')
else:
    print(f'\nDecrypted message:\n{ans}')
    print('Full decrypted text copied to clipboard.')

