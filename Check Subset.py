# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    a = int(input())
    set_a = set((map(int, input().split())))
    b = int(input())
    set_b = set((map(int, input().split())))
    print(set_a.issubset(set_b))
