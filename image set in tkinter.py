from tkinter import *

canvas_width=300
canvas_height=300


root=Tk()

w=Canvas(root,width=canvas_width,height=canvas_height)
w.pack(expend=YES,fill=BOTH)
img=PhotoImage(fill='C:\\Users\\singham\\Downloads\\waterfall.gif')
w.create_image(20,20,anchor=NW)

root.mainloop()


