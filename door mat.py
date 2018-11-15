#wap to digine door mat
n,m = map(int,input("enter two number: ").split())
for i in range(1,n//2+1):
    print(('.|.'*(2*i-1).center(m,'-'))

print("WELCOME".center(m,'-'))

for i in reversed(range(1,n//2+1)):
    print(('.|.'*(2*i-1)).center(m,'-'))
