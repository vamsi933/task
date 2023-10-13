# .Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}

dict_1 = {}
a = int(input("enter size :"))
for i in range(a):
    keys = input("enter the key :")
    values = input("enter the vales :")
    dict_1[keys] = values
    dict_1.update({'name':"vamsi"})
print(dict_1)



#2.Write a Python script to check whether a given key already exists in a dictionary.
dict_1 = {}
a = int(input("enter size :"))
for i in range(a):
    keys = input("enter the key :")
    values = input("enter the vales :")
    dict_1[keys] = values
    
    c = input("enter the key exsit :")
if c in dict_1 :
    print("Keys already exsist")
else:
    print("Not exsist")

#Write a Python program to iterate over dictionaries using for loops
dict_1 = {}
a = int(input("enter size :"))
for i in range(a):
    keys = input("enter the key :")
    values = input("enter the vales :")
    dict_1[keys] = values
for i in dict_1.items():
    print(i)


# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
dict_1={}
a = int(input())
for x in range(1,a+1):
    dict_1[x]=x*x
print(dict_1)



# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'marolix technology'
string_1 = input("enter the text:")
dict_1 ={}
for i in string_1:
    if i in dict_1:
        dict_1[i] += 1
    else:
        dict_1[i] = 1
for j in dict_1:
    print(j, ':',dict_1[j] ,end=" ")


#Write a Python program to sum all the items in a dictionary
# Sum of values of a dictionary

dict_1 = {}
a = int(input("enter size :"))
for i in range(a):
    keys = input("enter the key :")
    values = int(input("enter the vales :"))
    dict_1[keys] = values
s = sum(dict_1.values())
print(s)

#.Write a Python program to combine two dictionary by adding values for common keys.
dict_1 = {'a': 100, 'b': 200, 'c':300}
dict_2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
for i, j in dict_1.items():

    for x, y in dict_2.items():

        if i == x:

            d3[i]=(j+y)

print(d3)



#Write a Python program to access dictionary key's element by index.
dict_1 = {}
a = int(input("enter size :"))
for i in range(a):
    keys = input("enter the key :")
    values = input("enter the vales :")
    dict_1[keys] = values
print(dict_1.keys())

#Write a Python program to remove a key from a dictionary.
dict_1 = {}
a = int(input("enter size :"))
for i in range(a):
    keys = input("enter the key :")
    values = input("enter the vales :")
    dict_1[keys] = values
dict_1.pop("car")
print(dict_1)

#Write a Python script to merge two Python dictionaries.d
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)