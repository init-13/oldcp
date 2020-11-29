def getMaxScore(j):
    jl=len(j)
    for x in range(jl):
        j[x]-=1
    pr=set()
    pr.add(0)
    node=0
    nc=0
    ir=list(range(1,jl))
    i=0
    while(ir):
        while(1):
            pr.add(j[i])
            print(ir,pr)
            if (j[i] in pr):
                if j[i]==i:
                    node=1
                nc+=1
                break
            i=j[i]
        for x in range(1,len(pr)+1):
            ir.pop(-x)
        pr.clear()
        if not ir:
            break
        i=ir[0]
        
    print(nc-node)
getMaxScore([2, 3, 4, 1, 5])
