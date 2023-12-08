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
1.inside the Construter we can declre a by using self
2.inside the method we can declre a by using self
3.outside a clas we can declare bby uing object reference varible

#where we can access the variable in instance method#
1.inside the Construter we can access a by using self
2.inside the method we can access a by using self
3.outside a clas we can access bby uing object reference varibe
"""
#EXAMPLE OF INSTANCE VARIABLE


class Trip:
    def __init__(self):
        self.place = "Kerala"
        print(self.place)
    def m1(self):
        self.location = "goa"
        print(self.location)
e = Trip()
e.m1()
e.budget = "10k"
print(e.budget)



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
class College:
    college = "Santhiram"
    def __init__(self):
        College.name = "vamsi"
        print(self.name)
    def m1(self):
        College.id = 101
        print(College.id)
    @classmethod
    def m2(cls):
        cls.semmarks = "7.8 CGPA"
        College.totalper = "68.25 per"
        print(cls.semmarks)
        print(College.totalper)
    @staticmethod
    def m3():
        College.year = "3 rd year"
        print(College.year)
    #local variable inside the fuction we can delcare and acces and
    #outside the function we can't access the varible
    def m4(self):
        a = "subject"
        print(a)

e = College()
e.m1()
e.m2()
e.m3()
e.m4()
print(College.college)
College.place = "Nandyal"
print(e.place)

# #Instance method
'''
1> inside the method if we are declaring (or) accesing instance variable 
2> While declaring instance we have to pass(self) as an argument
ex : def m1(self)
        self.name = "vamsi"
3> we can access instance method from outside of the class by using ORV
'''
#EXAMPLE FOR THE INSTANCE METHOD

class bike:
    def m1(self):
        self.name = "NS160"
        self.rpice = "1lak"
e = bike()
e.m1()
print(e.name)
print(e.rpice)



# #Class method
'''
1>inside the method if we are declare a some static variable. 
2> we can declare a classmetho by @classmethod decorator
3> we can acces static variable using cls inside of the classmethod and 
using classname outside of theclass
4> we can acces classmethod outside using of class ORV and classname.
'''
# #EXAMPE FOR THE CLASS METHOD
class Mobile:
    Brand = "IQOO"
    @classmethod
    def m1(cls):
        cls.model ="iqoo neo 6"
        Mobile.bckcamera = "64 Mp"
e = Mobile()
e.m1()
print(e.Brand)
print(Mobile.model)
print(e.bckcamera)

# #static method
"""
1> we can't use the instance and classmethod in static methd
2> we need to defined the @staticmethod while declaring
3> we can't mention the parament like(self,cls)
4> we can acces statice mtthod  by using classname and ORV
"""
# EXAMPLE OF THE STATIC METHOD
class MObile :
    @staticmethod
    def m1():
        MObile.name = "IQOO"
        MObile.model= "noe 6"
        # print(MObile.name)
        # print(MObile.model)
e = MObile()
e.m1()
print(e.name)
print(MObile.model)


#inner class (or) nested class
"""
without having outer class there is no innerclass
"""
#EXAMPLE INNER CLASS
class Bike:
    def __init__(self):
        self.name = "vamsi"
        print("This is outer calss name ")
    def m1 (self):
        print(self.name)
    class Car:
        def __init__(self):
            self.id = 101
            print("This is inner class")
        def m2(self):
            print(self.id)
e = Bike()
e.m1()
C = Bike.Car()
C.m2()


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
class Gp:
    def __init__(self):
        self.name ="Das"
    def m1(self):
        print(self.name)
class p(Gp):
    def m2(self):
        print("This is parent class")
e = p()
e.m1()
e.m2()
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
        print(self.name)
    def m1(self):                                                  #a class from to B               
        print("this is main class animal")                          # b class to C                                                                  # 
class Rat(Animal):                                                   # C to d
    def m2(self):
        print("rat eat's food")
class cat(Rat):
    def m3(self):
        print("cat's eats rat's")
e = cat()
e.m1()
e.m2()
e.m3()



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
'''
>it is a inbuilt method superclass
>we can call parentclass constructor ,instance,and all variables in chlid class
'''
#EXAMPLE OF SUPERCLASS
class Parent:
    def __init__(self,name,id):
        self.name = name 
        self.id = id
    def m1(self):
        print("name :",self.name)
        print("id :",self.id)
class child(Parent):
    def __init__(self, name, id,villid,ide,phonenum):
        super().__init__(name, ide)
        self.villid= villid
        self.id = id
        self.phonenum = phonenum
    def m2(self):
        super().m1()
        print("villid :",self.villid)
        print("id :",self.id)
        print("Phone :",self.phonenum)
a = child("ram",23,"hyd",101,123456789)
a.m2()


'''
>some methods we can use in super
#>we are allow to acces parent class instance variable  to child class ,
to acces must and should we use self .
#>we can acces parent class static variables
'''
#EXAMPLE OF THE FIRST METHOD
class employee:
    name = "marolix"
    def __init__(self):
        self.id = 101
class staf(employee):
    def m1(self):
        print(super().name)
        print(self.id)
e = staf()
e.m1()

'''
#from child class instance method and constructer 
# we can acces all methods they are instanec, class,static
'''
class P :
    def __init__(self):
        print("this is parentclass constructer") 
    def m1(self):
        print("this is parentclass instancemethod")
    @classmethod    
    def m2(cls):
        print("this is parentclass classmethod")
    @staticmethod   
    def m3():
        print("this is parentclass staticmethod")

class C(P):
    def __init__(self):
       super().__init__()
       super().m1()
       super().m2()
       super().m3()
    def m1(self):
       super().__init__()
       super().m1()
       super().m2()
       super().m3() 
C=C()
C.m1()


'''
we cannote accese parent class instance method and constructer from
child class classmethod.
'''
class P :
    def __init__(self):
        print("this is parentclass constructer") 
    def m1(self):
        print("this is parentclass instancemethod")
    @classmethod    
    def m2(cls):
        print("this is parentclass classmethod")
    @staticmethod   
    def m3():
        print("this is parentclass staticmethod")

class C(P):
    @classmethod
    def m4(cls):
       #super().__init__()   invalid
       #super().m1()   invaid instead of we usinng the down method
       super(C,cls).__init__(cls)
       super(C,cls).m1(cls)
       super().m2()
       super().m3()
c=C()
c.m4()


'''
#in child class staticmethod we are not allowed to use super() 
#>we can call parent class staticmethodss into the childclass static method
'''
class P :
    def __init__(self):
        print("this is parentclass constructer") 
    def m1(self):
        print("this is parentclass instancemethod")
    @classmethod    
    def m2(cls):
        print("this is parentclass classmethod")
    @staticmethod   
    def m3():
        print("this is parentclass staticmethod")
class C(P):
    @staticmethod 
    def m4():
       #super().__init__()  invalid
       #super().m1()  invalid
       #super().m2() invalid
       #super().m3()  invalid
       super(C,C.m3())
c=C()
c.m4()

#Polymorshipm
'''
>polymorphism is frequently used in class methods,
where we can use multiple class with same method name 
>one object can be display more than one function EX method as same is from many object
'''
class School:
    def m1(self):
        print("this is a school")
class Teacher:
    def m1(self):
        print("This is a Tecaher")
class Student:
    def m1(self):
        print("This is a student")
# a = School()
# b = Teacher()
# c = Student()
for d in(School(),Teacher(),Student()):
    d.m1()


#OVERLOADING
'''
>> means we can use same operater or method for different functionaliteis 
1.operater overloading 
2.method overloading 
3.constructer overloading 
'''

#OPERATOR OVERLOADING
'''
>we can use same operater for multiple perposes  ex = +
>for every operater we have magic method, whenever we 
are using operater overloading we have to use magic methods 
'''
class student:
    def __init__(self,maths):
        self.maths = maths
    def __mul__(self,internlmarks):
        return self.maths * internlmarks.maths
s1 = student(35)
s2 = student(20)
print(s1 * s2)



class Employee:
    def __init__(self,name):
        self.name = name
    def __sub__(self,city):
        return self.name - city.name
s = Employee(10)
s1 = Employee(20)

print(s-s1)


#METHOD OVERLOADING
'''
>if two methods have same name but defferent arguments.
'''
class ADD:
    def add(a,b):
        print(a+b)
    def add(a,b,c):
        print(a+b+c)
    add(10,20,90)
    add(10,20)   #invalid
a = ADD()

#CONSTRUCOTR OVERLOADING
'''
not used in python
'''
class P:
    def __init__(self):
        self.name = "vamsi"
        print(self.name)
    def __init__(self) :
        self.id = 101
        print(self.id)
    def __init__(self):
        self.city = "hyd"
        print(self.city)
a = P()


#OVERRIDING
'''
> we can use overriding the pranet class constructor method into the child class method override the method
'''
#EXAMPLE OF OVERRIDING
class Company:
    def __init__(self):
        self.name = 'vamsi'
        print(self.name)
    def display(self):
        self.id = '1038*(&)'
        print("id :",self.id)
class Employee(Company):
    def __init__(self):
        self.salary='25k'
        print(self.salary) 
    def display(self):
        self.id = 101
        print("id :",self.id)
c = Employee()
c.display()

#ABSTRACT METHOD
'''
hiding unnesscary data 
'''
#abstract class 
'''
>a class that having more then one abstract method  
'''

from abc import ABC
class add(ABC):
    def m1(self):
        pass
a = add()


#abstract method
''''
> we are declaring a method but not implementing, such type of method is abstract method
> we have to mention @abstractmethod 

'''
from abc import ABC,abstractmethod
class test(ABC):
    @abstractmethod
    def m1(self):
        pass

t = test()    #we are not allow to create object for abstractclass
t.m1()




#abtsrct base class 
'''
>every abstract class is derived from the these base class only 
>python is providing abc module,from here we can import ABC class
'''
from abc import ABC,abstractmethod
class add(ABC):
    @abstractmethod
    def m1(self):
        pass
    print("HIS is a bat")
class sum(add):
    def m1(slef):
        print("HIS is aball")
e = sum()
e.m1()

# Python program to 
# demonstrate private members 

# Creating a Base class 

#ENCAPSULATION
"""
It essentially means binding variables and methods together into a single unit
 and preventing them from being accessed by other classes.""" 

#EXAMLE OF A encapsulation

class Employee:
    def __init__(self,name,id,salary):
        self.name = name
        self.id= id
        self.salary = salary
    def m1(self):
        print(self.name,'is in traning',self.id)

    def m2(self):
        print(self.name,'is in traning',self.salary)

a = Employee('ram',102,'25 k')
a.m1()
a.m2()

#WE HAVE SOME METHODS IN ENCAPSULATION MEMBERS
'''
1>Public Member: Accessible anywhere from otside oclass.
2>Private Member: Accessible within the class
3>Protected Member: Accessible within the class and its sub-classes
'''

#PUBLIC MEMBER 
'''
we can access anywhere from the class inside(SELF) or outside(by using oRV)
'''
#EXAMPLE
class Police:
    def __init__(self,name,position,duty_area):
        self.name = name
        self.position = position
        self.duty_area= duty_area
    def method(self):
        print(self.name,' is a',self.position,'police')
e = Police('KRISHNA','DSP',"HYD")
e.method()
print(e.position,'oof the',e.duty_area)

#PRIVATE
'''
ACESS within the class only by uing self
To define a pravite varible name by using only the one or to underscore
'''
#EXAMPLE OF PRAVITE
class Student:
    def __init__(self,name,branch,id):
        self.name = name
        self.__branch = branch
        self.__id = id                   # PRIAVTE METHOD
    def show(self):
        print(self.name,self.__branch,self.__id)
a = Student("RAM","ECE",102)
a.show()
# print(a.name,a.__branch,a.__id)         INVALID

#PROTECTED MEMBER
'''
1> we can acces inside th classs and in the subclass also we can acces
we will use only one underscore(_)
'''
# base class
class Student:
    def __init__(self):
        self._name = 'vamsi'
class College(Student):
    def __init__(self, collegename):
        self.collegename = collegename
        Student.__init__(self)
    def m1(self):
        print('student name :',self._name)
        print('college name :',self.collegename)
a = College('santhiram')
a.m1()
print(a.collegename)
#there are another function are there getter and setter metod
#GETTER
#SETTER
#GETTER
'''
we can get the dat from the class
'''
#EXAAAMPLE OF GETTER
class Student:
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    def getter_show(self):
        return self.name
a = Student('vamsi',23)
a.getter_show()
print('name :',a.name,a.age)

#SETTER
'''
we can change the date from the paranet class
'''
#EXAMPLE OF SETTER

class Student:
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    def getter_show(self):
        return self.name
    
    def setter_sho(self,age):
        self.age= age
        print('setter age :',self.age)
a = Student('vamsi',23)
a.getter_show()
print('name :',a.name)
print('getter age :',a.age)
a.setter_sho(30)




#EXCEPATATION HANDLING
try:
    print(10/2)
    print(10/2)
    print(20/2)
except:
    print(20-90)
    print(10+20)
    print(3-3)
    print(5-9)


try:
    print(10/2)
    print(10/0)
    print(20/2)
except:
    print(20-90)
    print(10+20)
finally:
    print(3-3)
    print(5-9)

try:
    print(10/2)
    try:
        print(10/0)
    except:
        print(399-94454)
except:
    print(20-90)
finally:
    print(787+9453)