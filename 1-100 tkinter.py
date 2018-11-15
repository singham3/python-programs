from tkinter import *
root=Tk()
root.geometry('900x800')
def Display(t):
    Button(root,text=str(t[0]*t[1]),bg='#000fff000',width=3,height=1).grid(row=t[0],column=t[1],padx=2,pady=2)
    
f=Frame(root,bg='blue')
for i in range(1,11):
    Label(root,text=str(i),bg='lightgrey',width=3,height=1,font=('arial',10,'bold')).grid(row=0,column=i,padx=2,pady=2)


for i in range(1,11):
    Label(root,text=str(i),bg='lightgrey',width=3,height=1,font=('arial',10,'bold')).grid(row=i,column=0,padx=2,pady=2)
    
for i in range(1,11):
    for j in range(1,11):
        b=Button(root,text='?',bg='white',width=3,height=1,command=lambda x=(i,j):Display(x))
        b.grid(row=i,column=j,padx=2,pady=2)
f.grid()
root.mainloop()
