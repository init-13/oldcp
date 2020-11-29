from math import log2
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if n>65:
        print("NO")
        continue

    cd=set()
    N=0
    for i in l:
        if i in cd :
            N=1
            break
        else:cd.add(i)

    if N:
        print("NO")
        continue
    cd=set()
    nn=0
    for i in range(n):
        xn=0
        for x in range(i,n):
            xn|=l[x]
            if xn in cd:
                print("NO")
                nn=1
                break
            else: cd.add(xn)
        if nn:
            break
        
    if not nn:
        print('YES')
        continue
