from tkinter import *
from tkinter import scrolledtext 

try:
    import pyttsx3
except ImportError:
    print('The pyttsx3 module needs to be installed to run this')
    print('program. On Windows, open a Command Prompt and run:')
    print('pip install pyttsx3')
    print('On macOS and Linux, open a Terminal and run:')
    print('pip3 install pyttsx3')
    quit()
    
def validate_input(value):
    if value.isdigit():
        return True
    else:
        return False
    
engine = pyttsx3.init()  # Initialize the TTS engine.
root = Tk()
root.title('Text to speech ')
vcmd = (root.register(validate_input), '%P')

def speak():
    a = t1.get(1.0,END)
    engine.say(a)
    engine.runAndWait()
    
l1 = Label(root, text='Text to speech converter', fg='blue', bg='light grey', padx=250, font=('Times', '40'), bd=3, relief='sunken')
l1.grid(row=0, column=0, columnspan=6)
l2 = Label(root, text='                  ', fg='blue', bg='light grey', padx=250, bd=3, relief='sunken')
l2.grid(row=1, column=0, columnspan=6,sticky=W+E)
l3 = Label(root, text='Gender', fg='blue', bg='light grey', padx=50, font=('Times',15), bd=3, relief='sunken')
l3.grid(row=2, column=3,sticky=W+E)

l1 = Label(root, text='Text to speech converter', fg='blue', bg='light grey', padx=250, font=('Times', '40'), bd=3, relief='sunken')
l1.grid(row=0, column=0, columnspan=6)
l1 = Label(root, text='Text to speech converter', fg='blue', bg='light grey', padx=250, font=('Times', '40'), bd=3, relief='sunken')
l1.grid(row=0, column=0, columnspan=6)


t1 = scrolledtext.ScrolledText(root, wrap = WORD, width = 40, height = 10, font = ("Times New Roman",15)) 
t1.insert(1.0,'Text here')
t1.grid(row=2,column=0,columnspan=3,rowspan=3,sticky=W+E)

b1 = Button(root,text = 'Speak',fg='blue',font= ('Comic Sans MS', '20'),command=speak,width=15,relief='sunken')
b1.grid(row=5,column=0,sticky=W+E)

'''s1 = Spinbox(root, from_= 0, to = 20,validate="key", validatecommand=vcmd) 
s1.grid(row=3,column=4,columnspan=3,sticky=W+E)
'''
mainloop()



