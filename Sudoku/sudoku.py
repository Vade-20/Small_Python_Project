from tkinter import *

root = Tk()
root.title('Sudoku')
root.config(bg='light blue')
FONT_COLOR = 'blue'
BACKGROUND_COLOR = 'light blue'


entry_list = []
l1 = Label(root, text='Sudoku', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '40'), bd=3, relief='solid',justify='center')
l1.grid(row=0, column=0, columnspan=13,sticky=W+E)
l2 = Label(root, text='      ', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '2'), bd=3, relief='sunken',justify='center')
l2.grid(row=1, column=0, columnspan=13,sticky=W+E)
for i in range(2,14):
    if i in [5,9,13]:
        l1 = Label(root, text='-'*110, fg=FONT_COLOR ,bg=BACKGROUND_COLOR ,font=('Times', '10'), bd=3, relief='flat')
        l1.grid(row=i, column=0, columnspan=13,sticky=W+E)
    else:
        for j in range(2,14):
            if j in [5,9,13]:
                l1 = Label(root, text='|', fg=FONT_COLOR,bg=BACKGROUND_COLOR  ,font=('Times', '10'), bd=3, relief='flat')
                l1.grid(row=i, column=j, sticky=W+E)
            else:
                e1 = Entry(root, fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '10'), bd=3, relief='groove',width=5,justify='center')
                e1.grid(row=i, column=j)
                entry_list.append(e1)
                
            






mainloop()