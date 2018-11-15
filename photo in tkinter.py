from tkinter import *

root=Tk()
w=Canvas(root,width=200, height=100)
w.pack()
w.create_rectangle(50,20,150,80,fill='green')

w.create_rectangle(65,35,135,65,fill='yellow')
w.create_line(0,0,50,20,width=2,fill='red')
w.create_line(0,100,50,80,width=2,fill='red')
w.create_line(150,20,200,0,width=2,fill='red')
w.create_line(150,80,200,100,width=2,fill='red')
w.create_text(100,50,text='Python')



root.mainloop()


