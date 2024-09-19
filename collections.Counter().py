from collections import Counter
x_shoes = int(input())
y_shoe_sizes = Counter(map(int, input().split()))
n = int(input())
total = 0
for i in range(n):
    size, rate = map(int, input().split())
    if y_shoe_sizes[size]: 
        y_shoe_sizes[size] -= 1
        total += rate
print(total)
