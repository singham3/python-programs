#wap to print year is leap year is not
n=int(input("enter a year: "))
if n%400==0 or n%100!=0 and n%4==0:
    print("leap year")
else:
    print("not a leap year")
