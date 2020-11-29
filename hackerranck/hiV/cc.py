def getMaxScore(jewels):
    j=list(jewels)
    j.append('$')
    jl=len(j)
    s=0
    i=0
    while(j[i]!='$'):
        print(j,i,s)
        if j[i]==j[i+1]:
            j.pop(i)
            j.pop(i)
            s+=1
            if i:
                i-=1
            
        else:
            i+=1
    return s
getMaxScore("absllsbd")
