#wap to print for loop peturn

n=int(input("enter nmumbers of row: "))
k=0
for i in range(0,n+1):
    for j in range(0,(n-i)+1):
        print(end=" ")
    while k!=(2*i-1):
        print(k,end=" ")
        k=k+1
    print()
        
        

