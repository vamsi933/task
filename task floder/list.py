# list topics
# create a list
list_1 = (input().split())
print(list_1)

# append list by integer only
list_1 = int(input())
list_2 =[]
for i in range(1,list_1+1) :
    if (i%2 == 0):
        list_2.append(i)   
print(list_2)


# insert method
list_1 = input().split()
list_2 = input()
list_1.insert(1,list_2)
print(list_1)

# append method

list_1 = input().split()
list_2 = input()
list_1.append(list_2)
print(list_1)


#Remove
list_1 = input().split()
list_2 = input()                   # remove the element by given specific element
list_1.remove(list_2)
print(list_1)

#pop method
list_1 = input().split()
list_2 = int(input())          #pop is remove by using th index method
list_1.pop(list_2)
print(list_1)


# clear method
list_1 = input().split()

list_1.clear()
print(list_1)

# delete method we can 
list_1 = input()
print(list_1)
del(list_1)
print(list_1)


#extended method
list_1 = input().split()
list_2 = input().split()
(list_1.extend(list_2))
print(list_1)


# sort method
list_1 = input().split()

(list_1.sort())
print(list_1)


# copy method
list_1 = input().split()

list_2=list_1.copy()
print(id(list_1))
print(id(list_2))

# or another method
list_1 = input().split()
list_2 = list_1[:]
print(id(list_1))
print(id(list_2))


# asling method
list_1 = input().split()
list_2 = list_1
print(id(list_1))
print(id(list_2))


# count method
list_1 = input()
list_2 = (input())
print([list_1.count(list_2)])

#exmple 

a = list(map(int,input().split()))
print(a.count(2))



# codes even and odd sort order in list
list_1 = list(map(int,input().split()))     # 3 8 5 7 1 6
even_num =[]
odd_num = []
for i in (list_1) :
    if (i%2 == 0):
        even_num.append(i)
    else:
        odd_num.append(i)

print(even_num)            # 8 6 
print(odd_num)             # 3 5 7 1

even_num.sort()  
odd_num.sort()   
print(even_num)   # 6 8
print(odd_num)    # 1 3 5 7 


