from collections import defaultdict
n, m = map(int, input().split())
dict1 = defaultdict(list)
for i in range(n):
    a = input()
    dict1[a].append(i+1)
for j in range(m):
    b = input()
    if b not in dict1:
        print(-1)
    else:
        print(*dict1[b])
