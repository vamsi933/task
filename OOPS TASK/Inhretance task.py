#EXample of single 
class parent:
    def __init__(self):
        self.name = "vamsi"
        print(self.name)
    def m1(self):
        print("parent inhretance")
class child(parent):
    def m2(self):
        print("child class")
e = child()
e.m1()
e.m2()

#XAMPLE OF MULTILEVEL

class Animal:
    def __init__(self):
        self.name = "animals"
        print(self.name)
    def m1(self):                                                  #a class from to B               
        print("this is main class animal")                          # b class to c                                                                  # 
class Rat(Animal):                                                   # c to d
    def m2(self):
        print("rat eat's food")
class cat(Rat):
    def m3(self):
        print("cat's eats rat's")
e = cat()
e.m1()
e.m2()
e.m3()


#EXAMPLE MULTIPLE
class Aramy:
    def __init__(self):
        self.name = "miltray"
        print(self.name)                                    # class one and class 2 we can use athe end class
    def m1(self):
        print("This is a base class of aramy")
class Farmer:
    def m2(self):
        self.name = "king"
        print(self.name)
        print("this is sub class of farmer")
class World(Aramy,Farmer):
    def m3(self):
        print("this is multiple of all class")
e = World()
e.m1()
e.m2()
e.m3()


#EXAMPLE OF HERARICAL
class Doctor:
    def __init__(self):
        self.name = "doctor"
        print(self.name)
    def m1(self):
        print("This is a main Doctor class")
class Dentist(Doctor):
    def m2(self):
        print("this is a dentist class")
class Hematoloists(Doctor):                                     # in herarical we need to creaata orv based on the classes
    def m3 (self):
        print("this is a hematolists")
e = Hematoloists()
e.m1()
e.m3()
a = Dentist()
a.m2()
a.m1()


#EXMPLE OF HYBIRD
class Tittle:
    def __init__(self):
        self.Moviename = "KGF"
    def m1(self):
        print("This is a movie tittle :",self.Moviename)
class Director(Tittle):
    def __init__(self):
        self.Dirctorname = "Prashanth Neil"
        super().__init__()
    def m2(self):
        print("This is a diector name :", self.Dirctorname)
class Actor(Tittle):
    def __init__(self):
        self.Heroname = "YASH"
        super().__init__()
    def m3(self):
        print("This is a diector name :",self.Heroname)
class Movie(Director,Actor):
    def __init__(self):
        super().__init__()
    def m4(self):
        print("This is the information about movie ")
a = Movie()
a.m1()
a.m2()
a.m3()
a.m4()

