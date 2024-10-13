from itertools import groupby
s = input()

def print_new_list(s):
    lst = [] 
    for i,j in groupby(s):
        j = len(list(j))
        lst.append((int(j),int(i))) 
    print(*lst,sep=" ")

print_new_list(s)
