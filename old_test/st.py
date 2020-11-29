
for i in range(int(input())):
    n=int(input())
    s=input()
    d=dict()

    
    if n%2:
        print("NO")
        continue

    
    else:
        for x in range(n):
            if s[x] in d:
                d[s[x]]+=1
            else:
                d[s[x]]=1
        nn=0
        for x in d.values():
            if x%2:
                print("NO")
                nn=1

        if not nn:
            print("YES")
            
            
                
