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
