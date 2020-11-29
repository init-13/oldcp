def canf(s):
    if s.count(s[0])!=3:
        if s.count(s[0])==2:
            return s[0]
        elif s.count(s[1])==2:
            return s[1]
    else:
        return 0
f= open("out22.txt","w+")
for _ in range(int(input())):

    n=int(input())
    stg=input()

    stack=list()
    stack.append(stg[0])
    stack.append(stg[1])
    s=''
    for i in range(2,n):
        #print(stack)
        stack.append(stg[i])
        try:
            s=stack[-3]+stack[-2]+stack[-1]
        except:
            continue

        if canf(s):
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append(canf(s))
            
    if len(stack)==1:
        bol='Y'
    else:
        bol='N'
    
    xs="Case #{0}: {1}".format(_+1,bol)+'\n'
    #print(x)
    print(xs)
    f.write(xs)

f.close()

            
                

        
