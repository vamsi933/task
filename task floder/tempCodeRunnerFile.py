list_1 = input().split(" ")                                      #marolix technology

p=[]
for char in list_1:
	
    if char not in p:
        p.append(char)
print(p)