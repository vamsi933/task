# 1.Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12


def string_count(a):

    upper_case = 0
    lower_case = 0
    for i in a:
        if i.isupper():
            upper_case += 1
        elif i.islower():
            lower_case += 1
        
    print(upper_case)
    print(lower_case)

a = input()
string_count(a)


# 2.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]


def list_dup(a):
    unique_list = []
    for i in a:
        if i  not in  unique_list:
            unique_list.append(i)
    print(unique_list)
a = input().split()
list_dup(a)



#Write a Python function to create and print a list where the values are the squares of numbers between 1 and 10 (both included)
def square_num(a):
    list_1 =[]
    for i in range(1,a+1):
        list_1.append(i**2)
    print(list_1)
a = int(input())
square_num(a)




# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20 

def sum_all(a):
    list_1 =0
    for i in (a):
        list_1 += int(i) 
    return (list_1)
a = input().split()
print(sum_all(a))




#write a function to find sum of given values, pass values has variable number of arguments to function
def values_all (*a):
    d = 0
    for i in a:
        d = d+i 
    return (d)
print(values_all(1,2,3))
print(values_all(30,505,90))
print(values_all(10,20,30,50))





# Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog".

def fun_string(string):
    # function to check if all elements are present or not
    string=string.replace(" ","")
    string=string.lower()
    alphabets="abcdefghijklmnopqrstuvwxyz"
    c=0
    for i in alphabets:
        if i in string:
            c+=1
    if(c==len(alphabets)):
        print("The string is a pangram")
    else:
        print("The string isn't a pangram")
a = input()
fun_string(a)