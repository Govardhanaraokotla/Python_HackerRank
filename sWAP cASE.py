def swap_case(s):
    string=""
    for i in s:
        if i.isupper():
            string+=i.lower()
        else:
            string+=i.upper()
        
    return string

