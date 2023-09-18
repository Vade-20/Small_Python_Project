from string import ascii_lowercase,ascii_uppercase
from pyperclip import copy

lower_ = ascii_lowercase
upper_ = ascii_uppercase

print('ROT13 Cipher')
while True:
    ans = input('Enter a message to encrypt/decrypt (or QUIT) : ')
    ans = ' ' if ans=='' else ans
    if ans[0].lower()=='q':
        print('Thank you')
        quit()
    translated = ''
    for i in ans:
        if i.isupper():
            num = (upper_.find(i) + 13)%26
            translated += upper_[num]
        elif i.islower():
            num = (lower_.find(i) + 13)%26
            translated += lower_[num]
        else:
            translated+=i
    copy(translated)  
    print(f'The translated message is: {translated}')
    print('(Copied to clipboard.)')
    print('-'*45)