# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
set1=list(map(int,input().split()))
n1=int(input())
set2=list(map(int,input().split()))
lst_set1=set(set1)
lst_set2=set(set2)
diff1=lst_set1.difference(lst_set2)
diff2=lst_set2.difference(lst_set1)
a_union=diff1.union(diff2)
a_union_sort=sorted(a_union)
for i in a_union_sort:
    print(i)
