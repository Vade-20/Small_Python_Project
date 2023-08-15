from time import sleep
import os

terminal_size = os.get_terminal_size()
sign = 1
spaces = 0
speed = 0.01

color_codes = {
    1: "\033[31m",           #red
    2: "\033[38;5;208m",     #orange
    3: "\033[33m",           #yellow 
    4: "\033[32m",           #green
    5: "\033[34m",           #blue
    6: "\033[38;5;54m",      #indigo
    7: "\033[38;5;128m",     #violet
    "reset": "\033[0m"
}

def get_ans(text,num):
    return f"{color_codes[num]}{text}{color_codes['reset']}"

def colour_text(text):
        final_msg = ''
        col = 1
        for i in text:
            if i==' ':
                final_msg+=' '
                continue
            if col == 8:
                col = 1
            final_msg+=get_ans(i,col)
            col+=1
        return final_msg
    
text = ''
for i in range(1,8):
    text += get_ans('##',i)
print(colour_text('RAINBOW'))
print(colour_text('Press CTRL+C to quit'))

sleep(2.5)

while True:
    try:
        print(' '*spaces+text)
        spaces+=sign
        if spaces==terminal_size.columns-14:
            sign = -1
        elif spaces==0:
            sign = 1
        sleep(speed)
    except KeyboardInterrupt:
        print('\n')
        final_msg = ''
        col = 1
        for i in 'Thank you':
            if i==' ':
                final_msg+=' '
                continue
            if col == 8:
                col = 1
            final_msg+=get_ans(i,col)
            col+=1
        print(final_msg)
        break