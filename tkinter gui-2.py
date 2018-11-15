from tkinter import *
root=Tk()
root.title("windows")

b1=Button(root,text='TOP',bg='red',bd=10,font=('arial',15,'bold'),width=6,height=3)
b1.grid(row=0,column=0,padx=5,pady=5)


b2=Button(root,text='BOTTOM',bg='yellow',bd=10,font=('arial',15,'bold'),width=6,height=3)
b2.grid(row=0,column=0,padx=5,pady=5)


b3=Button(root,text='LEFT',bg='green',bd=10,font=('arial',15,'bold'),width=6,height=3)
b3.grid(row=0,column=0,padx=5,pady=5)


b4=Button(root,text='RIGHT',bg='blue',bd=10,font=('arial',15,'bold'),width=6,height=3)
b4.grid(row=0,column=0,padx=5,pady=5)

root.geometry("600x300")
root.mainloop()
