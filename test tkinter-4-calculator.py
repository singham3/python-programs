from tkinter import *
import time
root=Tk()
root.title("Calculator second")
root.geometry('300x350')
def Display(value):
    global s
    s=s + str(value)
    text.set(s)
def result():
    global s
    try:
        s1=str(eval(s))
        text.set(s1)
        s=''
    except:
        s=''
        text.set('ERROR')
def counter_label(label):
    counter=0
    def count():
        global counter
        counter=counter+1
        label.config(text=time.ctime())
        label.after(1000,count)
    count()
def clear():
    global s
    s=''
    text.set(s)
def clear1():
    global s
    s=s[:len(s)-1]
    text.set(s)
counter=0
s=''
text=StringVar()
e1=Entry(font=('arial', 15,'bold'), textvariable=text,bd=0,bg='#F0EFE7',justify='right',width=25).grid(padx=2,pady=2,sticky='nswe',columnspan=4)
s1=['798/','456*','123+','.0-']
k=1
for i in s1:
    l=0
    for j in i:
        b=Button(root,text=j,bd=0,width=8,height=2,bg='white',font=('arial',10,'bold'),command=lambda x=j:Display(x))
        b.grid(row=k,column=l,sticky='nswe',padx=2,pady=2)
        l=l+1
    k=k+1
b2=Button(root,text='=',bd=0,bg='lightgrey',font=('arial',10,'bold'),width=8,height=2,command=result)
b2.grid(row=4,column=3,sticky='nswe',padx=2,pady=2)
b2=Button(root,text='CE',bd=0,bg='lightgrey',font=('arial',10,'bold'),width=8,height=2,command=clear1)
b2.grid(row=5,column=0,columnspan=2,sticky='nswe',padx=2,pady=2)
b2=Button(root,text='C',bd=0,bg='lightgrey',font=('arial',10,'bold'),width=8,height=2,command=clear)
b2.grid(row=5,column=2,columnspan=2,sticky='nswe',padx=2,pady=2)
label=Label(root,font=('arial',15,'bold'),height=3)
label.grid(row=7,column=0,columnspan=4,sticky='nswe',padx=5,pady=5)
counter_label(label)
root.mainloop()
