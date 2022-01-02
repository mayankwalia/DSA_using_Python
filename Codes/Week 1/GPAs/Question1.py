def find_Min_Difference(L,P):
    l=sorted(L)
    if P==1:
      return min(l)
    mini=max(l)
    for i in range(0,len(l)):
        if ((i+P)<=len(l)):
            if (l[P+i-1]-l[i])<mini:
                mini=l[P+i-1]-l[i]
    return mini
L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))
