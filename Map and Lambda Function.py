cube = lambda x: x**3

def fibonacci(n):
    a,b=0,1
    x=[]
    for i in range(n):
        x.append(a)
        c=a+b
        a,b=b,c
    return x
