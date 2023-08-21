import curses
from curses import wrapper
from random import randint
from time import sleep

col_num = 0

def get_colours():
        global col_num
        col_num += 1
        if col_num == 8:
            col_num = 1
        
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
        return curses.color_pair(col_num)
    
@wrapper
def main(stdsrc):
    curses.echo()
    
    while True:
        stdsrc.clear()
        stdsrc.refresh()
        stdsrc.addstr(0,10,'Snail Race'.upper())
        stdsrc.addstr(1,10,'@v --> Snail')
        stdsrc.addstr(2,0,'How many snails will race :  ')
        ans = stdsrc.getstr(2,28).decode(encoding='utf-8')
        if not ans.isdigit():
            stdsrc.addstr(2,28,' '*10)
            continue
        ans = int(ans)
        if ans not in range(2,13):
            stdsrc.addstr(2,0,'Please enter a number in the range [2-12]')
            stdsrc.addstr("\nPress enter to continue")
            stdsrc.getch()
            stdsrc.addstr(2,28,' '*10)
            continue
        break
    
    names = ['Golden Flash', 'Scarlet Speedster', 'Sapphire Streak', 'Jade Viper', 'Majestic Magenta Marvel', 'Electric Elegance', 
             'Ivory Illusion', 'Radiant Yellow Roadster', 'Inferno Blaze', 'Navy Nitro', 'Emerald Velocity','Vibrant Vixen',]

    stdsrc.clear()
    stdsrc.refresh()
    curses.curs_set(0)
    name_num = 0
    moves = {}
    for i in range(1,2*ans+2,2):
        stdsrc.addstr(i,0,'-'*52)
        if i-1!=0:
            col = get_colours()
            stdsrc.addstr(i-1,0,'|'+'  '+' '*48+'|')
            stdsrc.addstr(f'  {names[name_num]}',col)
            moves[name_num] = (0,i-1,col)
            name_num += 1
            
    stdsrc.addstr(0,0,'START')
    stdsrc.addstr(0,46,'FINISH')
    stdsrc.refresh()
    while True:
        rand = randint(0,ans-1)
        x,y,colour = moves[rand]
        s = '.@v'
        stdsrc.addstr(y,x,s,colour)
        moves[rand] = (x+1,y,colour)
        sleep(0.1)
        if x+1 == 50:
            stdsrc.addstr(i+2,0,f'{names[rand]} wins the race.\nThank you for playing',colour)
            stdsrc.getch()
            quit()
        stdsrc.refresh()
            
        
        
    
    