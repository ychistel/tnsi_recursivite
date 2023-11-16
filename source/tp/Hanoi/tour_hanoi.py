n = 4

def dessus(L):
    if len(L) > 0:
        return L[len(L)-1]
    else:
        return n+1
    
def transfert(L1,L2):
    d1 = dessus(L1)
    d2 = dessus(L2)
    if d1 <= n or d2 <= n:
        if d1 < d2:
            L1.pop(len(L1)-1)
            L2.append(d1)
        else:
            L2.pop(len(L2)-1)
            L1.append(d2)
    
pileA = [n-i for i in range(n)]
pileB = []
pileC = []
print(pileA,pileB,pileC)
while len(pileC) != n:
    a = dessus(pileA)
    b = dessus(pileB)
    c = dessus(pileC)
    #print(a,b,c)
    if a < b and a < c:
        transfert(pileA,pileB)
        transfert(pileA,pileC)
    if b < a and b < c:
        transfert(pileB,pileC)
        transfert(pileB,pileA)
    if c < a and c < b:
        transfert(pileC,pileA)
        transfert(pileC,pileB)
    print(pileA,pileB,pileC)