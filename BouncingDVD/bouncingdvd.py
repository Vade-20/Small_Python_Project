from tkinter import *

colours = ['red','green','blue','yellow']
root = Tk()
canvas_size_x = 1000
canvas_size_y = 500
x_corr=1
y_corr=1
choice = 0
root.geometry(f'{canvas_size_x}x{canvas_size_y}')
canvas = Canvas(root,bg='black',highlightthickness=0)
canvas.pack(fill='both',expand=True)
dvd = canvas.create_text(50,50,text='DVD',fill=colours[choice],font=('Times new roman',35),width=101)

def moves():
    global x_corr,y_corr,dvd,choice
    x,y = canvas.coords(dvd)
    if int(x)>950:
        choice = choice + 1 if choice <3 else 0
        canvas.itemconfig(dvd, fill=colours[choice])
        x_corr=-1
        
    elif int(x)<50:
        choice = choice + 1 if choice <3 else 0
        canvas.itemconfig(dvd, fill=colours[choice])
        x_corr=1
        
    if int(y)>480:
        choice = choice + 1 if choice <3 else 0
        canvas.itemconfig(dvd, fill=colours[choice])
        y_corr=-1
    elif int(y)<20:
        choice = choice + 1 if choice <3 else 0
        canvas.itemconfig(dvd, fill=colours[choice])
        y_corr=1
        
    canvas.move(dvd,x_corr,y_corr)
    return root.after(10,moves)

    

moves()
mainloop()


