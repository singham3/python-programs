from tkinter import *

root=Tk()
def Display():
    l=listbox.curselection()
    print(l)

listbox=Listbox(root,selectmode=EXTENDED)
listbox.pack()

listbox.insert(END,'a list entry')
s=['one','two','three','four']
for item in s:
    listbox.insert(END,item)
    
    
Button(root,text='ok',command=Display).pack()
root.mainloop()
