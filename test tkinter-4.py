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
        btnClear()
        

root=Tk()
root.title("Calculator")
operator=''
text_Input=StringVar()



txtDisplay=Entry(root, font=('arial', 15,'bold'), textvariable=text_Input,bd=0,bg='#F0EFE7',insertwidth=5,justify='right',width=30).grid(columnspan=4)



 
 

photo1=PhotoImage(file="C:\\Users\\singham\\Downloads\\CE.png")
b1=Button(root,image=photo1,bd=0,width=327,height=35, command=btnClear)
b1.grid(row=1,column=0,columnspan=4,padx=2,pady=2)



photo5=PhotoImage(file="C:\\Users\\singham\\Downloads\\seven.png")
b5=Button(root,image=photo5,bd=0,width=60,height=35,command=lambda:btnClick('7'))
b5.grid(row=2,column=0,padx=2,pady=2)

photo6=PhotoImage(file="C:\\Users\\singham\\Downloads\\eight.png")
b6=Button(root,image=photo6,bd=0,width=60,height=35,command=lambda:btnClick('8'))
b6.grid(row=2,column=1,padx=2,pady=2)

photo7=PhotoImage(file="C:\\Users\\singham\\Downloads\\9.png")
b7=Button(root,image=photo7,bd=0,width=60,height=35,command=lambda:btnClick('9'))
b7.grid(row=2,column=2,padx=2,pady=2)

photo19=PhotoImage(file="C:\\Users\\singham\\Downloads\\divide.png")
b19=Button(root,image=photo19,bd=0,width=60,height=35,command=lambda:btnClick('/'))
b19.grid(row=2,column=3,padx=2,pady=2)






photo9=PhotoImage(file="C:\\Users\\singham\\Downloads\\four.png")
b9=Button(root,image=photo9,bd=0,width=60,height=35,command=lambda:btnClick('4'))
b9.grid(row=3,column=0,padx=2,pady=2)

photo10=PhotoImage(file="C:\\Users\\singham\\Downloads\\five.png")
b10=Button(root,image=photo10,bd=0,width=60,height=35,command=lambda:btnClick('5'))
b10.grid(row=3,column=1,padx=2,pady=2)

photo11=PhotoImage(file="C:\\Users\\singham\\Downloads\\six.png")
b11=Button(root,image=photo11,bd=0,width=60,height=35,command=lambda:btnClick('6'))
b11.grid(row=3,column=2,padx=2,pady=2)

photo12=PhotoImage(file="C:\\Users\\singham\\Downloads\\-.png")
b12=Button(root,image=photo12,bd=0,width=60,height=35,command=lambda:btnClick('-'))
b12.grid(row=3,column=3,padx=2,pady=2)




photo13=PhotoImage(file="C:\\Users\\singham\\Downloads\\one.png")
b13=Button(root,image=photo13,bd=0,width=60,height=35,command=lambda:btnClick('1'))
b13.grid(row=4,column=0,padx=4,pady=4)

photo14=PhotoImage(file="C:\\Users\\singham\\Downloads\\two.png")
b14=Button(root,image=photo14,bd=0,width=60,height=35,command=lambda:btnClick('2'))
b14.grid(row=4,column=1,padx=2,pady=2)

photo15=PhotoImage(file="C:\\Users\\singham\\Downloads\\three.png")
b15=Button(root,image=photo15,bd=0,width=60,height=35,command=lambda:btnClick('3'))
b15.grid(row=4,column=2,padx=2,pady=2)

photo16=PhotoImage(file="C:\\Users\\singham\\Downloads\\+.png")
b16=Button(root,text='+',image=photo16,bd=0,width=60,height=35,command=lambda:btnClick('+'))
b16.grid(row=4,column=3,padx=2,pady=2)




photo17=PhotoImage(file="C:\\Users\\singham\\Downloads\\dot.png")
b17=Button(root,image=photo17,bd=0,width=60,height=35,command=lambda:btnClick('.'))
b17.grid(row=5,column=0,padx=2,pady=2)

photo18=PhotoImage(file="C:\\Users\\singham\\Downloads\\zero.png")
b18=Button(root,image=photo18,bd=0,width=60,height=35,command=lambda:btnClick('0'))
b18.grid(row=5,column=1,padx=2,pady=2)



photo20=PhotoImage(file="C:\\Users\\singham\\Downloads\\equal.png")
b20=Button(root,image=photo20,bd=0,width=60,height=35,command=btnEquals)
b20.grid(row=5,column=2,padx=2,pady=2)


photo8=PhotoImage(file="C:\\Users\\singham\\Downloads\\X.png")
b8=Button(root,image=photo8,bd=0,width=60,height=35,command=lambda:btnClick('*'))
b8.grid(row=5,column=3,padx=2,pady=2)



mainloop()
