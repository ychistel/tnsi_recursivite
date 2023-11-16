"""
def code_gray(n):
    if n==1:
        return ['0','1']
    else:
        code = []
        cg = code_gray(n-1)
        for i in range(len(cg)):
            code.append('0'+cg[i])
        for i in range(len(cg)):
            code.append('1'+cg[i])
        return code
"""
# il faut vérifier l'ordre des nombres
def code_gray(n):
    if n==1:
        return ['0','1']
    else:
        code_0,code_1 = [],[]
        cg = code_gray(n-1)
        for i in range(len(cg)):
            code_0 = code_0 + ['0' + cg[i]]
        for i in range(len(cg)):
            code_1 = ['1' + cg[i]] + code_1
        return code_0 + code_1
    
c = code_gray(2)