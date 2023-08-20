from random import randint
import curses
from curses import wrapper

boxes = {
'red_box_close' : ''' 
  __________ 
 /         /|
+---------+ |
|   RED   | |  
|   BOX   | / 
+---------+/  
''',
'gold_box_close':'''
  __________
 /         /|
+---------+ |
|   GOLD  | |
|   BOX   | /
+---------+/''',
'red_box_open_empty':'''
   _________
  |         |
  |         |
  |_________|
 /         /|
+---------+ |
|   RED   | |
|   BOX   | /
+---------+/''',
'red_box_open_carrot':'''
   ___VV____ 
  |   VV    |
  |   VV    |
  |___||____|
 /    ||   /|
+---------+ |
|   RED   | | 
|   BOX   | / 
+---------+/''',
'gold_box_open_carrot':'''
   ___VV____ 
  |   VV    |
  |   VV    |
  |___||____|
 /    ||   /|
+---------+ |
|   GOLD  | | 
|   BOX   | / 
+---------+/'''}

def add_wrapped_str(win, x,y, text, width,colour):
    words = text.split()
    line = ''
    for word in words:
        if len(line) + len(word) + 1 <= width:
            line += word + ' '
        else:
            win.addstr(y, x, line,colour)
            y += 1
            line = word + ' '
    win.addstr(y, x, line,colour)
    
@wrapper
def main(stdsrc):
    stdsrc.clear()
    stdsrc.refresh()
    width = curses.COLS
    if width<98:
        raise Exception ('Press increase the width of your terminal')
    curses.echo()
    
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_BLACK)
    RED = curses.color_pair(1)
    YELLOW = curses.color_pair(2)
    GREEN = curses.color_pair(3)
    
    #1 part
    stdsrc.addstr(0,20,'Carrot in a box',GREEN)
    rules = '''This is a bluffing game for two human players. Each player has a box.One box has a carrot in it. To win, you must have the box with the carrot in it.The first player looks into their box (the second player must close their eyes during this.) The first player then says "There is a carrot in my box" or "There is not a carrot in my box". The second player then gets to decide if they want to swap boxes or not.
    '''
    add_wrapped_str(stdsrc,0,2,rules,width,GREEN)
    stdsrc.addstr(6,0,'Player 1 name : ',GREEN)
    player_1 = stdsrc.getstr(6,16).decode(encoding="utf-8")
    stdsrc.addstr(8,0,'Player 2 name : ',GREEN)
    player_2 = stdsrc.getstr(8,16).decode(encoding="utf-8")
    stdsrc.clear()
    stdsrc.addstr(0,10,'HERE ARE THE TWO BOXES--->',GREEN)
    stdsrc.refresh()
    box_1 = curses.newwin(15,20,2,0)
    box_1.addstr(boxes['red_box_close'],RED)
    box_1.addstr(f'\n  {player_1}',RED)
    box_1.refresh()
    box_2 = curses.newwin(11,20,17,0)
    box_2.addstr(boxes['gold_box_close'],YELLOW)
    box_2.addstr(f'\n  {player_2}',YELLOW)
    box_2.refresh()
    
    rule_box = curses.newwin(13,80,4,35)
    rule_box.addstr(f'    \n\n  {player_1}, you have a RED box in front of you.\n\n  {player_2}, you have a GOLD box in front of you.\n\n  {player_1}, you will get to look into your box.\n\n  {player_2}, close your eyes and don\'t look!!!\n\n  When {player_2} has closed their eyes, press Enter...',GREEN)
    rule_box.border()
    rule_box.refresh()
    rule_box.getch()
    # 2 part
    box_1.clear()
    rand = randint(1,2)
    if rand == 1:
        box_1.addstr(boxes['red_box_open_carrot'],RED)
        box_1.addstr(f'\n{player_1}',RED)
        box_1.addstr('\nCarrot Found!!',GREEN)
    else:
        box_1.addstr(boxes['red_box_open_empty'],RED)
        box_1.addstr(f'\n{player_1}',RED)
        box_1.addstr('\nNo Carrot!!',GREEN)
    box_1.refresh() 
    
    rule_box.clear()
    rule_box.addstr('\n\n  Press Enter to continue...',GREEN)
    rule_box.border()
    rule_box.refresh()
    rule_box.getch()
    # 3 part
    
    box_1.clear()
    box_1.addstr(boxes['red_box_close'],RED)
    box_1.addstr(f'\n{player_1}',RED)
    box_1.refresh()
    
    rule_box.clear()
    rule_box.addstr(f'    \n  {player_1}, tell {player_2} to open their eyes.',GREEN)
    rule_box.addstr('\n  Press Enter to continue...',GREEN)
    rule_box.border()
    rule_box.refresh()
    
    rule_box.getch()
    
    rule_box.addstr(f'\n  {player_1}, say one of the following sentences to {player_2}',GREEN)
    rule_box.addstr(f'\n        1) There is a carrot in my box.',GREEN)
    rule_box.addstr(f'\n        2) There is not a carrot in my box.',GREEN)
    rule_box.addstr(f'\n  Press Enter to continue....',GREEN)
    rule_box.border()
    rule_box.refresh()
    rule_box.getch()
    rule_box.addstr(f'\n  {player_2},do you want to swap boxes with {player_1} (Y/N) : ',GREEN)
    rule_box.border()
    rule_box.refresh()
    
    ans = str(rule_box.getstr().decode(encoding="utf-8")).lower()
    
    if ans[0] not in ['y','n']:
            ans = 'n'
    
    if ans[0] != 'y' and rand==1:
        rule_box.addstr(f'    Press Enter to reveal the winner....',GREEN)
        rule_box.border()
        rule_box.refresh()
        rule_box.getch()
        box_1.clear()
        box_1.addstr(boxes['red_box_open_carrot'],RED)
        box_1.addstr(f'\n {player_1}')
        box_1.refresh()
        rule_box.clear()
        rule_box.addstr(f'\n\n\n\n\n\n\t\t{player_1} ,is the winner!!!!!!!!!'.upper(),RED)
        rule_box.border()
        rule_box.refresh()
        
    elif ans[0] != 'y' and rand!=1:
        rule_box.addstr(f'  Press Enter to reveal the winner....',GREEN)
        rule_box.border()
        rule_box.refresh()
        rule_box.getch()
        box_2.clear()
        box_2.addstr(boxes['gold_box_open_carrot'],YELLOW)
        box_2.addstr(f'\n  {player_2}')
        box_2.refresh()
        rule_box.clear()
        rule_box.addstr(f'\n\n\n\n\n\n\t\t{player_2} ,is the winner!!!!!!!!!'.upper(),YELLOW)
        rule_box.border()
        rule_box.refresh()
    else:
        box_1.clear()
        box_2.clear()
        box_1.addstr(boxes['gold_box_close'],YELLOW)
        box_1.addstr(f'\n {player_1}',YELLOW)
        box_2.addstr(boxes['red_box_close'],RED)
        box_2.addstr(f'\n {player_2}',RED)
        box_2.refresh()
        box_1.refresh()
        rule_box.clear()
        rule_box.addstr('\n\n  The boxes are switched...',GREEN)
        rule_box.border()
        rule_box.refresh()
        rule_box.getch()
        if rand!=1:
            rule_box.addstr(f'\n  Press Enter to reveal the winner....',GREEN)
            rule_box.border()
            rule_box.refresh()
            rule_box.getch()
            box_1.clear()
            box_1.addstr(boxes['gold_box_open_carrot'],YELLOW)
            box_1.addstr(f'\n {player_1}',YELLOW)
            box_1.refresh()
            rule_box.clear()
            rule_box.addstr(f'\n\n\n\n\n\n\t\t{player_1} ,is the winner!!!!!!!!!'.upper(),YELLOW)
            rule_box.border()
            rule_box.refresh()
        elif rand==1:
            rule_box.addstr(f'    Press Enter to reveal the winner....',GREEN)
            rule_box.border()
            rule_box.refresh()
            rule_box.getch()
            box_2.clear()
            box_2.addstr(boxes['red_box_open_carrot'],RED)
            box_2.addstr(f'\n {player_2}',RED)
            box_2.refresh()
            rule_box.clear()
            rule_box.addstr(f'\n\n\n\n\n\n\t\t{player_2} ,is the winner!!!!!!!!!'.upper(),RED)
            rule_box.border()
            rule_box.refresh() 
    rule_box.getch()
    
    
