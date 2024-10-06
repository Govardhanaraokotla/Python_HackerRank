# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement
s,k=map(str,input().split())
sort_s=sorted(s)
a=combinations_with_replacement(sort_s,int(k))
for i in a:
    print("".join(i))
