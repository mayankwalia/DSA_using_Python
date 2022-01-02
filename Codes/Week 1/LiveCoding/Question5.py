def isodd(n):
    return n%2
def sumsquare(L):
    result=[0,0]
    for i in L:
        if isodd(i):
            result[0]+=i**2
        else:
            result[1]+=i**2
    return result
L = eval(input())
print(sumsquare(L))
