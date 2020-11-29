def strongdfs(graph,hl):
    
    allnodes=set(graph.keys())
    visnodes=set()
    sumset=set()

    while(allnodes):
        xtm=allnodes.pop()
        dfs(visnodes,graph,xtm,0,sumset,hl)
        visnodes=set()
        #allnodes=allnodes-visnodes

    return sumset
        
        
    





def dfs(v,g,n,sm,smd,hl):
    if n not in g:
        v.add(n)
        sm+=hl[n]
        smd.add(sm)
        #print(n,'#%',v)
        return
    #print(g,n,smd)
    if n not in v:
        v.add(n)
        sm+=hl[n]
        for nxt in g[n]:
            dfs(v, g, nxt,sm,smd,hl)
            #print(n,'#2%',v)
        
        




for _ in range(int(input())):

    n=int(input())

    td=list()

    fepf=dict()
    bepf=dict()

    fepb=dict()
    bepb=dict()

    fg=dict()
    bg=dict()

    hl=list()
    

    for i in range(n):
        p,h=map(int,input().split())
        td.append([p,h])
        hl.append(h)
        x1=p-h
        x2=p+h

        if p in fepf:
            fepf[p].append(i)
        else:
            fepf[p]=[i]

        if x1 in fepb:
            fepb[x1].append(i)
        else:
            fepb[x1]=[i]

        if p in bepf:
            bepf[p].append(i)
        else:
            bepf[p]=[i]

        if x2 in bepb:
            bepb[x2].append(i)
        else:
            bepb[x2]=[i]


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
    
    print("Case #{0}: {1}".format((_+1),max(sumset)))
        
