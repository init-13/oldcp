from collections import deque
def receivedText(s):
    sl=len(s)
    
    x=deque()
    lock=0
    cur=0
    ap=1
    ss=list()
    i=-1
    while(i<sl-1):
        i+=1
        #print(cur,"    ",x)
        if s[i]=='#':
            lock=lock^1
            continue
        if lock and s[i].isdigit():
            continue
        elif s[i]=='*':
            if  cur:
                cur-=1
                del x[cur]
                
            else:
                cur=0
            continue
        elif s[i]=='<':
            ap=0
            cur=0
            continue
        elif s[i]=='>':
            ap=1
            cur=len(x)
            continue
        else:
            if ap==1:
                x.append(s[i])
            elif ap==0:
                x.insert(cur,s[i])
            cur+=1
        
    return "".join(x)

print (receivedText('eee*<*B#*vn!21g#>231V'))
