print("Hello SAMSUNG")

def d2b(num,l=[]):
    if(num>=1):
        d2b(num//2,l)
        l.append(num%2)
    #print(num%2, end=" ")
    l=[str(i) for i in l]
    return "".join(l)


def get_num(l,k=5,p=2):
    end=len(l)-p
    start=end-k+1
    print(start)
    if(start>=0):
        print("==Binary is ",l)
        print("==Extracted from pos %s is %s"% (p,l[start:end+1]))
        res=l[start:end+1]
        return int(res,2)
    else:
        print("K value exceeds the digits from the given p")
    
out=d2b(171)
print(out)
print(get_num(out))



def braces(inp):
    l='{(['
    r='})]'
    res=[]
    d={']':'[',')':'(','}':'{'}
    for i in inp:
        if i in l:
            res.append(i)
        elif i in r:
            if(len(res)!=0):
                if(res[-1]==d[i]):
                    res.pop()
                else:
                    return False
            else:
                return False
    return len(res)==0
    
    
print(braces('{{()}}'))


def pattern(inp):
    for i in range(inp):
        print('*' * i)
        
    
pattern(5)