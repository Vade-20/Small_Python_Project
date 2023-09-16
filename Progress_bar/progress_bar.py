import curses
from time import sleep

num_of_iterations = 500000


def bar(num_of_iterations:int):
    stdsrc = curses.initscr()
    curses.noecho()  # Turn off automatic echoing of keys to the screen
    curses.cbreak()  # React to keys instantly (don't wait for Enter)
    stdsrc.keypad(True)  # Enable special keys like arrow keys
    curses.start_color()
    BLOCK = chr(9608) # Character 9608 is '█'

    try:
        stdsrc.clear()
        stdsrc.refresh()
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        GREEN = curses.color_pair(1)
        RED = curses.color_pair(2)

        stdsrc.addstr('Progress Bar \n',GREEN)
        stdsrc.addstr('[',GREEN)
        stdsrc.addstr(1,52,']',GREEN)
        stdsrc.refresh()
        bar_win =  curses.newwin(1,51,1,1) 
        percentage_win = curses.newwin(1,20,1,54) 
        value_ = 0
        bar_percentage = 0
        for _ in range(1,num_of_iterations+1):
            percentage_win.clear()
            value_ += 1
            current_percentage = int((value_*100)/num_of_iterations)
            percentage_win.addstr(f'{current_percentage}%  {value_}/{num_of_iterations}',RED)
            percentage_win.refresh()
            while bar_percentage<int(current_percentage/2):
                bar_win.addstr(BLOCK,RED)
                bar_win.refresh()
                bar_percentage += 1
        sleep(1)
        print('Progress Completed')
    finally:
        # Cleanup curses
        curses.nocbreak()
        stdsrc.keypad(False)
        curses.echo()
        curses.endwin()


if __name__=='__main__':
    bar(num_of_iterations)