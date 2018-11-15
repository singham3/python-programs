from tkinter import *

from tkinter import scrolledtext

root=Tk()
root.title('Redio Button')
root.geometry('350x200')
txt=scrolledtext.ScrolledText(root,width=40,height=10,bd=0,bg='#F0F0F0')
txt.pack(expand=YES,fill=BOTH)

root.mainloop()


