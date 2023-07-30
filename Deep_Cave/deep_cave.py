from random import randint
from time import sleep

LEFT_WIDTH=20
GAP = 10
WIDTH = 70
PAUSE = 0.5
print('DEEP CAVE')
print('CTRL+C for quiting')
sleep(2)
while True:
    try:
        RIGHT_WIDTH = WIDTH-GAP-LEFT_WIDTH
        print('#'*LEFT_WIDTH,' '*GAP,'#'*RIGHT_WIDTH)
        rand_nm = randint(1,6)
        if rand_nm==1 and LEFT_WIDTH>1:
            LEFT_WIDTH-=1
        elif rand_nm==2 and LEFT_WIDTH+GAP<WIDTH-1:
            LEFT_WIDTH+=1
        else:
            pass
        sleep(0.05)
    except KeyboardInterrupt:
        mosnter = '''
░▄▄▄▄░
▀▀▄██►
▀▀███►
░▀███►░█►
▒▄████▀▀
'''
        for i in mosnter.splitlines():
            print(''.ljust(LEFT_WIDTH,'#'),' '+i.ljust(9),''.ljust(RIGHT_WIDTH,'#'))
        print('#'*WIDTH+'##')
        break 