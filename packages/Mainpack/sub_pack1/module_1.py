def string_count(a):

    upper_case = 0
    lower_case = 0
    for i in a:
        if i.isupper():
            upper_case += 1
        elif i.islower():
            lower_case += 1
        
    print(upper_case)
    print(lower_case)
