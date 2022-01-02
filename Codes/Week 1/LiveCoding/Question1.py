def isprime(n):
    for i in range(2,n):
        if (n%i==0):
            return False
    return True
def prime_product(m):
    for i in range(2,m):
        for j in range(2,i+1):
            if i*j==m:
                if isprime(i) and isprime(j):
                    return True
    return False
n = int(input())
print(prime_product(n))
