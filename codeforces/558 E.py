def ns (st,s):
    return st[:s[0]]+"".join(sorted(st[s[0]:s[1]],reverse=not bool(s[2])))+st[s[1]:]

t=input().split()
st=input()
nt=int(t[1])
ilis=list()
while(nt):
    a,b,c=(map(int,input().split()))
    if a==b:
        nt-=1
        continue
    a-=1
    ni=0
    poplist=list()
    for i in range(1,len(ilis)+1):
        i*=-1
        #print(a,b,ilis[i])
        x1=int( ilis[i][0] in range(a,b+1))
        x2=int( ilis[i][1] in range(a,b+1))
        x=x1+x2
        
        if x==1:
            break
        elif x==2 and c==ilis[i][2]:
            poplist.append(i)
            
        elif (a in range(ilis[i][0],ilis[i][1])) and (b in range(ilis[i][0],ilis[i][1]+1)) and c==ilis[i][2] :
            ni=1
            break
            
        elif ilis[i][0]==a and ilis[i][1]==b:
            ni=1
            if ilis[i][2]!=c:
                ilis.pop(i)
            break
    while(poplist):
        ilis.pop(poplist.pop())
    if not ni:
        ilis.append([a,b,c])
    nt-=1
for i in ilis:
    st=ns(st,i)
#print(ilis)
print(st)
