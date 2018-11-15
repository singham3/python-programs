from os import system, name
from time import sleep
import getpass

def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')
        
print("\t\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2")
print("\t\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2")
print("\t\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2    PANJAB NETIONAL BANK   \xB2\xB2\xB2\xB2\xB2\xB2\xB2")
print("\t\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2")
print("\t\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2")


while True:
    print("\n\n\n\n\n")
    username = input("\t\t\tenter your usename: ")
    password = getpass.getpass("\t\t\tHi {} , enter your password: ".format(username))
    if username=="singham" and password=="singham3":
        print("\t\t\twellcome {}".format(username))
        break
    else:
        print("\t\t\tyou entered wrong password ".format(username))
        try:
            input("\t\t\tPress enter to continue")
        except SyntaxError:
                pass

clear()
        
print("\n\n\n")
print("\t\t\t== == == == == == == == == == == == == == == == == ==")
print("\t\t\t== == == == == == == == == == == == == == == == == ==")
print("\t\t\t==                                                 ==")
print("\t\t\t==                                                 ==")
print("\t\t\t==                                                 ==")
print("\t\t\t==                                                 ==")
print("\t\t\t==                                                 ==")
print("\t\t\t==                                                 ==")
print("\t\t\t== ----------------------------------------------- ==")
print("\t\t\t== ----------------   WELLCOME   ----------------- ==")
print("\t\t\t== ----------------------------------------------- ==")
print("\t\t\t==                                                 ==")
print("\t\t\t==                                                 ==")
print("\t\t\t==                                                 ==")
print("\t\t\t==                                                 ==")
print("\t\t\t==                                                 ==")
print("\t\t\t==                                                 ==")
print("\t\t\t==                                                 ==")
print("\t\t\t== == == == == == == == == == == == == == == == == ==")
print("\t\t\t== == == == == == == == == == == == == == == == == ==")




try:
     input("\n\n\n\n\t\t\tPress Enter to continue...")
except SyntaxError:
    pass

clear()

    
    
def createAcc():
    
    
    name=input("enter account holder name: ")
    
    while True:
        marriage=input("{} enter your marital status(unmarried/married): ".format(name))
        sex=input("{} enter your sex(male/female/other): ".format(name))
        if sex=="male":
            sex="Mr."
            break
        elif sex=="female" and marriage=="unmarried":
            sex="Ms."
            break
        elif sex=="female" and marriage=="married":
            sex=="Mrs."
            break
        elif sex=="other":
            sex="Mx."
            break
        else:
            print("you entered wrong gender category ")
    print("hello {} {} welcome to Panjab Netional Bank".format(sex,name))  
    age=int(input("{} {} enter your age: ".format(sex,name)))
    citizenship=input("{} {} enter your citizenship: ".format(sex,name))
    print("{} {} enter your permanent Address: ".format(sex,name))
    plotnumber=input("\t\t{} {} enter your plot no./flat no./Bldg name:".format(sex,name))
    street=input("\t\t{} {} enter your stree/road & area/locality: ".format(sex,name))
    city=input("\t\t{} {} enter your city and district: ".format(sex,name))
    state=input("\t\t{} {} enter your state and country: ".format(sex,name))
    while True:
        pinCode=int(input("\t\t{} {}enter your pin code: ".format(sex,name)))
        if pinCode<=100000 and pincode>=999999:
            print("\t\t{} {}you have entered wrong pin code ")
        break
    while True:
        phonenumber=int(input("{} {} enter your phone number: ".format(sex,name)))
        if phonenumber<=100000000000 and phonenumber>=9999999999:
            print("{} {} you have entered wrong mobile number")
        break
    email=input("{} {} enter your Email id: ".format(sex,name))
    print("{} {} select any customer id proof".format(sex,name))
    print("\t\t1.aadhar card: ")
    print("\t\t2.voter id: ")
    print("\t\t3.driving Licence: ")
    print("\t\t4.Pen Card: ")
    while True:
        id=int(input("{} {}enter your id choice: ".format(sex,name)))
        if id==1:
            aadharCard=int(input("{} {} enter your Adhar card number: ".format(sex,name)))
            break
        elif id==2:
            voterId=input("{} {} enter your voter id number:".format(sex,name))
            break
        elif id==3:
            driving=input("{} {} enter your driving licence: ".format(sex,name))
            break
        elif id==4:
            penCard=input("{} {} enter your Pen Card number: ".format(sex,name))
            break
        else:
            print("you have entered wrong option")
    
    while True:
        depositAmount=float(input("{} {} enter amount you want to deposit $: ".format(sex,name)))
        if depositAmount<=0:
            print("{} {} you deposit amount is low".format(sex,name))
        break
    print("\n\n\n")
    print("---type of Account types---")
    print("select any choice of Account type")
    print("\n")
    print("\t\t\t 1. saving Account: ")
    print("\t\t\t 2. current Account: ")
    print("\t\t\t 3. Fixed deposit(for 1 year): ")
    print("\t\t\t 4. Fixed deposit(for 2 year): ")
    print("\t\t\t 5. Fixed deposit(for 3 year): ")
    print("\t\t\t 6. Fixed deposit(for 5 year): ")
    print("\n\n")
    while True:
        accchoice=int(input("\t\t\t Enter Your Account Choice: "))
        if accchoice==1 and  depositAmount>=1000:
            print("{} {} your Saving Account Has successfully created".format(sex,name))
            break
        elif accchoice==2 and depositAmount>=10000:
            print("{} {} your Current Account Has successfully created".format(sex,name))
            break
        elif accchoice==3 and depositAmount==1000:
            print("{} {} your Fixed Deposit Account Has successfully created  \n your monthly Deposit Amount is {} for 1 year".format(sex,name,depositAmount))
            break
        elif accchoice==4 and depositAmount==500:
            print("{} {} your Fixed Deposit Account Has successfully created  \n your monthly Deposit Amount is {} for 2 year".format(sex,name,depositAmount))
            break
        elif accchoice==5 and depositAmount==250:
            print("{} {} your Fixed Deposit Account Has successfully created  \n your monthly Deposit Amount is {} for 3 year".format(sex,name,depositAmount))
            break
        elif accchoice==6 and depositAmount==100:
            print("{} {} your Fixed Deposit Account Has successfully created  \n your monthly Deposit Amount is {} for 5 year".format(sex,name,depositAmount))
            break
    
        else:
            print("you have entered wrong choice")
    
    try:
        input("\n\n\n\n\t\t\tEnter 1 to go to the main menu and 0 to exit: ")
    except SyntaxError:
        pass

file=open("E:\\python programs\\program`s files\\banksystem.bin","wb")

print("\n\n\t\tCUSTOMER ACCOUNT BANKING MANAGEMENT SYSTEM")
print("\n\n\t\t\t▓▓▓▓▓▓▓ WELCOME TO THE MAIN MENU ▓▓▓▓▓▓▓")
print("\n\t\t1.Create new account")
print("\n\t\t2.Update information of existing account")
print("\n\t\t3.For transactions")
print("\n\t\t4.Check the details of existing account")
print("\n\t\t5.Removing existing account")
print("\n\t\t6.View customer's list")
print("\n\t\t7.Exit")

while True:
    optionChoice=int(input("\n\n\n\t\t\t\t\t\tEnter your Choice: "))
    if optionChoice==1:
        accnumber=3952001000100101
        first=createAcc()
        



sleep(1200)














