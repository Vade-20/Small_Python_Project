from random import randint
from pyperclip import copy


def sponge_casing(text:str):
    new_text = ''
    for i in text:
        if not i.isalpha():
            new_text += i
            continue
        num = randint(0,1)
        if num == 0:
            new_text += i.lower()
        elif num == 1:
            new_text += i.upper()
    return new_text    
        
    
def main():
    text = input(f'{sponge_casing("enter your message :")} ')
    ans = sponge_casing(text)
    print(ans)
    print(f'{sponge_casing("copied spongecase to clipboard")}')

if __name__ == '__main__':
    main()