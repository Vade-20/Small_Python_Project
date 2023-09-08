import time
import random
import os

column = os.get_terminal_size().columns
MIN_STREAM_SIZE = 6
MAX_STREAM_SIZE = 14
PAUSE = 1
DENSITY = 10

density = [i for i in range(DENSITY)]
stream = {}
print('Digital Stream')
print('Press Ctrl+C to quit')
while True:
    try:
        while len(stream)<DENSITY:
            stream.setdefault(random.randint(0,column) , random.randint(MIN_STREAM_SIZE,MAX_STREAM_SIZE))
        for i in range(0,column):
            if i not in stream:
                print(end=' ')
            else: 
                print(f'{random.randint(0,1)}')
                stream[i] -= 1
                if stream[i]<1:
                    stream.pop(i)
                    
        time.sleep(PAUSE)
    except KeyboardInterrupt:
        break

print('Thank you ')
