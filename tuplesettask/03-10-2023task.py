# 1.Write a Python program to unpack a tuple into several variables.
tuple_1 = tuple(input().split())
print(tuple_1)
p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8 = tuple_1
print(p_1)
print(p_2)
print(p_3)
print(p_4)
print(p_5)
print(p_6)
print(p_7)
print(p_8)



#2.Write a Python program to add an item to a tuple.
tuple_1 = tuple(input().split())
tuple_2 = tuple(input().split())
print(tuple_1 + tuple_2)


# 3.Write a Python program to convert a tuple to a string.
# Ex:tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
tuple_1 = tuple(input().split())
tuple_1 = "".join(tuple_1)
print(tuple_1)

#4.Write a Python program to get the specified element from the last element of a tuple.
tuple_1 = tuple(input().split())
print(tuple_1[-1])

#method 2
tuple_1 = tuple(input().split())
tuple_2 = int(input())
print(tuple_1[tuple_2])


#5.Write a Python program to add member(s) to a set.
set_1 = set(input().split())
set_2.add("nag")
print(set_1)


#another method 
set_1 = set(input().split())
set_2 = set(input().split())
set_3=set_1.update(set_2)
print(set_3)


#6.Write a Python program to create an intersection of sets.
set_1 = set(input().split())
set_2 = set(input().split())
print(set_1.intersection(set_2))


#7.Write a Python program to create a union of sets.
set_1 = set(input().split())
set_2 = set(input().split())
print(set_1.union(set_2))


#8.Write a Python program to create set difference.
set_1 = set(input().split())
set_2 = set(input().split())
print(set_1.difference(set_2))

#9.Write a Python program to create a symmetric difference.
set_1 = set(input().split())
set_2 = set(input().split())
print(set_1.symmetric_difference(set_2))


#10.Write a Python program to find the maximum and set_1 = set(input().split())
set_1 = set(input().split())
print(max(set_1))


# Write a Python program to find the set_1 = set(input().split())
set_1 = set(input().split())
print(min(set_1))