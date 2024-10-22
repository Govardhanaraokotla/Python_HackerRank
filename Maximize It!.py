import itertools

line = input()
K = int(line.split()[0])
M = int(line.split()[1])

N = []
for i in range(K):
  lst = input().split()
  lst = [ int(n) for n in lst ]
  lst = lst[1:]
  N.append(lst)

pro = list( itertools.product( *N ) )

maxi = 0
for item in pro:
  sum=0
  for num in item:
    sum += num**2
  modu = sum % M
  if (modu > maxi):
    maxi = modu

print (maxi) 
