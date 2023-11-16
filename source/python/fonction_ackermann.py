i=1
i_max=0
def ackermann(m,n):
    global i,i_max
    if m==0:
        if i>i_max:
            i_max=i
            print(i_max)
        else:
            i=0
        return n+1
    elif m>0 and n==0:
        i +=1
        return ackermann(m-1,1)
    else:
        i+=1
        return ackermann(m-1,ackermann(m,n-1))
        
print(ackermann(4,5))