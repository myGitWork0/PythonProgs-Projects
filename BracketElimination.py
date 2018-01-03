def fun(str):
    opening=['{','(','[']
    closing=['}',')',']']
    d=dict(zip(opening,closing))
    x=0
    k=0
    li=[]
    w=False
    if len(str)%2!=0:
        return w
    while x<len(str):
        if str[x]=='{' or str[x] == '(' or str[x] =='[' :
            li.insert(k,str[x])
            k=k+1
        elif str[x]=='}' or str[x]==')' or str[x]==']':
            if k>0:
                if (d[li[k-1]]==str[x]) :
                    k=k-1
                    del li[k]

                else :
                    return w
            else :
                return w
        x = x + 1

    if len(li)==0:
        return True
    else:
        return False


str='{{}}{}({{{}}})}'
print(fun(str))

