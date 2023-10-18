def fun_string(string):
    # function to check if all elements are present or not
    string=string.replace(" ","")
    string=string.lower()
    alphabets="abcdefghijklmnopqrstuvwxyz"
    c=0
    for i in alphabets:
        if i in string:
            c+=1
    if(c==len(alphabets)):
        print("The string is a pangram")
    else:
        print("The string isn't a pangram")
