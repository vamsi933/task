
# Write a python program to remove a given  character from string
string_1 = "Marolix Technology"
print(string_1.replace("n",""))


# Write a program to check String is Palindrome or not
str_1 = "madam"
str_2 = ""
for i in str_1:
    str_2 = i+str_2
if(str_1 == str_2):
    print("Palindrome")
else:
    print("Not Palindrome")


#Write a python program to check given character is vowel or consonant.

str_1 = "A"

vowels = "a","e","i","o","u","A","E","I","O","U"
if str_1 in vowels:
    print("Vowel")
else:
    print("Consonant")



#Write a python program to replace string space with given character in Python.


string_1 = "Marolix Technology"
print(string_1.replace("o"," "))


#Write a python program to count alphabets, digits, and special characters in the string
str_1 = "123abc3@$%67"
digit_1 = 0
alphabets_1 =0
special_character = 0
for i in str_1:
  
    if i.isalpha():
        alphabets_1 += 1 
        
    elif i.isdigit():
        digit_1 += 1
    else:
        special_character = special_character + 1 
print("alphabets_1 :", alphabets_1 ,"digit_1 :", digit_1, "special_character :", special_character)


#Write a python program to remove all the blank spaces in a given string.

str_1 = "Learning python is not easy"
print(str_1.replace(" ",""))


#Write a python program to find sum of integers in the string.

str_1 = "Marol124x89"
digit_count = 0
for i in str_1:
    if i.isdigit():
        i = int(i)
        digit_count += i 
print(digit_count)


#Write a python program to Remove Repeated Character from String.
str_1 = "Maroloix Technology"
p=""
for char in str_1:
	if char not in p:
		p=p+char
print(p)

#Write a python program to count occurrence of given character in string. 

str_1 = "marolix Technology"
print(str_1.count("o"))

#Write a python program to check string is anagrams or not in Python.
str_1 = "marolix"
str_2 = "rolixam"
if (sorted(str_1)==sorted(str_2)):
    print("Anagram")
else:
    print("Not Anagram")





