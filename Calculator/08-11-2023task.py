def Calculator(a,b):
    c = int(input("ENter the number :"))
    if c == 1:
        return(a+b)
    elif c == 2:
        return(a-b)
    elif c == 3:
        return(a*b)
    elif c == 4:
        return (a/b)
    elif c == 5:
        return (a%b)
    elif c == 6:
        return (" ")
    else:
        return("Please enter valid input.")
x = int(input())
y = int(input())
print(Calculator(x,y))