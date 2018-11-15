#wap to static mathod
class student:
    college="Matrix"
    def __init__(self,roll=0,name="rahul"):
        self.roll=roll
        self.name=name
    def Display(self):
        print("{} {}".format(self.roll,self.name))

    @staticmethod
    def staticmethod(t):
        print(student.college)
        print("{} {}".format(t.roll,t.name))


#student.staticmethod()
s=student(5,"rahul")
s.staticmethod(s)
s.Display()
