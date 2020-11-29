import time

for _ in range(int(input())):
    strt=time.time()

    n=int(input())

    td=list()

    pdi=dict()
    pb=dict()
    pf=dict()
    
    vis=set()

    binc=dict()
    
    sm=set()
    
    hl=list()
    iff=list()
    ibb=list()

    for i in range(n):
        p,h=map(int,input().split())
        hl.append(h)
        pdi[p]=i
        x1=p-h
        x2=p+h

        iff.append(x2)
        ibb.append(x1)
        

        if x1 in pb:
            pb[x1].append(i)
        else:
            pb[x1]=[i]

        if x2 in pf:
            pf[x2].append(i)
        else:
            pf[x2]=[i]

    sm.add(max(hl))

    #print(pb,pf,pdi,iff,ibb)
    
    for i in range(n):
        #print(vis)
        if i in vis:
            continue
        else:
            s=hl[i]
            st=i
            while(1):
                #print(s,end=" ")
                #rint(vis,sm)
                vis.add(st)
                np=iff[st]

                if np in pb:
                    if np in binc:
                        binc[np].append(s)
                    else:
                        binc[np]=[s]
                        
                if np in pdi:
                    s+=hl[pdi[np]]
                    st=pdi[np]
                
                if np not in pdi:
                    sm.add(s)
                    break
    #print(binc)

    vis=set()

    for i in range(n-1,-1,-1):
        if i in vis:
            continue
        else:
            s=hl[i]
            st=i
            while(1):
                vis.add(st)
                np=ibb[st]
                if np in pf:
                    for xx in binc[np]:
                        sm.add(s+xx)
                        
                if np in pdi:
                    s+=hl[pdi[np]]
                    st=pdi[np]
                
                if np not in pdi:
                    sm.add(s)
                    break

                
    print("Case #{0}: {1}".format((_+1),max(sm)))

        
print(time.time()-strt)                        
                        
                    
                    
            

'''
    #FORWARD

    for i in range(n):
        chf=td[i][0]+td[i][1]
        chb=td[i][0]-td[i][1]
        

        if chf in fepf:
            if i in fg:
                
                fg[i].append(('F',fepf[chf]))

            else:
                fg[i]=[('F',fepf[chf])]

        if chb in bepf:
            if i in bg:
                bg[i].append(('B',bepf[chb]))
            else:
                bg[i]=[('B',bepf[chb])]

        if chf in fepb:
            if i in fg:
                
                fg[i].append(('B',fepb[chf]))

            else:
                fg[i]=[('B',fepb[chf])]

        if chb in bepb:
            if i in bg:
                bg[i].append(('F',bepb[chb]))
            else:
                bg[i]=[('F',bepb[chb])]

    print(bg,fg)

    sumset=strongdfs(fg,hl).union(strongdfs(bg,hl))
    sumset.add(max(hl))
    '''
    
        
