#wap to total of ditance in km and meter 
class Distance:
    def __init__(self):
        self.km=0
        self.m=0
    def Input(self):
        self.km=int(input("Enter km: "))
        self.m=int(input("enter meter: "))
    def Display(self):
        if self.m>=1000:
            self.km=self.km+self.m//1000
            self.m=self.m%1000
        print("km: {} \tm: {}".format(self.km,self.m))
    def Addition(self,d):
        t=Distance()
        t.km=self.km+d.km
        t.m=self.m+d.m
        return t

d1=Distance()
d2=Distance()
print("Enter first Distance: ")
d1.Input()
print("Enter second Distance: ")
d2.Input()
d1.Display()
d2.Display()
