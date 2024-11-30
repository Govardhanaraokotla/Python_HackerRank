import re

n=int(input())

for i in range(n):
    a=input()

    a_split=a.split()

    if len(a_split)>1  and  '{' not in a_split:
        a_split=re.findall(r'#[a-fA-F0-9]{3,6}',a)
        [print(i) for  i in a_split]
