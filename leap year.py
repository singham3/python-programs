#wap to print year is leap year is not
n=int(input("enter a year: "))
if n%100==0:
        if n%400==0:
            print("leap year")
        else:
            print("not a leap year")
else:
    if n%4==0:
        print("leap year")
    else:
        print("not a leap year")
