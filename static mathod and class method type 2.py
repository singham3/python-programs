#wap to count the number of object created class
class method:
    def i_method(self,x):
        print(self,x)
    
    @staticmethod
    def s_method(x):
        print(x)
    @classmethod
    def c_method(cls,x):
        print(cls,x)
        
s_method=staticmethod()

c_method=classmethod(c_method)
obj=method()
obj,i_method(1)
method.i_method(obj,2)

obj.s_method(3)
method.s_method(4)

obj.c_method(5)
method.c_method(6)
