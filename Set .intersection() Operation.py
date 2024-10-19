# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
n_lst=set(map(int,input().split()))
n1=int(input())
n1_lst=set(map(int,input().split()))
total_lst=n_lst.intersection(n1_lst)
print(len(total_lst))
