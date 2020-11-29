p,d=map(int,input().split())
minn=99999999
x=list()
for _ in range(int(d)):
    x.append((list(map(int,input().split()))))
    
sm=list()
av=list()
pm=list()

for i in x:
    il=len(i)
    tm=list()
    for t in range(il):
        tmm=list()
        for tt in range(il):
            tmm.append(sum(i[t:tt+1]))
        tm.append(tmm)

    
    sm.append(list(tm))
    av.append(list(tm))
    if len(sm)>1:
        tl=list()
        tlv=list()
        for x in range(p):
            #tll=list(zip(sm[0][x],sm[1][x]))
            tlvv=list(zip(av[0][x],av[1][x]))
            for n in range(p):
                #tll[n]=min(tll[n])
                tlvv[n]=sum(tlvv[n])
           # tl.append(list(tll))
            tlv.append(list(tlvv))
        #sm.clear()
        #sm.append(tl)
        av.clear()
        av.append(tlv)


for i in av:
    av=i
for i in range(d):
    for x in range(p):
        av[i][x]/=4
        for xx in range(d):
            n=av[i][x]-sm[xx][i][x]
            sm[xx][i][x]=[sm[xx][i][x],n]

        
        
print()
print(sm)
xmin=set()
lsip=list()

for x in range(int(d)):
    lsip.append(0)
xmax=int(p)
lsip.append(int(p))
#print(lsip)
for ii in range(2,len(lsip)+1):
    while(lsip[-ii]<xmax-1):
        tms=0
        lb=lsip[0]
        for ix in lsip:
            #tms+=sm[lb][-(ix+1)]
            lb=ix+1
            
        xmin.add(tms)
        lsip[-ii]+=1
        #print(lsip)
    xmax-=1
print(min(xmin))        
        
        
    
            
        
