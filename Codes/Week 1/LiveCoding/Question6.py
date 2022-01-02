def histogram(L):
    result=[]
    seen=[]
    for i in L:
        if i not in seen:
            result.append((L.count(i),i))
            seen+=[i]
    result.sort()
    final_result=[(j,i) for i,j in result]
    return final_result
L=eval(input())
print(histogram(L))
