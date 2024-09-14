def print_rangoli(size):
     chr1=97 # ASCII code for 'a'. for 'A' it is 65
     def print_line(i):
        t=[]
        for j in range(i,size): t.append( chr(chr1 + j) )
        t = list(reversed(t)) + t[1:]
        centre, sides = "-".join(t), '--'*i
        print(sides+centre+sides)
        
     for i in reversed(range(size)): print_line(i)
     for i in range(1,size): print_line(i)
    
    
    

