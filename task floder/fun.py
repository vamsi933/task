def sum_1(a,b):
    
    print(a+b)
    print(b-a)
sum_1(10,20)

# a small function that can be defined in a single line of code
a = lambda x: x**2
print(a(2))


a = [1,2,3,4,5]
r = list(filter(lambda x: x%2 == 0,a))
print(r)


#recurse function
def function(a):
    if a ==1:               #Base
        return 1
    return a *function(a-1)  #recursive
a =function(5)
print(a)