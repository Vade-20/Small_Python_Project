from time import sleep
import random
import os

column = int(os.get_terminal_size().columns)

MIN_STREAM_SIZE = 6         #Enter how long a single stream should be
MAX_STREAM_SIZE = 14

PAUSE = 0.1                 #Enter the pause each stream should have after printing it out
DENSITY = 10                #Enter the density percentage ie the percantage of terminal you want the screen to appear in eg 10%,50%,70%
stream = {}
print('\033[32mDigital Stream')
print('Press Ctrl+C to quit')
sleep(1)
while True:
    try:
        while len(stream) != (int((DENSITY*column)/100)):
            stream[random.randint(0,column)] = random.randint(MIN_STREAM_SIZE,MAX_STREAM_SIZE)
        for i in range(0,column):
            if i in stream:
                print(f'{random.randint(0,1)}',end='',flush=True)
                stream[i] -= 1
                if stream[i]<1:
                    stream.pop(i)
            else:
                print(' ',end='',flush=True)
        print('',flush=True)
        sleep(PAUSE)
    except KeyboardInterrupt:
        break
print('')
print('Thank you \033[0m')
