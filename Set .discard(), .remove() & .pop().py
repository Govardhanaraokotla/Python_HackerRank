n = int(input())
s = set(map(int, input().split()))
ope=int(input())
for i in range(ope):
    a=input()
    if a=="pop":
        s.pop()
    else:
        b,c=a.split(' ')
        if b=="remove":
            s.remove(int(c)) 
        else:
            s.discard(int(c))
print(sum(s))
    

