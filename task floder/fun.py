# function calling
# function arguments
# keyword arguments
# possitional arguments
# default argumetns
# variable length argument
# keywordargs 


#  function calling
def print_arg():
    print("Hello World!")
print_arg()



#function arguments
#printing rightanle triangle by using function   
# * 
# * *
# * * *
# * * * *
# * * * * *           
def right_triangle(a):                                    
    for i in range(1,a+1):
        print("* "*i)
right_triangle(5)



# Another problem EVEN OR ODD NUMBERS
def show_numbers(number):
    # Complete this Function
    for i in range(0,number+1):
        if i % 2 ==0:
            print(str(i)+" EVEN")
        else:
            print(str(i)+" ODD")


number = int(input())
# Call the show_numbers function
show_numbers(number)


#keyword argument
def key_wordarg(a,b,c):
    print(a+b-c)
    print(b+a-c)
    print(c-a+b)
key_wordarg(a=10,b=99,c=88)



#positional keyword
def positionl_arg(a,b,c):
    print(a+b-c)
    print(b+a-c)
    print(c-a+b)
positionl_arg(10,99,88)




#default arguments taking the varable here only
def deafult_args(a=10,b = 20, c=70):
    print(a+b-c)
deafult_args()



#varable length argument is defined as (*)
def variable_leng(*a):
    d = 0 
    for i in (a):
        
        d = d+i 
    return d 
print(variable_leng(10,20))
print(variable_leng(1,2,3,4,5,6,))
print(variable_leng(10,90,888))
print(variable_leng(10,20,90,78))
print(variable_leng(10,20,1000,10000,100))

# another method multipication of numbers
def variable_leng(*a):
    d = 1
    for i in (a):
        
        d = d*i 
    return d 
print(variable_leng(10,20))
print(variable_leng(10,20,30))
print(variable_leng(10,20,-40))
print(variable_leng(10,20,90))



#keywordargs we there in dictinary format both key's and values
def keyword_args(**a):
    print(a)
    for i,j  in a.items():
        print(i,"-",j)
keyword_args(a_key = "hello",b_key="wolrd!")
keyword_args(a_key = "Python",b_key="is",c_key="easy",d_key="to Learn")
keyword_args(a_key = "10",b_key="20")
keyword_args(a_key = "100",b_key="101",c_key = 102)


#recurse function
def function(a):
    if a ==1:               #Base
        return 1
    return a *function(a-1)  #recursive
a =function(5)
print(a)


#sum of numbers in function
def get_sum(numbers):
    c = 0 
    for i in (numbers):
        c += int(i) 
    return c
numbers = input().split()
sum_of_numbers = get_sum(numbers)
print(sum_of_numbers)


#reverse string by using recurse function
def reverse_string(string):
    r = string[::-1]
    print(r)
string = input()
string_r = reverse_string(string)



# a small function that can be defined in a single line of code
a = lambda x: x**2
print(a(2))


#another method lambda
a = lambda x: x+2
print(a(98))


#greter than or lessthan by using lambda 
a = lambda x,y: x if x>y else y 
print(a(20,9))

#filter method 
a = [1,2,3,4,5,6,7,8,9,10]
r = list(filter(lambda x: x%2 == 0,a))
print(r)

#filter odd numbers
a = [1,2,3,4,5,6,7,8,9,10]
r = list(filter(lambda x: x%2 != 0,a))
print(r)


#filter vowles count
def vowels_count(a):
    b = "aeiou"
    for i in a:
        if i in b:
            return True
        else:
            return False
l = input()
l1 = filter(vowels_count,l)
print(list(l1))


#finding digit in the string

def fun(a):
    
    digit_count = 0
    for i in a:
        if i.isdigit():
            i = int(i)
            digit_count += i 
    return digit_count
str_1 = input()
str_2 = filter(fun,str_1)
print(list(str_2))
