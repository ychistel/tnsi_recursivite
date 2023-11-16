def ecrire(n):
    if n > 0:
        print("phrase numéro %s" % n)
        ecrire(n-1)

def ecrire2(n):
    if n > 0:
        ecrire2(n-1)
        return "phrase numéro %s" % n

def ecrire3(n):
    if n > 0:
        return ecrire3(n-1)+"phrase numéro %s\n" % n
    else:
        return ''
    
def ecrire4(n):
    if n > 0:
        return "phrase numéro %s\n" % n + ecrire4(n-1)
    else:
        return ''

print(ecrire4(5))
