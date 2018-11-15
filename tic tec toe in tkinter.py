from tkinter import *

root=Tk()
root.title('Tic Tec Toe')
root.geometry('360x555')

l=[]

def button():
    for i in range(1,4):
        for j in range(1,4):
            l.append(Button(root,width=15,height=8,bd=0,bg='white',state='disable')
            l.grid(row=i,column=j,padx=2,pady=2)

def f():
    for i in l:
        i['state']='active'

        b1['text']='Restart'
        b1['state']='disable'

button()
b1=Button(root,text='Start',command=f)
b1.grid(row=4,column=1)


root.mainloop()
