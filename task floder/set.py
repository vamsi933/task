# set is in {}
#add
#clear
#copy
#union
#remove
#update
#discard
#intersection
#difference
#symmetric_difference
#pop()

# by taking user input in set
set_1 = set(input().split())
print(set_1)

#add method 
set_1 = set(input().split())
set_1.add('car')
print(set_1)

#clear
set_1 = set(input().split())
print(set_1.clear())


#copy
set_1 = set(input().split())
set_2 = set_1.copy()
print(set_2)

#remove
set_1 = set(input().split())             # in remove no element in remove it will shows error
(set_1.remove("20"))
print(set_1)

#pop
set_1 = set(input().split())            
(set_1.pop())
print(set_1)

#discard
set_1 = set(input().split())              #it will not shows error
(set_1.discard("20"))
print(set_1)


#update
set_1 = set(input().split())
set_2 = set(input().split())
(set_1.update(set_2))
print(set_1)


#union 
set_1 = set(input().split())     # it will come all from one and two
set_2 = set(input().split())
set_3=(set_1.union(set_2))
print(set_3)

#intersection
set_1 = set(input().split())               #it will comes 2 set's of combine values only
set_2 = set(input().split())
set_3=(set_1.intersection(set_2))
print(set_3)

#difference
set_1 = set(input().split())               #it will comes 2 set's of diffenrce values only print from set 1
set_2 = set(input().split())
set_3=(set_1.difference(set_2))
print(set_3)


#symmetric difference
set_1 = set(input().split())               #it will comes 2 set's of diffenrce values only print from set1 and set2
set_2 = set(input().split())
set_3=(set_1.symmetric_difference(set_2))
print(set_3)

#isdisjoint
#Return True if no items in set x is present in set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)



def add(a,b):
    return a+b 
add(10,20)