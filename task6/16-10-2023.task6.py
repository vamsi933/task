#REcurssion
#FIlter
#map
#nesed function
#REDUCE


#RECURSSION METHOODS
#FACTORIAL OF NUMBER

def factorail_ALL(x):
    if x==1:
        return 1
    return x*factorail_ALL(x-1)
a = int(input())
print(factorail_ALL(a))


#ANOTHER EX IS FIBONACI SERIES
def fibonaaci_series(x):
    if x<=1:
        return 1
    return (fibonaaci_series(x-1)+fibonaaci_series(x-2))
a = int(input())
print(fibonaaci_series(a))


# function that adds a list of python
def sum_n(n):
    if n== 0:
        return 0
    else:
        return n + sum_n(n-1)
    
a = int(input())
print(sum_n(a))



#FILTER METHOD
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
b = list(filter(lambda x: x%2 == 0,a))
print(b)


#filter by vowles
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False
filtered_vowels = filter(filter_vowels, letters)
vowels = tuple(filtered_vowels)
print(vowels)


#REDUCE
from functools import reduce
a = [1,2,3,4,5]
b = reduce(lambda x,y: x*y,a)
print(b)

#ADDING TWO ELEMENTS
from functools import reduce
 
def do_sum(x1, x2): 
    return x1 + x2

print(reduce(do_sum, [1, 2, 3, 4]))

#MULTIPLY 
from functools import reduce
 
def do_sum(x1, x2): 
    return x1 * x2

print(reduce(do_sum, [1, 2, 3, 4]))


#NESTEDD FUNCTION
def greet(name):
        print("HELLO",name)
        def display_name():
            print("Hi", name)
        display_name()
greet("John")  


# another one is
def exponential(x):
    def square(y):
        return y * y
    return square(x) * square(x)  # 2*2  * 2*2

print(exponential(2))  #16 

#MAP
a =[1,2,3,4,5]
b = list(map(lambda x: x**2,a))
print(b)


a = [1,2,3,4,5,6,7,8,9,10]
b = list(map(lambda x: x%2 == 0,a))
print(b)