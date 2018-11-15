from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import scrolledtext


root=Tk()
root.title('Bank Of Baroda')
root.iconbitmap('E:\\python programs\\python images\\cat.ico')
root.geometry('800x700')
conn=pymysql.connect(user="root",password="root@1234",host="127.0.0.1",database="bob")
cur=conn.cursor()

def loginPage():
    def removeValue(event):
        ent.delete(0, 'end')
        return None
    def REmoveValue(event):
        ent2.delete(0, 'end')
        return None
    def Login():
        def deshboard():
            global db1
            global db2
            global db3
            global db4
            global db5
            global db6
            image12=PhotoImage(file='E:\\python programs\\python images\\dashboard1.png')
            db1=Label(d,bd=0,compound=CENTER,width=315,height=240,image=image12,text='About us:\nIt has been a long and eventful journey of almost \na century across 25 countries.Starting in 1908 \nfrom a small building in Baroda to its new hi-rise and \nhi-tech Baroda Corporate Centre in Mumbai, is a saga of \nvision,enterprise,financial prudence \nand corporate governance.')
            db1.image=image12
            db1.place(x=1030,y=20)
            db2=Label(d,bd=0,width=315,height=240,image=image12,compound=CENTER,text='HISTORY:\nThe bank was founded by the Maharaja of Baroda,\nMaharaja Sayajirao Gaekwad III on 20 July 1908. \nThe bank, along with 13 other major commercial banks of \nIndia,was nationalised on 19 July 1969, by the Government \nof India and has been designated as a profit-making \npublic sector undertaking (PSU).')
            db2.image=image12
            db2.place(x=1030,y=273)
            image13=PhotoImage(file='E:\\python programs\\python images\\dashboard2.png')
            db3=Label(d,bd=0,width=530,height=210,image=image13,compound=CENTER,text='Carefully crafted career path policy \nThe career path policy in the bank ensures a rich variety of exposures\n in areas like operations, credit, forex, and administration/facilitation \nfor all officers joining the bank. It ensures that over time, all officers \nare wholesome, holistic bankers. The policy also ensures a \ngrowth track for all employees in the bank.')
            db3.image=image13
            db3.place(x=815,y=525)
            image14=PhotoImage(file='E:\\python programs\\python images\\dashboard3.png')
            db4=Label(d,bd=0,width=460,height=493,image=image14,compound=CENTER,text='Things to Remember when Opening and Maintaining a Savings Account with Bank of Baroda\nOne should check the interest rate over deposits for that particular savings account.\n\tThe interest rate will determine your return over the deposits and\n knowing this before choosing a savings account is important.\n\tChecking the minimum balance requirement of the savings account and \nassessing if it suits their finances is necessary.\n\tOne should check the penalty fees for not maintaining the minimum balance.\n\tCustomers should check the transaction and withdrawal limit per day for that \nparticular account.The applicant should check if there are extra charges if \none withdrawals cash using cheques and the withdrawal limit per \nmonth at ATMs other than Bank of Baroda.\n\tIf in case a transaction has been without your knowledge, \none should contact the bank immediately.\n\tOnce the account is opened, you should ensure that your account password \nand PIN is never shared through emails, SMS, or on social media.\n\tEnsure that you check your bank statements regularly to keep a check \nif there are any cases of fraudulent activity and to keep a track of \nyour finances - in and out of your account.\n\tIf your debit card is either lost or stolen, you should either \nblock it through your net banking account immediately or \ncall the customer care of Bank of Baroda to do it for you.\n\tAvoid saving your bank account details on online merchant websites.\n\tEnsure that you close the page as soon as you have completed a transaction \nonline and that you only shop on websites that are secure.')
            db4.image=image14
            db4.place(x=550,y=20)
            image15=PhotoImage(file='E:\\python programs\\python images\\dashboard5.png')
            db5=Label(d,bd=0,width=630,height=210,image=image15,compound=CENTER,text='Bank of Baroda Customer Care Number \nFor customers that need help, have doubts, grievances or complaints \nregarding savings accounts, they can contact the Bank of Baroda \ncustomer care number - 1800 22 33 44 / 1800 102 4455.')
            db5.image=image15
            db5.place(x=165,y=525)
            image16=PhotoImage(file='E:\\python programs\\python images\\dashboard4.png')
            db6=Label(d,bd=0,width=365,height=493,image=image16,compound=CENTER,text='ATM Network \nThe Bank has large network of ATMs in India. ATM/ Branch Locator \nThe Bank’s plans are to extend this network in stages in future.\nThe Bank also plans to deploy low cost ATMs at Rural centers.\nBank has launched School fees collection module which enables payment of School\n fees through Bank’s ATM.\n\nInternet Payment Gateway\n3D secure implementation has been completed under Internet Payment Gateway. \nIPG facilitates direct customer merchant transactions and \nsettlement through the Bank’s Central ATM Switch.')
            db6.image=image16
            db6.place(x=165,y=20)
        def terdesh():
                db1.destroy()
                db2.destroy()
                db3.destroy()
                db4.destroy()
                db5.destroy()
                db6.destroy()
        def createAccount():
            terdesh()
            
            ca_t=d.create_text((500,30),text='Create A New Account',fill='white',font=('arial',40,'bold'))
            image17=PhotoImage(file='E:\\python programs\\python images\\label.png')
            ca_l=Label(d,image=image17,bd=0,height=20,width=300,text='Personal Details',compound=RIGHT)
            ca_l.image=image17
            ca_l.place(x=180,y=80)
            ca_t1=d.create_text((282,130),text='First Name :',fill='white',font=('arial',13,'bold'))
            ca_e1=Entry(d,bd=0)
            ca_e1.place(x=340,y=120)
            ca_t2=d.create_text((284,170),text='Last Name :',fill='white',font=('arial',13,'bold'))
            ca_e2=Entry(d,bd=0)
            ca_e2.place(x=340,y=160)
            ca_t3=d.create_text((275,210),text='Gender :',fill='white',font=('arial',13,'bold'))
            ca_r3=Radiobutton(d,bd=0,text='Male',value=1)
            ca_r3.place(x=340,y=200)
            ca_r3_2=Radiobutton(d,bd=0,text='Female',value=2)
            ca_r3_2.place(x=440,y=200)
            ca_t3=d.create_text((275,230),text='Date of Birth :',fill='white',font=('arial',13,'bold'))
            cal=DateEntry(d,dateformat=3,width=12, background='darkblue',foreground='white', borderwidth=4,Calendar =2018)
            cal.place(x=340,y=230)
            ca_t4=d.create_text((280,250),text='Citizenship :',fill='white',font=('arial',13,'bold'))
            ca_e4=Entry(d,bd=0)
            ca_e4.place(x=340,y=240)
            ca_t5=d.create_text((308,290),text='Age :',fill='white',font=('arial',13,'bold'))
            ca_e5=Entry(d,bd=0)
            ca_e5.place(x=340,y=280)
            ca_t6=d.create_text((250,330),text='TelePhone Number :',fill='white',font=('arial',13,'bold'))
            ca_e6=Entry(d,bd=0)
            ca_e6.place(x=340,y=320)
            ca_t7=d.create_text((255,370),text='Deposit Ammount :',fill='white',font=('arial',13,'bold'))
            ca_e7=Entry(d,bd=0)
            ca_e7.place(x=340,y=360)
            
        f.destroy()
        image4=PhotoImage(file='E:\\python programs\\python images\\blur2.png')
        d=Canvas(root)
        d.pack(expand=True, fill=BOTH)
        d.img=image4
        d.create_image(0, 0, anchor=NW, image=image4)
        image5=PhotoImage(file='E:\\python programs\\python images\\fr.png')
        fr=Label(d,width=150,height=1234,image=image5,bd=0)
        fr.image=image5
        fr.place(x=0,y=0)
        deshboard()
        image6=PhotoImage(file='E:\\python programs\\python images\\button2.png')
        b_fr=Button(fr,bd=0,width=148,height=50,image=image6,command=createAccount)
        b_fr.image=image6
        b_fr.place(x=0,y=50)
        image7=PhotoImage(file='E:\\python programs\\python images\\button3.png')
        b_fr1=Button(fr,bd=0,width=148,height=50,image=image7)
        b_fr1.image=image7
        b_fr1.place(x=0,y=100)
        image8=PhotoImage(file='E:\\python programs\\python images\\button4.png')
        b_fr2=Button(fr,bd=0,width=148,height=50,image=image8)
        b_fr2.image=image8
        b_fr2.place(x=0,y=150)
        image9=PhotoImage(file='E:\\python programs\\python images\\button5.png')
        b_fr3=Button(fr,bd=0,width=148,height=50,image=image9)
        b_fr3.image=image9
        b_fr3.place(x=0,y=200)
        image10=PhotoImage(file='E:\\python programs\\python images\\button6.png')
        b_fr4=Button(fr,bd=0,width=148,height=50,image=image10)
        b_fr4.image=image10
        b_fr4.place(x=0,y=250)
        image11=PhotoImage(file='E:\\python programs\\python images\\button7.png')
        b_fr5=Button(fr,bd=0,width=148,height=50,image=image11)
        b_fr5.image=image11
        b_fr5.place(x=0,y=300)
        
    def signup():
        
        def conpass():
            getuser=user_name_.get()
            getname=Name_.get()
            Getpass2=conform_password_.get()
            Getpass=_password_.get()
            if Getpass!=Getpass2:
                messagebox.showerror('ERROR','Password not Matched')
            else:
                
                c.destroy()
                loginPage()
        def REmoveValue(event):
            conform_password_.delete(0, 'end')
            return None
        f.destroy()
        image=PhotoImage(file='E:\\python programs\\python images\\blur2.png')
        c=Canvas(root)
        c.pack(expand=True, fill=BOTH)
        c.img=image
        c.create_image(0, 0, anchor=NW, image=image)
        image3=PhotoImage(file='E:\\python programs\\python images\\CNA.png')
        l2=Label(c,image=image3,bd=0)
        l2.image=image3
        l2.place(x=170,y=130)
        user_name=c.create_text((281,300),text='User Name:',fill='white',font=('arial',13,'bold'))
        user_name_=Entry(c,bd=0,font=('arial',10,'bold'),width=30)
        user_name_.place(x=350,y=290)

        name=c.create_text((302,350),text='Name:',fill='white',font=('arial',13,'bold'))
        Name_=Entry(c,bd=0,font=('arial',10,'bold'),width=30)
        Name_.place(x=350,y=340)
        
        password_=c.create_text((285,400),text='Password:',fill='white',font=('arial',13,'bold'))
        _password_=Entry(c,bd=0,show='*',font=('arial',10,'bold'),width=30)
        _password_.place(x=350,y=390)
        
        
        conform_password_=c.create_text((248,450),text='Conform Password:',fill='white',font=('arial',13,'bold'))
        conform_password_=Entry(c,bd=0,show='*',font=('arial',10,'bold'),width=30)
        conform_password_.bind("<Button-1>", REmoveValue)
        conform_password_.place(x=350,y=440)
        
        
        b2=b=Button(c,height=2,bd=0,fg='white',bg='#6462E3',text='Create Account',font=('arial',10,'bold'),command=conpass)
        b2.place(x=455,y=500)
        
        
        
    #================================================================================================================================================= 
    
        
    image1=PhotoImage(file='E:\\python programs\\python images\\blur2.png')
    f=Canvas(root)
    f.pack(expand=True, fill=BOTH)
    f.img=image1
    f.create_image(0, 0, anchor=NW, image=image1)
    
        
    image2=PhotoImage(file='E:\\python programs\\python images\\profile3.png')
    l=Label(f,image=image2,bd=0)
    l.image=image2
    l.place(x=390,y=130)

    entl=f.create_text((280,300),text='UserName:',fill='white',font=('arial',13,'bold'))

    
    ent=Entry(f,bd=0,font=('arial',10,'bold'),width=30)
    
    ent.bind("<Button-1>", removeValue)
    ent.place(x=350,y=290)


    entleabel=f.create_text((280,330),text='Password:',fill='white',font=('arial',13,'bold'))
    
    ent2=Entry(f,bd=0,show='.',font=('arial',10,'bold'),width=30)
    
    ent2.bind("<Button-1>", REmoveValue)
    ent2.place(x=350,y=320)
    

    b=Button(f,width=12,height=2,bd=0,fg='white',bg='#6462E3',text='Log In',font=('arial',10,'bold'),command=Login)
    b.place(x=350,y=360)


    b2=b=Button(f,width=12,height=2,bd=0,fg='white',bg='#6462E3',text='Sign Up',font=('arial',10,'bold'),command=signup)
    b2.place(x=455,y=360)
    

    
loginPage()
root.mainloop()
