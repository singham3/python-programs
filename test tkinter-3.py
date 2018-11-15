from tkinter import *

def show_entry_fields():
    print('First Name: %s\nLast name: %s'%(e1.get(), e2.get()))
    e1.delete(0,END)
    e2.delete(0,END)

root = Tk()
Label(root, text='First Name').grid(row=0)
Label(root, text='Last Name').grid(row=1)

e1=Entry(root)
e2=Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)


Button(root, text="QUIT", command=root.quit).grid(row=3,column=0, pady=4,sticky=W)
Button(root, text="SHOW", command=show_entry_fields).grid(row=3,column=1,sticky=W,pady=4)
    

root.mainloop()
