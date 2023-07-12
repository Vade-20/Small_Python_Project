import string
import pyperclip

alpha = [i for i in string.ascii_lowercase]


def final(ans,size):
    final_ans = ''
    for j,i in enumerate(ans):
        if size[j]:
            final_ans+=i.upper()
        else:
            final_ans+=i
    return final_ans
                       
def main(text:str,shift:int,command):
    if shift>25:
        shift = shift%25
    size = {j:i.isupper() for j,i in enumerate(text)}
    text = text.lower()
    new_alpha = alpha[shift:len(alpha)]+alpha[0:shift]
    ans = ''
    if command == 'e':
        for i in text:
            if i in alpha:
                index = alpha.index(i)
                ans += new_alpha[index]
            else:
                ans+=i
    else:
        for i in text:
            if i in new_alpha:
                index = new_alpha.index(i)
                ans += alpha[index]
            else:
                ans+=i
    return final(ans,size)
   
        
if __name__=='__main__':
    while True:
        choice = input("Would you like to (e)ncrypt or (d)ecrypt:  ")
        if choice[0] not in ['e','d']:
            print("Press e for encryption and d for decryption")
            continue
        break
    while True:
        num = input('Please enter the key (1 to 26) to use: ')
        if not num.isdigit():
            print('Please enter a digit')
            continue
        elif int(num)<0:
            print('Please enter the number between 0-25')
        num = int(num)
        break
    text = input('Please enter the message here: ')
    
    ans = main(text,num,choice[0])
    print(text,'--->',ans)
    print(ans,'is copied to the clipbord')
    pyperclip.copy(ans)
    