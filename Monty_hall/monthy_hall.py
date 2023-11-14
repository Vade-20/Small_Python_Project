import random
import curses
from curses import wrapper

choices : {
"Door_1":'''
+-----------------------------------+
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
|               1                   |
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
+-----------------------------------+
''',
"Door_2":'''
+-----------------------------------+
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
|               2                   |
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
+-----------------------------------+
''',
"Door_3":'''
+-----------------------------------+
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
|               3                   |
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
+-----------------------------------+
''',
'Goat':'''
+------------------------------------------+
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⠴⣶⠷⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
|⠀⠀⠀⠀⠀⠀⠀⣠⢞⣿⠟⣥⡟⢁⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
|⠀⠀⠀⢿⣏⣶⣶⢷⣾⠷⣸⣿⢞⣽⢊⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    |
|⠀⠀⠀⠈⠻⣯⣀⡷⠖⣓⠒⣱⣟⡼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    |
|⠀⠀⠀⠀⣠⠞⠋⠀⣨⣴⡿⠘⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     |
|⢀⣤⠴⣏⡀⠀⠀⠀⠀⠉⠀⠀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠻⠟⣶    |
|⠸⢾⡤⠿⠃⠀⠀⠀⠀⢀⡠⠇⠸⠤⣤⣀⣀⣀⣠⡴⠒⠚⠉⠉⠉⠒⢢⣤⢷⡿  |
|⠀⠸⡸⡀⠀⢀⠀⡴⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠈⠁     |
|⠀⠀⠙⠒⠻⣥⢊⡂⡏⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⣿⠀⠀     |
|⠀⠀⠀⠀⠀⢻⠈⣧⡇⢣⠀⠀⢀⠀⡀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠰⡴⠃⠀⠀     |
|⠀⠀⠀⠀⠀⢸⠀⡿⠁⠈⠙⢲⠌⡄⢰⣀⣀⣀⣀⣀⣠⣤⣼⢤⠀⠘⡇⠀⠀⠀   |
|⠀⠀⠀⠀⠀⣞⡜⠁⠀⠀⠀⠀⡄⠃⠀⢇⠀⠀⠀⠀⠀⠀⢺⢸⠀⠀⡇⠀⠀⠀     |
|⠀⠀⠀⠀⠘⠋⠀⠀⠀⠀⢀⡴⠃⡀⠀⠸⡀⠀⠀⠀⠀⠀⢸⢸⠀⢀⡇⠀⠀      |
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⡂⣰⣇⠀⠄⣇⠀⠀⠀⠀⢠⣺⢈⠀⠀⡳⡄        |
|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠈⠓⠬⠇⠀⠀⠀⠀⠀⠈⠉⠑⠲⠞⠁⠀⠀     |
+------------------------------------------+
''',
'Car':'''
+------+
| CAR! |
|    __|
|  _/  |
| /_ __|
|   O  |
+------+''',
}

def rules(stdsrc,color):
    stdsrc.clear()
    stdsrc.refresh()
    rules= '''The Monty Hall Problem

In the Monty Hall game show, you can pick one of three doors. One door
has a new car for a prize. The other two doors have worthless goats:


+------+  +------+  +------+
|      |  |      |  |      |
|   1  |  |   2  |  |   3  |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+

Say you pick Door #1.
Before the door you choose is opened, another door with a goat is opened:


+------+  +------+  +------+
|      |  |      |  |  ((  |
|   1  |  |   2  |  |  oo  |
|      |  |      |  | /_/|_|
|      |  |      |  |    | |
|      |  |      |  |GOAT|||
+------+  +------+  +------+
You can choose to either open the door you originally picked or swap
to the other unopened door.


It may seem like it doesn't matter if you swap or not, but your odds
do improve if you swap doors! This program demonstrates the Monty Hall
problem by letting you do repeated experiments.


You can read an explanation of why swapping is better at
https://en.wikipedia.org/wiki/Monty_Hall_problem

Press Enter to start...'''
    stdsrc.addstr(2,5,rules,color)
    stdsrc.refresh()
    stdsrc.getch()
    stdsrc.clear()
    stdsrc.refresh()

@wrapper
def main(stdsrc):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_BLUE,curses.COLOR_BLACK)
    stdsrc.clear()
    GREEN = curses.color_pair(1)
    BLUE = curses.color_pair(2)
    cur_new = curses.newwin(1,10,10,10)
