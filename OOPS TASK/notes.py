# class 

"""
Class is an like an template blueprint of the anything.
Object is instance of a class
ORV is a declare a varibale of the object
"""
#EXAMPLE OF CLASS & OBJECT & ORV(object refernce variable)
class Employee:  #class
    def __init__(self,name,id):  #constructor
        self.name = name
        self.id = id
    def method1(self):  #method
        print("this is method")
        print(self.name)
#object refervce variable(ORV)
ORV = Employee("vamsi",101) #oject
ORV.method1()
print(ORV.id)



#Instance variable
"""
#values of the varible changing one object to anther object
< where we can delcre a variable>
1. inside the Construter we can declre a by using self
2.inside the method we can declre a by using self
3.outside a clas we can declare bby uing object reference varible

#where we can access the variable in instance method#
1.inside the Construter we can access a by using self
2.inside the method we can access a by using self
3.outside a clas we can access bby uing object reference varibe
"""
#EXAMPLE OF INSTANCE VARIABLE


# class Trip:
#     def __init__(self):
#         self.place = "Kerala"
#         print(self.place)
#     def m1(self):
#         self.location = "goa"
#         print(self.location)
# e = Trip()
# e.m1()
# e.budget = "10k"
# print(e.budget)



#static variable
#values of the varible can't cahnge one object to anther object
"""
@where we can declare
1.within the class directly
2.inside the constutor by using class name
3. inside the instanceemethod by uding the class name
4.inside the classmethd by using the cls&class name
5.inside the staticmethod by using the classname
6.outsude the class by using the classname
"""

#where we can acces by static variaable
"""
1.within the construtor by uusing the classname and slef
2.inside the classmethd by using the cls and claasname
3.inside the statice methd by usng the classname
4.ouside the class by using classname(ORV)
"""
#EXAMPLE OF STATIC VARIABLE
# class College:
#     college = "Santhiram"
#     def __init__(self):
#         College.name = "vamsi"
#         print(self.name)
#     def m1(self):
#         College.id = 101
#         print(College.id)
#     @classmethod
#     def m2(cls):
#         cls.semmarks = "7.8 CGPA"
#         College.totalper = "68.25 per"
#         print(cls.semmarks)
#         print(College.totalper)
#     @staticmethod
#     def m3():
#         College.year = "3 rd year"
#         print(College.year)
#     #local variable inside the fuction we can delcare and acces and
#     #outside the function we can't access the varible
#     def m4(self):
#         a = "subject"
#         print(a)

# e = College()
# e.m1()
# e.m2()
# e.m3()
# e.m4()
# print(College.college)
# College.place = "Nandyal"
# print(e.place)

# #Instance method
'''
1> inside the method if we are declaring (or) accesing instance variable 
2> While declaring instance we have to pass(self) as an argument
ex : def m1(self)
        self.name = "vamsi"
3> we can access instance method from outside of the class by using ORV
'''
#EXAMPLE FOR THE INSTANCE METHOD

# class Car:
#     def m1(self):
#         self.name ="vamsi"
#         self.id = 202
# e = Car()
# e.m1()
# print(e.name)
# print(e.id)


# #Class method
'''
1>inside the method if we are declare a some static variable 
2> we can declare a classmetho by @classmethod decorator
3> we can acces static variable using cls inside of the classmethod and 
using classname outside of theclass
4> we can acces classmethod outside using of class ORV and classname.
'''
# #EXAMPE FOR THE CLASS METHOD

# class Mobile:
#     Brand = "IQOO"
#     @classmethod
#     def m1(cls):
#         cls.model ="iqoo neo 6"
#         Mobile.bckcamera = "64 Mp"
# e = Mobile()
# e.m1()
# print(e.Brand)
# print(Mobile.model)
# print(e.bckcamera)

# #static method
"""
1> we can't use the instance and classmethod in static methd
2> we need to defined the @staticmethod while declaring
3> we can't mention the parament like(self,cls)
4> we can acces statice mtthod  by using classname and ORV
"""
# EXAMPLE OF THE STATIC METHOD
# class MObile :
#     @staticmethod
#     def m1():
#         MObile.name = "IQOO"
#         MObile.model= "noe 6"
#         # print(MObile.name)
#         # print(MObile.model)
# e = MObile()
# e.m1()
# print(e.name)
# print(MObile.model)


#inner class (or) nested class
"""
without having outer class there is no innerclass
"""
#EXAMPLE INNER CLASS
class Outer:
    def __init__(self):
        self.name = "vamsi"
        print("This is outer calss name ")
    def m1 (self):
        print(self.name)
    class inner:
        def __init__(self):
            self.id = 101
            print("This is inner class")
        def m2(self):
            print(self.id)
e = Outer()
e.m1()
c = e.inner()
c.m2()


#Inhertance
'''
1> Creating a new class from the existing class in such a way that all 
the features of the existing class are available to the newly crated 
class is inhertance
> there are 6 method
1.single inhertance
2.multilevel inhertance
3.multiple inhretance
4.herarical inhertance
5.hybird
6.cyclic
'''
#SINGLE INHERTANCE
'''
when you have a class that has basic characteristics and you 
need to create more classes that have all the basic characteristics
and some specific characteristics.

'''
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


#MULTILEVEL INHRETANCE
"""
In Python, multilevel inheritance refers to a situation where a class inherits from another 
class, and then a third class inherits from the second class,
 creating a chain of inheritance.
"""
#XAMPLE OF MULTILEVEL

class Animal:
    def __init__(self):
        self.name = "animals"
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
print(e.name)


#multple inhertnce
'''
A class can be derived from more than one superclass in Python.
For example, A class wolrd is derived from superclasses Aramy and farmer.
'''
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

#herarical inhertance
'''
where a single base class is inherited by multiple classes.
These derived classes, in turn, become base classes for other classes.
'''
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


#hybird inhretance
'''
combination of the both multiple and herarical is hybid
'''
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


#SUPER METHOD
'''
 super is a keyword that is used to refer to the immediate parent class of a class. 
 It is often used of inheritance to invoke methods or access attributes from the parent class.
'''