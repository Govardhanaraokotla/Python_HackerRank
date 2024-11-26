# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

a = int(input())

for i in range(a):
   b = input()
   b = re.sub(r"\ \&\&\ "," and ",b)
   b = re.sub(r"\ \|\|\ "," or ",b)
   b = re.sub(r"\ \&\&\ "," and ",b)
   b = re.sub(r"\ \|\|\ "," or ",b)
   print(b)
