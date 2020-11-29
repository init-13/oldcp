f= open("out12.txt","w+")
for _ in range(int(input())):

    n=int(input())
    inc=list(input())
    out=list(input())

    x=list()
    for i in range(n):
        x.append(list('N'*n))

    x[0][0]='Y'

    for i in range(n):
        st=i
        
        #print()
        for j in range(i,n):
            #print(i,j,end="  ")
            if out[st]=='N':
                x[i][st]='Y'
                break

            elif j==i or (inc[j]=='Y'):
                x[i][j]='Y'
                st=j
                
            else:
                break

    for i in range(n):

        st=i
        #print()
        for j in range(i,-1,-1):
            #print(i,j,end="  ")
            if out[st]=='N':
                x[i][st]='Y'
                break
            elif j==i or ( inc[j]=='Y'):
                x[i][j]='Y'
                st=j
            else:
                break
    xs="Case #{0}:".format(_+1)+'\n'
    #print(x)
    
    for i in x:
        
        for j in i:
            xs+=j
        xs+='\n'
    
    print(xs)
    f.write(xs)

f.close()

            
                

        
