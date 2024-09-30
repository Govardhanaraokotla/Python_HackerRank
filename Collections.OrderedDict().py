from collections import OrderedDict
a = OrderedDict()
n = int(input())
for _ in range(n):
    item1, item2, price = input().rpartition(' ')
    a[item1] = a.get(item1, 0) + int(price)
for item1, price in a.items():
    print(item1, price)
