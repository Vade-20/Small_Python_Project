from numbers_ import number_patterns
import curses
from curses import wrapper
from time import sleep,localtime


@wrapper
def main(stdscr):
  curses.curs_set(0)
  curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLACK)
  YELLOW_BLACK = curses.color_pair(1)
  while True:
    current_time = localtime()
    hours = current_time.tm_hour if len(str(current_time.tm_hour))==2 else '0'+str(current_time.tm_hour)
    minutes = current_time.tm_min if len(str(current_time.tm_min))==2 else '0'+str(current_time.tm_min)
    seconds = current_time.tm_sec if len(str(current_time.tm_sec))==2 else '0'+str(current_time.tm_sec)
    t = f"{hours}:{minutes}:{seconds}"
    a = 0 
    stdscr.clear()
    for i in str(t):
      i = int(i) if i.isdigit() else i
      cur_win = curses.newwin(0,0,15,a+15)
      num = number_patterns.get(i)
      cur_win.addstr(num,YELLOW_BLACK)
      a +=10
      cur_win.refresh()
    sleep(1)
