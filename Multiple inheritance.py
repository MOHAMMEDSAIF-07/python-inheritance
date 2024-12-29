#muliple inheritance
class A1:    #1st parent class
    def fun1(self):
        print("class A1 function called")
class B1:    #2nd parent class
    def fun2(self):
        print("class B1 function called")
class C1(A1,B1):   #child class derived from 1st and 2nd parent class
    def fun3(self):
        print("class C1 function called")
c=C1()
c.fun1()
c.fun2()
c.fun3()


class A1:    #1st parent class
    def fun1(self,a,b):
        self.a=a
        self.b=b
class B1:    #2nd parent class
    def fun2(self):
        self.c=self.a+self.b
class C1(A1,B1):   #child class derived from 1st and 2nd parent class
    def fun3(self):
        print(self.c)
c=C1()
c.fun1(a=int(input("enter a value")),b=int(input("enter b value")))
c.fun2()
c.fun3()