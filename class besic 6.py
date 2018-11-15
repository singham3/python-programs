#basic class program
class student:
    college="Matrix"
    def __init__(self,i):
        self.roll=int(input("Enter roll number of {} student: ".format(i+1)))
        self.name=input("Enter name of {} student: ".format(i+1))
    def Display (self):
        print("roll={} \tname={} ".format(self.roll,self.name))  

l=[]
n=int(input("Enter number of student: "))
for i in range(n):
    l.append(student(i))
for i in range(n):
    l[i].Display()


