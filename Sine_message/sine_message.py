import curses
from curses import wrapper
import math, shutil, time

@wrapper
def main(stdsrc):
    curses.echo()
    WIDTH,HEIGHT = shutil.get_terminal_size()
    new_pad = curses.newpad(10000,10000)
    while True:
        stdsrc.clear()
        stdsrc.refresh()
        stdsrc.addstr(15,30,'Sine Message')
        stdsrc.addstr(15+1,30,'(Press Ctrl-C to quit.)')
        stdsrc.addstr(15+2,30,f'What message do you want to display? (Max {WIDTH // 2}chars.)')
        stdsrc.addstr(15+3,30,f'>')
        ans = stdsrc.getstr(15+3,32).decode(encoding='utf-8')
        if len(ans)<WIDTH//2:
            break
    stdsrc.clear()
    stdsrc.refresh()
    step = 0.0  # The "step" determines how far into the sine wave we are.
    # Sine goes from -1.0 to 1.0, so we need to change it by a multiplier:
    multiplier = (WIDTH - len(ans)) / 2
    for i in range(1,10001):  # Main program loop.
        sinOfStep = math.sin(step)
        padding = ' ' * int((sinOfStep + 1) * multiplier)
        new_pad.addstr(padding + ans)
        step += 0.25  # (!) Try changing this to 0.1 or 0.5.
        
    for i in range(5000): #Vertical scroll
            new_pad.refresh(i,0,0,0,HEIGHT-10,WIDTH-10+i)
            time.sleep(0.2)   
            
    stdsrc.getch()