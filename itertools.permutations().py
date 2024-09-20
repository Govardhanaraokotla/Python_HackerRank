from itertools import permutations
s,k=map(str,input().split())
a=list(permutations(s.upper(),int(k)))
for i in sorted(a):
    print("".join(i))
