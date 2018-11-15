from tkinter import *

def one():
    e1.insert(0,'1')
def two():
    e1.insert(0,'2')

root = Tk()
e1=Entry(root,justify='right', bd=0,bg='light grey')
e1.grid(row=0,column=0)
root.title("ENTRY")

button=Button(root, text="1", command=one)
button.grid(row=1,column=0)
button2=Button(root, text="2", command=two)
button2.grid(row=1,column=1)
    

root.mainloop()
