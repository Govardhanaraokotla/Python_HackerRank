# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for i in range(int(input())):
    a = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', a)
        assert re.search(r'\d\d\d', a)
        assert not re.search(r'[^a-zA-Z0-9]', a)
        assert not re.search(r'(.)\1', a)
        assert len(a) == 10
    except:
        print('Invalid')
    else:
        print('Valid')
