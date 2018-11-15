# wap to wrep text
def wrap (string,max_width):
    l=''
    for i in range(0,len(string),max_width):
        l=l+string[0+i:max_width+i]+'\n'
    return l
s='abcdefghijklmnopqrstuvwxz'
max_width=int(input("enter width of string: "))
t=wrap(s,max_width)
print(t)
