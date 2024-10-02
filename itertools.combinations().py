from itertools import combinations
w,n=input().split()
sw=sorted(w)
l=list(print("".join(combo)) for i in range(1,int(n)+1) for combo in combinations(sw,i))
