# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB=int(input())
BC=int(input())
m=math.sqrt(AB**2+BC**2)
theta=math.acos(BC/m)
print(int(round(math.degrees(theta),0)),'\u00B0',sep='')
