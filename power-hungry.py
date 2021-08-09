def solution(xs):
    neg=[]
    pos=[]
    for i in xs:
        if i<0:
            neg.append(i)
        elif i>0:
            pos.append(i)
    ans=1
    neg=sorted(neg)
    for i in pos:
        ans=ans*i
    if len(neg)%2==0:
        for i in neg:
            ans=ans*i
    else:
        for i in range(len(neg)-1):
            ans=ans*neg[i]
    if len(pos)==0:
        if len(neg)==1:
            if len(xs)==1:
                return str(neg[0])
            else:
                return str(0)
        elif len(neg)==0:
            return str(0) 
        else:
            return str(ans)   
    return str(ans) 