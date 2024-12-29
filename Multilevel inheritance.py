#multilevel inheritence
class A:
    def myfunct1(self):
        print("class A function is called")
class B(A):
    def myfunct2(self):
        print("class B function is called")
class C(B):
    def myfunct3(self):
        print("class C function is called")
c1=C()
c1.myfunct1()
c1.myfunct2()
c1.myfunct3()

#multilevel inheritence
class A:
    def myfunct1(self,a,b):
        self.a=a
        self.b=b
class B(A):
    def myfunct2(self):
        self.c=self.a+self.b
class C(B):
    def myfunct3(self):
        self.myfunct2()
        print("addition of given numbers",self.c)
c1=C()
c1.myfunct1(a=int(input("enter a value")),b=int(input("enter b value")))
c1.myfunct3()

class Animal:
    def __init__(self,name):
        self.name=name
class Mammal(Animal):
    def walk(self):
        return f"{self.name} is started walking"
class Dog(Mammal):
    def bark(self):
        return f"{self.name} is started barking"
mydog=Dog("bob")
print(mydog.walk())
print(mydog.bark())