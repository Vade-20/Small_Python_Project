import curses
from curses import wrapper
import shutil
from time import sleep
x_terminal,y_terminal = shutil.get_terminal_size()
PAUSE = 0.9
bottle = ''' ||
 )(
|__|
|  |
|__|'''

@wrapper
def main(stdsrc):
    TOTAL_BOTTLES = 99
    stdsrc.clear()
    stdsrc.refresh()
    while TOTAL_BOTTLES>0:
        total_bottles = TOTAL_BOTTLES
        for i in range(0,25,6):
            for j in range(0,120,5):
                    cur_new = curses.newwin(5,5,i,j)
                    cur_new.addstr(bottle)
                    cur_new.refresh()
                    total_bottles -= 1
                    if total_bottles < 0:
                        break
            if total_bottles<0:
                break
            stdsrc.addstr(i+5,0,'-'*(x_terminal-1)+'\n')
        stdsrc.addstr(24,21,f'{TOTAL_BOTTLES} bottles of milk on the wall,')
        sleep(PAUSE)
        stdsrc.refresh()
        stdsrc.addstr(25,21,f"{TOTAL_BOTTLES} bottles of milk")
        sleep(PAUSE)
        stdsrc.refresh()
        stdsrc.addstr(26,21,'Take one down, pass it around,')
        sleep(PAUSE)
        stdsrc.refresh()
        stdsrc.addstr(27,21,f'{TOTAL_BOTTLES-1} bottles of milk on the wall!')
        stdsrc.refresh()
        sleep(PAUSE)
        TOTAL_BOTTLES -= 1
        stdsrc.clear()
        