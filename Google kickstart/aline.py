for x in range(int(input())):

    n=int(input())
    l=list(map(int,input().split()))

    lb=0
    ub=0
    

    rbc=0

    
    
    for i in range(1,n):
        
        if l[i]<l[i-1]:
            lb+=1
            ub=0
            
        elif l[i]>l[i-1]:
            ub+=1
            lb=0
        #xs.add(s)
        
            
        if lb>3 or ub>3 :
            #print("in",i)
            rbc+=1
            lb=0
            ub=0
            
    print("Case #{0}: {1}".format(x+1,rbc))
