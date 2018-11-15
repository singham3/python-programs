#wap to count string charector
n=input("enter a string: ")
find=input("enter a charector who find: ")
c=0
for i in n[:]:
    if i==find:
        c=c+1
print(c)
