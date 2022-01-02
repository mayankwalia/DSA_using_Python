def prime(n):
    flag=True
    if n<2:
        flag=False
    for i in range(2,n):
        if(n%i)==0:
            flag=False
            break
    return flag
    
def Twin_Primes(n,m):
    twinp=[]
    for i in range(n,m-1):
        if prime(i) and prime(i+2):
            twinp.append((i,i+2))
    return twinp
n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))
