def list_dup(a):
    unique_list = []
    for i in a:
        if i  not in  unique_list:
            unique_list.append(i)
    print(unique_list)