def odd_one(L):
    l=[type(i) for i in L]
    for i in range(len(l)):
        if l.count(l[i])==1:
            if type(L[i])==int:
                return 'int'
            elif type(L[i])==float:
                return 'float'
            elif type(L[i])==str:
                return 'str'
            elif type(L[i])==bool:
                return 'bool'
    
print(odd_one(eval(input().strip())))
