import curses
import random
from curses import wrapper
from curses.textpad import rectangle

def get_colours(a):
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
        
        COLORS = {
        'Y' : curses.color_pair(1),
        'R' : curses.color_pair(2),
        'B' : curses.color_pair(3),
        'G' : curses.color_pair(4),
        'P' : curses.color_pair(5),
        'C' : curses.color_pair(6),
        'W' : curses.color_pair(7),}
        return COLORS.get(a)

def get_symbol(a):
    symbol = {
    'H': chr(9829),  # '♥'
    'D': chr(9830),  # '♦'
    'S': chr(9824),  # '♠'
    'C': chr(9827),  # '♣'
    'B': chr(9679),  # '●'
    'T': chr(9650),}  # '▲'
    return symbol.get(a)


    
BORDER_WIDTH = 30  # max width 115
BORDER_HEIGHT = 20 # max height 25
BLOCK = chr(9608)
CHANCES = 30

def next_step(ans):
    global blocks
    global same_block

    for i in same_block:
        up = (i[0]-1,i[1])
        down = (i[0]+1,i[1])
        right = (i[0],i[1]+1)
        left = (i[0],i[1]-1)
        direction = [up,down,right,left]
        for j in direction:
            if same_block.get(i) == blocks.get(j):
                if j not in same_block:
                    same_block[j] = ans 
                    return next_step(ans)
        
@wrapper
def main(stdsrc):
    global blocks
    global same_block
    global CHANCES
    stdsrc.clear()
    stdsrc.bkgd(' ', get_colours('W'))
    stdsrc.refresh()
    curses.echo()
    stdsrc.addstr(0,0,''' Rules ~
Set the upper left color/shape, which fills in all the adjacent squares of that color/shape. 
Try to make the entire board the same color/shape.\nDo you want to play in colorblind mode (Y/N): ''',curses.A_BOLD)
    
    while True:
        choice = stdsrc.getstr(3,48).decode(encoding='utf-8')
        if choice.lower().startswith('n'):
            blocks = {(i,j):random.choice(['Y', 'R', 'B', 'G', 'P', 'C']) for i in range(5,BORDER_HEIGHT) for j in range(2,BORDER_WIDTH)}
            break
        elif choice.lower().startswith('y'):
            blocks = {(i,j):random.choice(['H','D','S','C','B','T']) for i in range(5,BORDER_HEIGHT) for j in range(2,BORDER_WIDTH)}
            break
        else:
            stdsrc.addstr(3,48,' '*10)
    
    for i in range(BORDER_WIDTH*BORDER_HEIGHT):
        y = random.randint(2,BORDER_WIDTH-2)
        x = random.randint(5,BORDER_HEIGHT-1)
        blocks[(x,y+1)] = blocks[(x,y)] 
    
    same_block = {(5,2):blocks.get((5,2))}  
    rectangle(stdsrc,4,1,BORDER_HEIGHT,BORDER_WIDTH)
    next_step(same_block.get((5,2)))

    while CHANCES!=0:
        for j in same_block:
            blocks[j] = same_block[j]  
        for i in blocks:
            if choice.lower().startswith('n'):
                stdsrc.addstr(i[0],i[1],BLOCK,get_colours(blocks.get(i)))
            else:
                stdsrc.addstr(i[0],i[1],get_symbol(blocks.get(i)))
        
        if len(same_block) == len(blocks):
            stdsrc.addstr(BORDER_HEIGHT+1,1,' '*100)
            stdsrc.addstr(BORDER_HEIGHT+1,1,'Congratulations!! You WIN!!')
            stdsrc.addstr(BORDER_HEIGHT+2,1,'Press enter to exit.')
            stdsrc.getch()
            quit()
        
        if choice.lower().startswith('n'):   
            stdsrc.addstr(BORDER_HEIGHT+1,1,f'Choose one of')
            stdsrc.addstr(' (R)ed',get_colours('R'))
            stdsrc.addstr(' (Y)ellow',get_colours('Y'))
            stdsrc.addstr(' (B)lue',get_colours('B'))
            stdsrc.addstr(' (G)reen',get_colours('G'))
            stdsrc.addstr(' (P)urple',get_colours('P'))
            stdsrc.addstr(' (C)yan',get_colours('C'))
            stdsrc.addstr(' (Q)uit : ')
            stdsrc.addstr(BORDER_HEIGHT+2,1,f'{CHANCES} LEFT')
            ans = stdsrc.getstr(BORDER_HEIGHT+1,70).decode(encoding='utf-8').upper()
        else:
            stdsrc.addstr(BORDER_HEIGHT+1,1,f'Choose one of (H)EART,(D)iamonds,(S)pade,(C)lub,(B)all,(T)riangle,(Q)uit : ')
            ans = stdsrc.getstr(BORDER_HEIGHT+1,80).decode(encoding='utf-8').upper()
            
        ans = stdsrc.getstr(BORDER_HEIGHT+1,70).decode(encoding='utf-8').upper()
        ans = ' ' if ans =='' else ans
        ans = ans[0]
        if ans == 'Q':
            quit()   
        
        if choice.lower().startswith('n'):   
            while ans not in ['R', 'G', 'B', 'Y', 'P', 'C', 'Q']:
                stdsrc.addstr(BORDER_HEIGHT+1,70,' '*10)
                ans = stdsrc.getstr(BORDER_HEIGHT+1,70).decode(encoding='utf-8').upper()
        else:
            while ans not in ['H', 'D', 'S', 'C', 'B', 'T', 'Q']:
                stdsrc.addstr(BORDER_HEIGHT+1,70,' '*10)
                ans = stdsrc.getstr(BORDER_HEIGHT+1,80).decode(encoding='utf-8').upper()
        
        same_block = {i:ans for i in same_block}    
        next_step(ans)
        stdsrc.addstr(BORDER_HEIGHT+1,70,' '*10)
        CHANCES -= 1
        
    stdsrc.addstr(BORDER_HEIGHT+1,1,' '*100)
    stdsrc.addstr(BORDER_HEIGHT+1,1,'You run of turns. You lose')
    stdsrc.addstr(BORDER_HEIGHT+2,1,'Press enter to exit.')
    stdsrc.getch()
    