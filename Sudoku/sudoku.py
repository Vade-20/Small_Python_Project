from tkinter import *

root = Tk()
root.title('Sudoku')
root.config(bg='light blue')
FONT_COLOR = 'blue'
BACKGROUND_COLOR = 'light blue'

def validate_input(value):
    if (value.isdigit() or value=='') and value !='0':
        return True
    else:
        return False

def winining_condition(event):
    for entry in entry_list:
        for i in entry:
            value = i.get()
            if len(value) >1:
                i.delete(0,END)
                i.insert(0,value[0])
                
            
        
vcmd = (root.register(validate_input), '%P')

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
        dummy_list = []
        for j in range(2,14):
            if j in [5,9,13]:
                l1 = Label(root, text='|', fg=FONT_COLOR,bg=BACKGROUND_COLOR  ,font=('Times', '10'), bd=3, relief='flat')
                l1.grid(row=i, column=j, sticky=W+E)
            else:
                e1 = Entry(root, fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '10'), bd=3, relief='groove',width=5,justify='center',validate='key',validatecommand=vcmd)
                e1.grid(row=i, column=j)
                dummy_list.append(e1)
        entry_list.append(dummy_list)
    
                

root.bind('<Key>',winining_condition)
mainloop()