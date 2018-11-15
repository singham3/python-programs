#basic class program
class student:
    college="Matrix"
    def __init__(self,r=-999,n="amit"):
        self.roll=r
        self.name=n

s1=student(1,'ravi')
s2=student(2,'sanju')
s3=student()
print(s1.roll,s1.name,s1.college)
print(s2.roll,s2.name,s2.college)
print(s3.roll,s3.name,student.college)
