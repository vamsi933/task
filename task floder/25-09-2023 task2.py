#write a python program to merge two lists.
list_1 = input().split()                         #[1,"hi",2.0,True]
list_2 = input().split()                                #[1,2,3,4,5]
print(list_1+list_2)



#another method is extend
list_1 = input().split()                         #[1,"hi",2.0,True]
list_2 = input().split()                                #[1,2,3,4,5]
list_1.extend(list_2)
print(list_1)



#write a python program to find the sum of list elements.
list_1 = input().split()
list_1 = list(map(int,list_1))                        # 12 23 24
list_2 = 0
for i in range(0,len(list_1)):
    list_2 = list_2+list_1[i]
print(list_2)                    #59
    

# another method 
list_1 = input().split()
list_1 = list(map(int,list_1)) 
t = sum(list_1)
print(t)


#write a python program to print even and odd numbers seperatly in list.
list_1 = int(input())

even_num = []
odd_num = []
for i in range(1,list_1+1):
    if (i%2==0):
        even_num.append(i)
    else:
        odd_num.append(i)
print(even_num)
print(odd_num)

# another method
list_1 = list(map(int,input().split()))          # 3 5 6 7 9 2 4 12 19 20
even_num =[]
odd_num = []
for i in list_1:
    if (i%2==0):
        even_num.append(i)
    else:
        odd_num.append(i)

print(even_num)                 # 6 2 4 12 20
print(odd_num)                   # 3 5 7 9 19 





#write a python program to delete element of given index in list.
# by using pop

list_1 = input().split()                             #"hello" 20 29 36
list_2 = int(input())
list_1.pop(list_2)
print(list_1)                     #20 29 36


#another method is del
list_1 = input().split()
del(list_1[2])
print(list_1)

#.write a python program to delete given elemet from the list 


list_1 = input().split()                  #hello hai world hi 
list_1.remove("hi")
print(list_1)


#write a python program to insert an elemet  at given index location.
list_1 = input().split()
list_1.insert(2,"Marolix")
print(list_1)


#write a python program to check the sizes of given two lists are same.
list_1 = input().split()
list_2 = input().split()
if (len(list_1) == len(list_2)):
    print("same")
else:
    print("Not Same")


#Write a Python function that takes two lists and returns True if they have at least one common member.
list_1 = input().split()
list_2 = input().split()

for i in list_1:
    for j in list_2:
        if (i==j):
            print("True")
        
# another method
list_1 = input().split()
list_2 = input().split()

for i in list_1:
    for j in list_2:
        if i in j:
            print("True")


#Write a Python program to remove a specified column from a given nested list.
list_1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
n = 0
for i in ((list_1)):
    del i[n]
print(list_1)

#another method by taking user input

list_1 =[]
n =int(input("enter a size"))
for i in range (n):
    list_2 =[]
    for j in range(n):
        na = int(input("enter values :"))
        list_2.append(na)
    list_1.append(list_2)
a = 0
for i in list_1:
    i.pop(a)
print(list_1)

#Write a Python program to convert a list of multiple integers into a single integer.
list_1 = input().split()
for i in list_1:
    print(i,end="")


#Write a Python program to remove duplicates from a list.

list_1 = input()                                       #marolix

p=[]
for char in list_1:
	
    if char not in p:
        p.append(char)
print(p)