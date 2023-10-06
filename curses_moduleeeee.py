import curses
from curses import wrapper 
from time import sleep
from curses.textpad import Textbox,rectangle

def type_of_attribute(stdsrc):
    curses.curs_set(1) # Hide the cursor
    stdsrc.clear() # Clear the screen
    stdsrc.addstr('Hello world') #add string to the screen and can be overlapped and can be places anywhere on screen
    stdsrc.addstr(20,20,'I am the greatest in the world,this is bold',curses.A_BOLD) 
    stdsrc.addstr(25,20,'I am the greatest in the world,this will blink the text',curses.A_BLINK) 
    stdsrc.addstr(30,20,'I am the greatest in the world,this will revese the colour of background and font',curses.A_REVERSE) 
    stdsrc.addstr(35,20,'I am the greatest in the world,this should put a underline but it doesnt work as some terminal do not support it',curses.A_UNDERLINE) 
    stdsrc.addstr(40,20,'I am the greatest in the world,this will din the text',curses.A_DIM) 
    stdsrc.addstr(45,20,'I am the greatest in the world,this work similiar to reverse',curses.A_STANDOUT) 
    stdsrc.addstr(0,0,'Owned') 
    stdsrc.refresh() # Refresh the screen ie change the value on the screen 
    stdsrc.getch() #get character from keyboar

def colour(stdsrc):
    curses.curs_set(0) # Hide the cursor
    stdsrc.clear()
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_GREEN)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_WHITE)
    curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    BLUE_GREEN = curses.color_pair(1)
    RED_WHITE = curses.color_pair(2)
    YELLOW_BLACK = curses.color_pair(3)
    stdsrc.addstr(15,15,"This text is in the colour blue",BLUE_GREEN | curses.A_BOLD)
    stdsrc.addstr(20,15,"This text is in the colour red",RED_WHITE | curses.A_BOLD)
    stdsrc.addstr(30,15,"This text is in the colour yellow",YELLOW_BLACK | curses.A_BOLD)
    stdsrc.refresh() # Refresh the screen ie change the value on the screen 
    stdsrc.getch() #get character from keyboar

def count(stdsrc):
    curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    YELLOW_BLACK = curses.color_pair(1)
    curses.curs_set(0)
    for i in range(30):
        stdsrc.clear()
        stdsrc.addstr(20,20,f'COUNT : {i}',YELLOW_BLACK | curses.A_UNDERLINE)
        stdsrc.refresh()
        sleep(1)
    stdsrc.getch()
   
def new_win(stdsrc):
    cur_new = curses.newwin(1,10,10,10) #curses.newwin(height, width, begin_y, begin_x)
    curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_BLUE,curses.COLOR_GREEN)
    stdsrc.clear()
    YELLOW_BLACK = curses.color_pair(1)
    BLUE_GREEN = curses.color_pair(2)
    stdsrc.addstr("This text is in the colour blue",BLUE_GREEN | curses.A_BOLD)
    stdsrc.refresh()
    for i in range(1,31):
        cur_new.clear()
        cur_new.addstr(f'COUNT : {i}',YELLOW_BLACK | curses.A_UNDERLINE)
        cur_new.refresh()
        sleep(1)
    stdsrc.getch()

def pad_examples(stdsrc):
    stdsrc.clear()
    curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    YELLOW_BLACK = curses.color_pair(1)
    new_pad = curses.newpad(100,100)   #Tell us the size of the new pad
    stdsrc.refresh()
    for i in range(1,101):
        for i in range(26):
            ch= chr(67+i)
            new_pad.addstr(ch)
    new_pad.refresh(0,0,0,0,20,20) #First 2 arguments are the top left corner row and column 3 and 4 arguments are the place where the new pad should be and the 
                                    #last 2 arguments are the bottom right corner.       
                                     
    stdsrc.getch()


def mouse_scrolling(stdsrc):
    stdsrc.clear()
    curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    YELLOW_BLACK = curses.color_pair(1)
    new_pad = curses.newpad(100,100)   #Tell us the size of the new pad
    stdsrc.refresh()
    for i in range(1,101):
        for i in range(26):
            ch= chr(67+i)
            new_pad.addstr(ch)
    '''for i in range(50): #Horizontal scroll
        new_pad.refresh(0,i,5,5,20,20)
        sleep(0.2)
    for i in range(50): #Vertical scroll
        new_pad.refresh(i,0,5,5,20,20)
        sleep(0.2)   
    for i in range(50): #Moving with square scroll 
        stdsrc.clear()
        stdsrc.refresh()
        new_pad.refresh(0,0,5,i,20,20+i)
        sleep(0.2) 
    '''                                 
    for i in range(50): #idk how to describe this scroll
        stdsrc.clear()
        stdsrc.refresh()
        new_pad.refresh(0,i,5,i,20,20+i)
        sleep(0.2) 
                                     
    stdsrc.getch()
    

def move_a_chracter_on_screen(stdsrc):
    curses.curs_set(0)
    stdsrc.clear()
    stdsrc.refresh()
    x,y = 0,0
    stdsrc.addstr(y,x,'Hello')
    stdsrc.nodelay(True)  #Make sure that there is no delay between run and input event
    string_x = 0
    while True:
        try:
            ch = stdsrc.getkey()
        except curses.error:
            ch = None
        if ch == 'KEY_LEFT':
            x -= 1
        elif ch == 'KEY_RIGHT':
            x += 1
        elif ch == 'KEY_UP':
            y -= 1
        elif ch == 'KEY_DOWN':
            y += 1
        stdsrc.clear()
        string_x +=1
        stdsrc.addstr(0,string_x//100,'This is nice')
        stdsrc.addstr(y,x,'Hello')
      

def drawing_a_rectangle(stdsrc):
    curses.curs_set(0)
    stdsrc.clear()
    stdsrc.refresh()
    rectangle(stdsrc,5,5,10,20)
    stdsrc.getch()
    
def text_box(stdsrc):
    curses.curs_set(0)
    curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    YELLOW_BLACK = curses.color_pair(1)
    stdsrc.clear()
    stdsrc.refresh()
    new_win = curses.newwin(14,14,6,6)
    box = Textbox(new_win)
    rectangle(stdsrc,5,5,20,20)
    stdsrc.refresh()
    box.edit() #imp part for making refrence
    text_on_screen = box.gather()
    stdsrc.addstr(21,21,f'{text_on_screen}') #Press Ctrl + G to get out of textbox but remember it doesn't matter work in vscode but works in terminal
    stdsrc.getch()

def rectangle_with_color(stdsrc):
    curses.curs_set(0)
    stdsrc.clear()
    stdsrc.refresh()
    stdsrc.border() #+++++++++++++++++++++++++++++++++IMP+++++++++++++++ADD BORDER TO THE SCREEN
    curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    YELLOW_BLACK = curses.color_pair(1)
    stdsrc.attron(YELLOW_BLACK)
    stdsrc.addstr(0,0,'HEllo world nice')
    rectangle(stdsrc,5,5,10,20)
    stdsrc.attroff(YELLOW_BLACK)
    stdsrc.getch()
   
 
def moving_cursor(stdsrc):
    stdsrc.clear()
    stdsrc.refresh()
    stdsrc.addstr(5,5,'Hello world')
    stdsrc.move(10,10)
    stdsrc.addstr(10,10,'hello nice world')
    stdsrc.refresh()
    stdsrc.getch()

@wrapper
def typing_on_screen(stdsrc):
    stdsrc.clear()
    stdsrc.refresh()
    curses.echo()
    stdsrc.move(10,10)
    while True:
        key = stdsrc.getkey()
        if key == 'q':
            break
    