#basic class program
class student:
    college="Matrix"
    def __init__(self,r=-999,n="amit"):
        self.roll=r
        self.name=n
    def Display (self):
        print(self.roll,self.name,self.college)

s1=student(1,'ravi')
s2=student(2,'sanju')
s3=student()
#s1.Display()
student.Display(s1)
s2.Display()
s3.Display()

