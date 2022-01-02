def expanding(L):
    if len(L)>=2:
        pdiff=abs(L[1]-L[0])
    for i in range(1,len(L)-1):
        diff=abs(L[i+1]-L[i])
        if (diff-pdiff)<=0:
            return False
        pdiff=diff
    return True
L = eval(input())
print(expanding(L))
