
x=list()
pathb=list()
for _ in range(int(input())):

    n,m=map(int,input().split())

    
    se=0
    sn=0
    
    sp=1

    s0=1
    no=0
    for i in range(n):
        x.append(int(input()))

    snset=0
    for i in range(n-2,0,-1):
        #print(sp,x[i])
        #print(sn,se,s0,sp,end="^^")
        if sp==m+1 and not snset:
            no=1
            break
            
        if s0==m+1:
            no=1
            break
        
        if x[i]==0:
            s0+=1
            if sp==m:
                #print(sp,sn,se,x[i],"$$",end=" ")
                snset=0
                s0=1
                sp=0
                pathb.append(sn)
                se=sn
                sn=0
            sp+=1
            #print()
            continue
        
        elif not snset:
            sn=x[i]+se
            snset=1
        #print(x[i],sn,se)
        if x[i]+se<sn:
            #print('##')
            sn=x[i]+se
           # print(sn,se,"99")
        #print(sp)
        if sp==m:
            #print(sp,sn,se,x[i],"$$",end=" ")
            snset=0
            s0=1
            sp=0
            pathb.append(sn)
            se=sn
            sn=0
            #print(sp,sn,se,x[i],"$",end=" ")
            

        #print(sn,se,s0,sp)    
        sp+=1
    try:
        print(pathb.pop())
    except:
        print(-1)
    x.clear()
    pathb.clear()

        

        
        
        
        
        
