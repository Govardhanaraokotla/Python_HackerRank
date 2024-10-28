# Enter your code here. Read input from STDIN. Print output to STDOUT
k=int(input())
rooms=list(map(int,input().split()))
a=set(rooms)
for i in a:
    rooms.remove(i)
    if i not in rooms:
        print(i)
        break

