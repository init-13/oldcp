def revd(r,c):
    ml=[]
    for i in range(r):
        ml.append(list(range(c)))
            
            
    x,y=(r-1,0)
    sp=1
    #li=list(range(1,r*c+1))
    while(y!=c):
        for i in range(y+1):
            if x-i>-1 and y-i>-1:
                #print(x-i,y-i)
                ml[x-i][y-i]=sp
                sp=sp+1

        y+=1

    y-=1
    x-=1

    while(x!=-1):
        for i in range(x+1):
            if x-i>-1 and y-i>-1:
                #print(x-i,y-i)
                ml[x-i][y-i]=sp
                sp=sp+1

        x-=1
    for i in ml:
        for j in i:
            print(j,end=' ')
        print()
    #print('\n')

revd(5,4)

    
    
            
