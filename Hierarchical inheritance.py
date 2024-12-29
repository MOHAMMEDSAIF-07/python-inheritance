# hierachical inheritance one parent class multiple child classes
class A1: #parent class
    def myfunc1(self):
        print("Class A1 function is called")
class A2(A1): #child class
    def myfunc2(self):
        print("Class A2 function is called")
class A3(A1): #child class
    def myfunc3(self):
        print("Class A3 function is called")
a2=A2()
a3=A3()
a2.myfunc1()
a2.myfunc2()
a3.myfunc3()

#Addition , Subraction , Multiplication of two no using hierachical inheritance
class A:
    def myfunc(self,a,b):
        self.a=a
        self.b=b
class A1(A):
    def myfunc1(self):
        print("Addition of a & b :- ",self.a+self.b)
class A2(A):
    def myfunc2(self):
        print("Subraction of a & b :- ",self.a-self.b)
class A3(A):
    def myfunc3(self):
        print("Multiplication of a & b :- ",self.a*self.b)
a1=A1()
a2=A2()
a3=A3()
a1.myfunc(a=int(input("enter a value")),b=int(input("enter b value")))
a1.myfunc1()
a2.myfunc(a=int(input("enter a value")),b=int(input("enter b value")))
a2.myfunc2()
a3.myfunc(a=int(input("enter a value")),b=int(input("enter b value")))
a3.myfunc3()