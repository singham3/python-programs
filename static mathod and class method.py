#wap to count the number of object created class
class method:
    t=0
    def __init__(self):
        print("constructor")
        self.a=10
    def i_method(self):
        print("instance method")

    @staticmethod
    def s_method():
        print("staticmathod ")
    @classmethod
    def c_method(self):
        print("class method")

method.s_method()
method.c_method()
m1=method()
m1.c_method()
