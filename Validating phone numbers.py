import re
n = int(input())
for i in range(0, n):
    if(re.match(r'^[7-9]{1}[0-9]{9}\n?\r?$', input())):
        print ("YES")
    else:
        print ("NO")
