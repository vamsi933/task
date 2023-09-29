#def differenceofSum(n.m)

"""The function takes two integrals m and n as arguments. You are required to obtain the total of all integers ranging between 1 to n (both inclusive) which are not divisible by m. You must also return the distinction between the sum of integers not divisible by m with the sum of integers divisible by m.

Assumption

m > 0 and n > 0
Sum lies within the integral range
 
Example

Input:
m = 6
n = 30

Output:
285

Integers divisible by 6 are 6, 12, 18, 24, and 30. Their sum is 90.
Integers that are not divisible by 6 are 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 25, 26, 27, 28, and 29. Their sum is 375.
The difference between them is 285 (375 – 90).
 
Sample input:
m = 3
n = 10

Sample output:
19"""

a = int(input())
b = int(input())
c = 0
d = 0
for i in range(1,b+1):
    if i %a == 0:
        c = c+i 
    elif i %a!=0:
        d = d+i 
print(d-c)


"""The function takes an integral arr which is of the size or length of its arguments. Return the sum of the second smallest element at odd position ‘arr’ and the second largest element at the even position.

Assumption

Every array element is unique.
Array is 0 indexed.
Note:

If the array is empty, return 0.
If array length is 3 or <3, return 0.
 
Example

Input:
Arr: 3 2 1 7 5 4

Output:
7
 """
a = [3,2,1,7,5,4]
if len(a)==0 or len(a)<3:
    r =0
else:
    
    r = a[-2]+a[2]
print(r)


"""Write a function to validate if the provided two strings are anagrams or not. If the two strings are anagrams, then return ‘yes’. Otherwise, return ‘no’.
Input:

Input 1: 1st string
Input 2: 2nd string

Output:
(If they are anagrams, the function will return ‘yes’. Otherwise, it will return ‘no’.)

Example

Input 1: Listen
Input 2: Silent

Output:
Yes

Explanation

Listen and Silent are anagrams (an anagram is a word formed by rearranging the letters of the other word)."""

str_1 = input()
str_2 = input()
if(sorted(str_1)== sorted(str_2)):
    print("True")
else:
    print("False")

"""4. Perform the following function. 
def Productsmallpair(sum,arr)

This function accepts the integers sum and arr. It is used to find the arr(j) and arr(k), where k ! = j. arr(j) and arr(k) should be the smallest elements in the array.

Keep this in mind:

If n<2 or empty, return –1.
If these pairs are not found, then return to zero.
Make sure all the values are within the integer range.
 
Example

Input:
Sum: 9
Arr: 5 4 2 3 9 1 7

Output:
2

Explanation

From the array of integers, we have to select the two smallest numbers, i.e 2 and 1. Sum of these two (2 + 1) = 3. This is less than 9 (3 < 9). The product of these two is 2 (2 x 1 = 2) Hence the output is integer 2.

Sample input:
Sum: 4
Arr: 9 8 –7 3 9 3

Sample output:
–21"""


a= 9
b = [5,4,2,3,9,1,7]
if len(b)==0 or len(b)<2:
    r = -1
else:
    b.sort()
    s1 = int()
    s2 = int()
    for i in b:
        if i < s1:
            s2=s1
            s1 =i
        elif i<s2:
            s2 = i 

    if s1+s2<a:
        r = s1*s2
    else:
        r =0
print((r))
    


"""8. Perform the function: Int operationchoices(int c, int n, int a, int b). This function considers three positive inputs of a, b and c.
Execute the function to get:
(a + b), if c = 1
(a / b), if c = 4
(a – b), if c = 2
(a x b), if c = 3

Example:

Input:
a: 12
b: 16
c: 1

Output:
28

Explanation
C = 1, hence the function is (a + b). Hence, the output is 28.

Sample input:
a: 16
b: 20
c: 2

Sample output:"""
a = int(input())
b = int(input())
c = int(input())
if (c==1):
    r = (a+b)
elif (c==2):
    r =(a-b)
elif (c==3):
    r =(a*b)
elif (c==4):
    r = (a/b)

print(r)


"""9. Perform the function Int calculate(int m, int n). This function needs two positive integers. Calculate the sum of numbers between these two numbers that are divisible by 3 and 5.
Assumption
m > n > = 0

Example

Input:
m: 12
n: 50

Output:
90

Explanation
The numbers between 12 and 50 that are divisible by 3 and 5 are 15, 30, and 45. The sum of these numbers is 90.

Sample input:
m: 100
n: 160

Sample output:
405"""
a = int(input())
b = int(input())
c = 0
for i in range(a,b+1):
    if i%3==0 and i %5==0:
        
        c +=i
print(c)