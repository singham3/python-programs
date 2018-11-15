#wap to print prime number under 1000
for i in range(1,1000+1):
    if i%i//2==0:
        print("not a prime number")
        break
    else:
        print("prime number")
