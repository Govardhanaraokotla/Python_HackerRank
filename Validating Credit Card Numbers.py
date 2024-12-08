# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
sample = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
    
a=int(input().strip())
for i in range(a):
    print("Valid" if sample.search(input().strip()) else "Invalid")
