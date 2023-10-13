
#clear
# copy
# fromkeys
# get
# items
# keys
# pop
# popitem
# update
# values

# # dictionary userinput method
dic_1 = {}
size_dict =  int(input("enter size"))
for i in range(size_dict):
    key = input("enter user input key")
    value = input("enter user value")
    dic_1[key] = value
print(dic_1)

#clear method
dic_1 = {}
size_dict =  int(input("enter size :"))
for i in range(size_dict):
    key = input("enter user input key :")
    value = input("enter user value :")
    dic_1[key] = value
    dic_1.clear()
print(dic_1)

#copy
dic_1 = {}
size_dict =  int(input("enter size :"))
for i in range(size_dict):
    key = input("enter user input key :")
    value = input("enter user value :")
    dic_1[key] = value
    dic_2 =dic_1.copy()
print(dic_2)


#update
dic_1 = {}
size_dict =  int(input("enter size :"))
for i in range(size_dict):
    key = input("enter user input key :")
    value = input("enter user value :")
    dic_1[key] = value
    dic_1.update({"id":2023})
print(dic_1)


# fromkeys
a = input().split()
b = int(input())
c = dict.fromkeys(a,b)
print(c)


# get it's return the values

dic_1 = {}
size_dict =  int(input("enter size :"))
for i in range(size_dict):
    key = input("enter user input key :")
    value = input("enter user value :")
    dic_1[key] = value
    dic_2 =dic_1.get(key)
print(dic_2)



# items  the output will be shown in list,tuple. a.items()
dic_1 = {}
size_dict =  int(input("enter size :"))
for i in range(size_dict):
    key = input("enter user input key :")
    value = input("enter user value :")
    dic_1[key] = value
    dic_2 = dic_1.items()
print(dic_2)


# keys it will shows only keys of dictinaroy
dic_1 = {}
size_dict =  int(input("enter size :"))
for i in range(size_dict):
    key = input("enter user input key :")
    value = input("enter user value :")
    dic_1[key] = value
    dic_2 = dic_1.keys()
print(dic_2)


# values
dic_1 = {}
size_dict =  int(input("enter size :"))
for i in range(size_dict):
    key = input("enter user input key :")
    value = input("enter user value :")
    dic_1[key] = value
    dic_2 = dic_1.values()
print(dic_2)

# pop 
dic_1 = {}
size_dict =  int(input("enter size :"))
for i in range(size_dict):
    key = input("enter user input key :")
    value = input("enter user value :")
    dic_1[key] = value
    dic_2 = dic_1.pop("age")
print(dic_2)

# another method by taking input 
dic_1  = {'name':'vamsi','age':23,'id':2023}
dic_1.pop('age')
print(dic_1)

# popitem 
dic_1 = {}
size_dict =  int(input("enter size :"))
for i in range(size_dict):
    key = input("enter user input key :")
    value = input("enter user value :")
    dic_1[key] = value
    dic_2 = dic_1.popitem()
print(dic_2)


#c0de rename of keys

fruits = {
    "apples": 10,
    "bananas": 20,
    "mangoes": 15,
    "oranges": 200,
    "watermelons": 50
}

a = input()
b = input()
fruit_urem=list(fruits.items())
fruit_urem_copy = fruit_urem.copy()
fruit_count = len(fruit_urem)
for i in range(fruit_count):
    if fruit_urem[i][0]==a:
        updated_tuple = (b,fruit_urem[i][1])
        fruit_urem_copy[i]=updated_tuple
print(fruit_urem_copy)