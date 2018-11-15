#wap to count the number of object created class
class student:
    t=0
    def __init__(self):
        student.t=student.t+1
    def Display(self):
        t=student()
        student.staticmethod()

    @staticmethod
    def staticmethod():
        print("Total number of obbject: ",student.t)

    def __del__(self):
        student.t=student.t-1


s1=student()
s2=student()
student=staticmethod()
s3=student()
student=staticmethod()
s3.Display()
student.staticmethod()
