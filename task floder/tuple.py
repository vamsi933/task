#by taking user input
tuple_1 = tuple(input().split())
print(tuple_1)


#maximum
tuple_1 = tuple(input().split())
print(min(tuple_1))


#maximum
tuple_1 = tuple(input().split())
print(max(tuple_1))


#index
tuple_1 = tuple(input().split())
print(tuple_1[:2])

# another example
tuple_1 = tuple(input().split())
print(tuple_1[::-1])


# by updating the present value
tuple_1 = tuple(input().split())
tuple_2 = list(tuple_1)
tuple_2[2] = "teja"
print(tuple(tuple_2))

#length
tuple_1 = tuple(input().split())
print(len(tuple_1))

#insert method not possible in tuple by changing into list is possible
tuple_1 = tuple(input().split())
tuple_2 = list(tuple_1)
tuple_2.insert(2,"car")
print(tuple(tuple_2))

#packing tupple
fruits = ("apple", "banana", "cherry")
print(fruits)

#unpacking
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
