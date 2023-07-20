from numbers_ import number_patterns
import curses
from curses import wrapper
from time import sleep
from datetime import datetime
import winsound

def correct_time():
  #Set the time accouding to you need here
  #-------------------------------------------
  hours = 0
  minutes = 0
  seconds =300
  #--------------------------------------------
  if not  str(hours).isdigit() or not str(minutes).isdigit() or not str(seconds).isdigit():
    raise Exception ("Please enter an integer in time")
  elif hours<0 or minutes<0 or seconds<0:
    raise Exception ("Please enter an integer greater than 0 in time")
  
  if seconds>59:
    minutes += seconds//60
    seconds = seconds%60
    
  if minutes>59:
    hours += minutes//60
    minutes = minutes%60
  
  if hours>23:
    raise Exception ("Please,for hour only enter a value less than 23")
  
  t = f"{hours}::{minutes}::{seconds}"
  a= datetime.strptime(t, '%H::%M::%S').time()
  return a 

@wrapper
def main(stdscr):
  curses.curs_set(0)
  n = correct_time()
  hours = n.hour
  minutes = n.minute
  seconds = n.second
  while str(n)!='00:00:00':
    if seconds<0:
      minutes -=1
      seconds = 59
    if minutes<0:
      hours -= 1
      minutes = 59
    t = f"{hours}::{minutes}::{seconds}"
    n = datetime.strptime(t,'%H::%M::%S').time()
    a = 0 
    stdscr.clear()
    for i in str(n):
      i = int(i) if i.isdigit() else i
      cur_win = curses.newwin(10,20,10,a+10)
      num = number_patterns.get(i)
      cur_win.addstr(num)
      a +=10
      cur_win.refresh()
    seconds -= 1
    sleep(1)
  winsound.Beep(200,5000)
