# Enter your code here. Read input from STDIN. Print output to STDOUT

n, x = map(int, input().split()) 
arr = []
for i in range(x):
    arr.append( map(float, input().split()) ) 

for i in zip(*arr): 
    print( sum(i)/len(i) )
        
    
    
