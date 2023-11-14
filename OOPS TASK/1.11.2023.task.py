
#creating a oops by using instance method & static & local vrilable 


class Employee:
    company = "Marolix"
    def __init__(self,name):
        self.name = name
        Employee.Domain = "PYTHON"
        print(f"Inside the construter instancemethod by using self by  : {self.name}")
        print(f"Within the construter staticmethod by using class name : {self.Domain}")
    def method1(self):
        self.id = "MT-02023"
        Employee.mailid = "@gmail.code"
        print(f"inside the instnce mthod using claasname : {Employee.mailid}")
        print(f"Inside the method instance by using self : {self.id}")
    @classmethod
    def method2(cls):
        Employee.salary = "40000 salary"
        cls.exprenices = "1.5 years"
        print(f"inside the clssmthod static   classname : {Employee.salary}")
        print(f"inside the classmethod static using ORV : {cls.exprenices}")
    @staticmethod
    def method3():
        Employee.city = "HYD"
        print(f"INside the static method is classname   :  {Employee.city}")

#local variable
    def method4(self):
        a = "WORK FROM HOME"
        print(f"Local variable by directly variable is :  {a}")
e  = Employee("vamsi")
e.method1()
e.method2()
e.method3()
e.method4()
e.phonenumber = 123456789
e.Joindate = "AUG-2023"
print("Outside the class instance using  orv : ",e.phonenumber)
print("Outside the class static classname    : ",Employee.company)
print("Outside the class static using  ORV   : ",e.Joindate)