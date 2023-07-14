import string

alpha = [i for i in string.ascii_lowercase]

def final(ans,size):
    final_ans = ''
    for j,i in enumerate(ans):
        if size[j]:
            final_ans+=i.upper()
        else:
            final_ans+=i
    return final_ans
                       
def main(text:str,shift:int):
    if shift>25:
        shift = shift%25
    size = {j:i.isupper() for j,i in enumerate(text)}
    text = text.lower()
    new_alpha = alpha[shift:len(alpha)]+alpha[0:shift]
    ans = ''
    for i in text:
        if i in new_alpha:
            index = new_alpha.index(i)
            ans += alpha[index]
        else:
            ans+=i
    return final(ans,size)
   
   
if __name__=='__main__':
    msg = input('Please enter your message here : ')
    for i in range(1,26):
        print(f'For key {i} : {main(msg,i)}')