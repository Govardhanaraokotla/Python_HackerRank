# Enter your code here. Read input from STDIN. Print output to STDOUT

a=int(input())
a_set=set(map(int,input().split()))
b=int(input())
for i in range(b):
    c, d = input().split()
    b_set=set(map(int,input().split()))
    if c=="intersection_update":
        a_set.intersection_update(b_set)
    elif c=="update":
        a_set.update(b_set)
    elif c=="symmetric_difference_update":
        a_set.symmetric_difference_update(b_set)
    else:
        a_set.difference_update(b_set)
print(sum(a_set))

    
    
