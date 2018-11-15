from tkinter import *
root=Tk()
root.title("windows")
TopFrame=Frame(root)
TopFrame.pack(side=TOP,expand=YES,fill=BOTH)
b1=Button(TopFrame,text='TOP1',bg='red',bd=10,font=('arial',15,'bold'),command=lambda:print('ok class'))
b1.pack(side=LEFT,expand=YES,fill=BOTH)
b11=Button(TopFrame,text='TOP2',bg='orange',fg='yellow',font=('arial',15,'bold'),command=lambda:print('ok class'))
b11.pack(side=LEFT,expand=YES,fill=BOTH)

BottomFrame=Frame(root)
BottomFrame.pack(side=BOTTOM,expand=YES,fill=BOTH)
b2=Button(BottomFrame,text='BOTTOM',bg='yellow',font=('arial',15,'bold'),command=lambda:print('bottom class'))
b2.pack(side=BOTTOM,expand=YES,fill=BOTH)

LeftFrame=Frame(root)
LeftFrame.pack(side=LEFT,expand=YES,fill=BOTH)
b1=Button(LeftFrame,text='LEFT',bg='green',bd=10,font=('arial',15,'bold'),command=lambda:print('LEFT class'))
b1.pack(side=LEFT,expand=YES,fill=BOTH)

RightFrame=Frame(root)
RightFrame.pack(side=RIGHT,expand=YES,fill=BOTH)
b1=Button(RightFrame,text='TOP1',bg='blue',font=('arial',15,'bold'),command=lambda:print('right class'))
b1.pack(side=LEFT,expand=YES,fill=BOTH)

root.geometry("600x300")
root.mainloop()
