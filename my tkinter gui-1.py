from tkinter import *

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator=''
    text_Input.set("")

def btnEquals():
    global operator
    try:
        sumup=str(eval(operator))
        text_Input.set(sumup)
        operator=''
    except:
        operator=''
        text_Input.set("ERROR")
        

root=Tk()
root.title("Calculator")
operator=''
text_Input=StringVar()

 

txtDisplay=Entry(root, font=('arial', 15,'bold'),bg='#F0EFE7', textvariable=text_Input,bd=0,insertwidth=5,justify='right',width=28).grid(sticky='e',columnspan=4)



b1=Button(root,text='CE',bd=0,bg='#E8E6E6',fg='black',width=8,height=11, command=btnClear)
b1.grid(row=1,column=4,rowspan=5,padx=2,pady=2)


b5=Button(root,text='7',bd=0,bg='white',fg='black',width=8,height=2,command=lambda:btnClick('7'))
b5.grid(row=2,column=0,padx=2,pady=2)
b6=Button(root,text='8',bd=0,bg='white',fg='black',width=8,height=2,command=lambda:btnClick('8'))
b6.grid(row=2,column=1,padx=2,pady=2)
b7=Button(root,text='9',bd=0,bg='white',fg='black',width=8,height=2,command=lambda:btnClick('9'))
b7.grid(row=2,column=2,padx=2,pady=2)
b8=Button(root,text='X',bd=0,bg='#E8E6E6',fg='black',width=8,height=2,command=lambda:btnClick('*'))
b8.grid(row=2,column=3,padx=2,pady=2)

b9=Button(root,text='4',bd=0,bg='white',fg='black',width=8,height=2,command=lambda:btnClick('4'))
b9.grid(row=3,column=0,padx=2,pady=2)
b10=Button(root,text='5',bd=0,bg='white',fg='black',width=8,height=2,command=lambda:btnClick('5'))
b10.grid(row=3,column=1,padx=2,pady=2)
b11=Button(root,text='6',bd=0,bg='white',fg='black',width=8,height=2,command=lambda:btnClick('6'))
b11.grid(row=3,column=2,padx=2,pady=2)
b12=Button(root,text='-',bd=0,bg='#E8E6E6',fg='black',width=8,height=2,command=lambda:btnClick('-'))
b12.grid(row=3,column=3,padx=2,pady=2)

b13=Button(root,text='1',bd=0,bg='white',fg='black',width=8,height=2,command=lambda:btnClick('1'))
b13.grid(row=4,column=0,padx=4,pady=4)
b14=Button(root,text='2',bd=0,bg='white',fg='black',width=8,height=2,command=lambda:btnClick('2'))
b14.grid(row=4,column=1,padx=2,pady=2)
b15=Button(root,text='3',bd=0,bg='white',fg='black',width=8,height=2,command=lambda:btnClick('3'))
b15.grid(row=4,column=2,padx=2,pady=2)
b16=Button(root,text='+',bd=0,bg='#E8E6E6',fg='black',width=8,height=2,command=lambda:btnClick('+'))
b16.grid(row=4,column=3,padx=2,pady=2)

b17=Button(root,text='.',bd=0,bg='#E8E6E6',fg='black',width=8,height=2,command=lambda:btnClick('+-'))
b17.grid(row=5,column=0,padx=2,pady=2)
b18=Button(root,text='0',bd=0,bg='white',fg='black',width=19,height=2,command=lambda:btnClick('0'))
b18.grid(row=5,column=1,columnspan=2,padx=2,pady=2)
b19=Button(root,text='/',bd=0,bg='#E8E6E6',fg='black',width=8,height=2,command=lambda:btnClick('/'))
b19.grid(row=5,column=3,padx=2,pady=2)

b20=Button(root,text='=',bd=0,bg='#E8E6E6',fg='black',width=49,height=2,command=btnEquals)
b20.grid(row=6,column=0,columnspan=5,padx=2,pady=2)







root.mainloop()
