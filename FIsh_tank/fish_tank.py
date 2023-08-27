import curses
from curses import wrapper
import random
import time


FISH_TYPES = [
    {'right': '><>',          'left':'<><'},
    {'right': '>||>',         'left':'<||<'},
    {'right': '>))>',         'left':'<[[<'},
    {'right': '>||o',         'left':'o||<',},
    {'right': '>))o',         'left':'o[[<'},
    {'right': '>-==>',        'left':'<==-<'},
    {'right': r'>\\>',        'left':'<//<'},
    {'right': '><)))*>',      'left':'<*(((><'},
    {'right': '}-[[[*>',      'left':'<*]]]-{'},
    {'right': ']-<)))b>',     'left':'<d(((>-['},
    {'right': '><XXX*>',      'left':'<*XXX><'},
    {'right': '><(((º>',      'left':'<º)))><'}
                    ] 

def get_colours(col_num):        
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)
    return curses.color_pair(col_num)

num_of_bubles = 7 # number of bubles
bub_pos = [[random.randint(0,110),random.randint(15,28)] for i in range(num_of_bubles)]
num_of_seaweeds = 4 # number of seaweed 
num_of_fishes = 7 # number of fishes
fishes_pov = [[random.randint(0,110),random.randint(2,28),random.choice([True,False]),random.randint(3,35),random.choice(FISH_TYPES),
               random.choice([[random.randint(1,6),random.randint(1,6)],[random.randint(1,6)]])] for i in range(num_of_fishes)]

def seaweed(sea_weeds):
    for seaweed in sea_weeds:
        s = ''
        for _ in range(sea_weeds[seaweed][1]):
            rand = random.choice(['(',')'])
            s += rand
        sea_weeds[seaweed][0].clear()
        sea_weeds[seaweed][0].addstr(s,get_colours(4))
        sea_weeds[seaweed][0].refresh()


def bubles(stdsrc):
    for i in bub_pos:
        stdsrc.addstr(i[1],i[0],' ')
        stdsrc.refresh()
        i[1] -= 1
        stdsrc.addstr(i[1],i[0],'0')
        stdsrc.refresh()
        if i[1]<8:
            stdsrc.addstr(i[1],i[0],' ')
            i[0] = random.randint(0,110)
            i[1] = 28     
     
def ground():
    ground = curses.newwin(2,120,28,0)
    ground.addstr('░'*119+' '+'░'*119,get_colours(1))
    ground.refresh()
    
def get_fish(stdsrc):
    stdsrc.clear()

    for i in range(num_of_fishes):
        x_pos,y_pos,side,num_of_turn,fish,colour_option = fishes_pov[i]
        if side:
            fish_side = fish.get('right')
        else:
            fish_side = fish.get('left')
        if len(colour_option) == 2:
            head_tail_col = get_colours(colour_option[0])
            body_col = get_colours(colour_option[1])
            stdsrc.addstr(y_pos,x_pos,f'{fish_side[0]}',head_tail_col)
            stdsrc.addstr(f'{fish_side[1:len(fish_side)-1]}',body_col)
            stdsrc.addstr(f'{fish_side[len(fish_side)-1]}',head_tail_col)
        elif len(colour_option) == 1:
            body_col = get_colours(colour_option[0])
            stdsrc.addstr(y_pos,x_pos,fish_side,body_col)
        y_pos += random.choice([-1,0,0,0,0,1])
        
        if y_pos>26:
            y_pos -= 2
        elif y_pos<2:
            y_pos += 2
            
        if side:
            if x_pos+len(fish)>115:
                side = False
                x_pos -= 1
            else:
                x_pos += 1
        else:
            if x_pos<1:
                side = True
                x_pos += 1
            else:
                x_pos += -1
                   
        if num_of_turn == 0:
            side = False if side else True
            num_of_turn = random.randint(3,35)
        else:
            num_of_turn -= 1
            
        fishes_pov[i] = (x_pos,y_pos,side,num_of_turn,fish,colour_option)
    stdsrc.refresh()

@wrapper
def tank(stdsrc):
    global seaweeds
    curses.curs_set(0)
    stdsrc.clear()
    stdsrc.bkgd(' ',get_colours(3))
    stdsrc.refresh()
    sea_weeds = {}
    
    for i in range(num_of_seaweeds):
        size = random.randint(7,25)
        x_pov = random.randint(5,99)
        sea_weeds[i] = (curses.newwin(size,1,29-size,x_pov),size-1)
    while True:
        try:
            get_fish(stdsrc)
            seaweed(sea_weeds)
            ground()
            bubles(stdsrc)
            time.sleep(0.5)
        except KeyboardInterrupt:
            break
