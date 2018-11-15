from tkinter import *

canvas_width=500
canvas_height=150

def paint():
    python_green='black'
    x1,y1=(event.x-1),(event.y-1)
    x2,y2=(event.x+1),(event.y+1)
    w.create_ovel(x1,y1,x2,y2,fill=pyhton_green)
root=Tk()
root.title('painting using ovel')
w=canvas(root,width=canvas_width,height=canvas_height)
w.pack(expend=YES,fill=BOTH)
w.bind('<B1-motion>')

root.mainloop()


