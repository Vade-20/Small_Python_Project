from random import randint
from pyperclip import copy


def sponge_casing(text:str):
    new_text = ''
    use_upper = True
    for i in text:
        if not i.isalpha():
            new_text += i
            continue
        
        if randint(1,100) <90:                  #90 percent propbabilty the cases will switch
            use_upper = not use_upper
            
        if use_upper:
            new_text += i.lower()
        else:
            new_text += i.upper()
    return new_text    
        
    
def main():
    text = input(f'{sponge_casing("enter your message :")} ')
    ans = sponge_casing(text)
    print(ans)
    print(f'{sponge_casing("copied spongecase to clipboard")}')
    copy(ans)

if __name__ == '__main__':
    main()