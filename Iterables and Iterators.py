# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

n = int(input())
l = input().split()
k = int(input())

a = list(combinations(l, k))
f = filter(lambda c: 'a' in c, a)
print("{0:.3}".format(len(list(f))/len(a)))
