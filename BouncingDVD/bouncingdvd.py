from tkinter import *
from random import randint

colours = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
root = Tk()
root.title("DVD")
canvas_size_x = 1000
canvas_size_y = 500
choice = 0
num_of_dvd = 5
count = 0
root.geometry(f'{canvas_size_x}x{canvas_size_y}')


canvas = Canvas(root,bg='black',highlightthickness=0)
canvas.pack(fill='both',expand=True)
counting = canvas.create_text(80,20,text='Count : 0',fill=colours[0],font=('Times new roman',20))

DVDS = [0 for i in range(num_of_dvd)]
last_move = {}
for i in range(num_of_dvd):
    DVDS[i] = canvas.create_text(randint(50,950),randint(50,480),text='DVD',fill=colours[randint(0,6)],font=('Times new roman',15),width=101)
    last_move[DVDS[i]] = (2,2)
    
def moves():
    global x_corr,y_corr,choice,count
    for dvd in DVDS:
        canvas.itemconfig(counting,text = f'Count : {count}')
        try:
            x_corr,y_corr = last_move[dvd]
            x,y = canvas.coords(dvd)
            if int(x)>980:
                count+=1
                choice = choice + 1 if choice <6 else 0
                canvas.itemconfig(dvd, fill=colours[choice])
                x_corr=-2
                
            elif int(x)<25:
                count+=1
                choice = choice + 1 if choice <6 else 0
                canvas.itemconfig(dvd, fill=colours[choice])
                x_corr=+2
                
            if int(y)>475:
                count+=1
                choice = choice + 1 if choice <6 else 0
                canvas.itemconfig(dvd, fill=colours[choice])
                y_corr=-2
            
            elif int(y)<20:
                count+=1
                choice = choice + 1 if choice <6 else 0
                canvas.itemconfig(dvd, fill=colours[choice])
                y_corr=+2
            
            last_move[dvd] = (x_corr,y_corr)  
            canvas.move(dvd,x_corr,y_corr)
            canvas.update()
        except TclError:
            quit()
    root.after(10,moves)

moves()
mainloop()


