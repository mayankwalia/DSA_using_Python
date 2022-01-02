def prime(n):
    flag=True
    for i in range(2,n):
        if (n%i==0):
            flag=False
            break
    return flag
    
def Goldbach(n):
    l=[]
    for i in range(2,n):
        for j in range(i,n):
            if (i+j==n) and (prime(i) and prime(j)):
                l.append((i,j))
    return l
n=int(input())
print(sorted(Goldbach(n)))
