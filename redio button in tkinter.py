from tkinter import *

from tkinter.ttk import *

root=Tk()
root.title('Redio Button')
root.geometry('350x200')
selected=IntVar()
selected2=IntVar()
red1= Radiobutton(root,text='1st',value=1,variable=selected)
red2= Radiobutton(root,text='2nd',value=2,variable=selected)
red3= Radiobutton(root,text='3rd',value=3,variable=selected)
red4= Radiobutton(root,text='4th',value=4,variable=selected2)
red5= Radiobutton(root,text='5th',value=5,variable=selected2)

def clicked():
    print(selected.get())
    
def click():
    print(selected2.get())

btn=Button(root,text='Click Me',command=clicked)
btn2=Button(root,text='Click Me',command=click)

red1.grid(column=0,row=0)
red2.grid(column=1,row=0)
red3.grid(column=2,row=0)
red4.grid(column=0,row=1)
red5.grid(column=1,row=1)

btn.grid(column=3,row=0)
btn2.grid(column=3,row=1)
root.mainloop()


