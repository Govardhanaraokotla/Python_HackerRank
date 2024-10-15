# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
n_lst=set(map(int,input().split()))
n1=int(input())
n1_lst=set(map(int,input().split()))
total_set=n_lst.union(n1_lst)
print(len(total_set))
