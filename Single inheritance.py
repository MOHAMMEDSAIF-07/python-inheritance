#single inheritance
class parentclass: #parent class
    def myfunction1(self): #parent class property
        print("parent class function called")
class childclass(parentclass): #child class
    def myfunction2(self):
        print("child class called")
c1=childclass()
c1.myfunction1()
c1.myfunction2()

#single inheritance
class parentclass: #parent class
    def myfun1(self): #parent class property
        self.a=54
        self.b=45
class childclass(parentclass): #child class
    def myfun2(self):
        c=self.a+self.b
        print(f"addition of a and b is",c)
c1=childclass()
c1.myfun1()
c1.myfun2()

#single inheritance
class parentclass: #parent class
    def myfun11(self): #parent class property
        self.a=a=int(input("enter a value"))
        self.b=b=int(input("enter b value"))
class childclass(parentclass): #child class
    def myfun22(self):
        c=self.a+self.b
        print(f"addition of a and b is",c)
c1=childclass()
c1.myfun11()
c1.myfun22()

#parent class
class vehicle:
    def __init__(self,brand):
        self.brand=brand
#child class
class car(vehicle):
    def drive(self):
        return f"the {self.brand} car is best car...."
mycar1=car("BMW")
mycar2=car("toyota supra")
print(mycar1.drive())
print(mycar2.drive())