import gc
import time



pdi=dict()
pb=dict()
pf=dict()

vis=set()

binc=dict()

sm=0

hl=list()
iff=list()
ibb=list()

for _ in range(int(input())):
    strt=time.time()
    n=int(input())

    

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

    sm=max(hl)

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
                        if s>binc[np]:
                            binc[np]=s
                        
			
                            
			    
                    else:
                        binc[np]=s
                        
                if np in pdi:
                    s+=hl[pdi[np]]
                    st=pdi[np]
                
                if np not in pdi:
                    if s>sm:
                        sm=s
                    break
    #print(binc)

    vis=set()
    iff.clear()
    pb.clear()
	
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
                    xx =binc[np]
                    if (s+xx)> sm:
                        sm=s+xx
		    
                        
                        
				
			
                        
                if np in pdi:
                    s+=hl[pdi[np]]
                    st=pdi[np]
                
                if np not in pdi:
                    if s>sm:
                        sm=s
			
                    break

                
    print("Case #{0}: {1}".format((_+1),sm))
    


    pdi.clear()
    
    pf.clear()
    
    vis.clear()

    binc.clear()
    
    
    hl.clear()
    
    ibb.clear()
    
    gc.collect()
    len(gc.get_objects())
print(time.time()-strt)
    
        
                        
                        
                    
   
