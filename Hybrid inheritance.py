#hybrid inheritance
class B1: #parent class
    def func1(self):
        print("Function of class B1 is calling...")
class B2(B1): 
    def func2(self):
        print("Function of class B2 is calling...")
class B3(B1): 
    def func3(self):
        print("Function of class B3 is calling...")
class B4(B2,B3): 
    def func4(self):
        print("Function of class B4 is calling...")
b=B4()
b.func1()
b.func2()
b.func3()
b.func4()