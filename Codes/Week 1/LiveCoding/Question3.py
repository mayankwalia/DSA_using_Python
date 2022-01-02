def shuffle(L1,L2):
    i,j=0,0
    m,n=len(L1),len(L2)
    l=[]
    while(m>0 and n>0):
        if i==j:
            l.append(L1[i])
            m-=1
            i+=1
        else:
            l.append(L2[j])
            n-=1
            j+=1
    while(m>0):
        l.append(L1[i])
        m-=1
        i+=1
    while(n>0):
        l.append(L2[j])
        n-=1
        j+=1
    return l
L1 = eval(input())
L2 = eval(input())
print(shuffle(L1,L2))
