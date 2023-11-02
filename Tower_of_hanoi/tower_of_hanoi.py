import curses
from curses import wrapper

class Tower:
    
    def __init__(self,size,top_value):
        self.size = size
        self.top = top_value
    
    def printing_tower(self):
        tower_str = ''
        for i in range(self.value):
            tower_str += f'{"@"*i}|{str(i).center(3)}|{"@"*i}\n'
        return tower_str
    
    def adding_values(self, tower_2):
        if self.top>tower_2.top:
            return None
        elif self.size == 0:
            return None
        
        self.size -= 1
        if self.size == 0:
            self.top = 0
        else:
            self.top += 1
            
        tower_2.top -= 1
        tower_2.size += 1

        
        
            
    
LENGHT_OF_TOWER = 5
NUMBER_OF_TOWER = 3
towers = {'A':[5,1]}
for i in range(1,NUMBER_OF_TOWER):
    ascii_code = chr(ord('A')+i)
    towers[ascii_code] = [0,0]

def rules(stdsrc,GREEN):
    stdsrc.clear()
    rule=''' 
        The objective of the puzzle is to move the entire stack to one of the other rods, obeying the following rules:
            1. Only one disk may be moved at a time.
            2. Each move consists of taking the upper disk from one of the stacks 
                and placing it on top of another stack or on an empty rod.
            3. No disk may be placed on top of a disk that is smaller than it.
            
        Press any key to continue...'''
    stdsrc.addstr(10,50,rule,GREEN)
    stdsrc.refresh()
    stdsrc.getch()
    stdsrc.clear()

def wining_condition():
    for i in towers:
        if i != 'A' and towers[i] == 5:
            return True
        else:
            return False


@wrapper
def main(stdsrc):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    GREEN = curses.color_pair(1)
    rules(stdsrc,GREEN)
    while not wining_condition():
        stdsrc.addstr(3,8,'Enter the letters of "from" and "to" towers, or QUIT.\n\t(e.g. AB to moves a disk from tower A to tower B.)',GREEN)
        stdsrc.refresh()
        stdsrc.getch()
        break
    
