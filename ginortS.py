# Enter your code here. Read input from STDIN. Print output to STDOUT
string=input()
a=[]
b=[]
c=[]
d=[]
e=[]
for i in string:
    if i.isalpha() and i.islower():
        a.append(i)
    elif i.isupper():
        b.append(i)
    elif i.isalnum() and int(i)%2!=0:
        c.append(i)
    else:
        d.append(i)
a.sort()
b.sort()
c.sort()
d.sort()
a.extend(b)
a.extend(c)
a.extend(d)

for i in a:
    print(i,end='')
        
    
        
