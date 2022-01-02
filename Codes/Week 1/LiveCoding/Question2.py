def del_char(s,c):
    if len(c)==1:
        result=''
        for i in s:
            if i!=c:
                result+=i
    else:
        result=s
    return result
s = input()
c = input()
print(del_char(s,c))
