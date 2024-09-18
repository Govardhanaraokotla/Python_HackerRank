from itertools import product
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=product(a,b)
for i in c:
    print(i,end=' ')
