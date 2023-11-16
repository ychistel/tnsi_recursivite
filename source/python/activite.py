def somme_f(n:int)->int:
    """ Calcule la somme des nombres entiers compris entre 1 et n: 1+2+...+(n-1)+n
        Paramètre:
            n : int
        Valeur renvoyée:
            nombre entier
            Exemple: somme(4) -> 1+2+3+4=10
        Algorithme itératif:
        - variable locale s = 1
        - Boucle for qui ajoute à la variable locale s la valeur de la variable de boucle i
    """
    s = 1
    for i in range(2,n+1):
        s += i
    return s

def somme_w(n:int)->int:
    """ Calcule la somme des nombres entiers compris entre 1 et n: 1+2+...+(n-1)+n
        Paramètre:
            n : int
        Valeur renvoyée:
            nombre entier
            Exemple: somme(4) -> 1+2+3+4=10
        Algorithme itératif:
        - variable locale s = 1, i = 2
        - Boucle while qui ajoute à la variable locale s la valeur de la variable de boucle i
        tant que i <= n
    """
    s = 1
    i = 2
    while i <= n:
        s += i
        i += 1
    return s

def somme_r(n):
    """ Calcule la somme des nombres entiers compris entre 1 et n: 1+2+...+(n-1)+n
        Paramètre:
            n : int
        Valeur renvoyée:
            nombre entier
            Exemple: somme(4) -> 1+2+3+4=10
        Algorithme récursif:
        - cas de base : n = 1
        - appel récursif : somme(n-1)
    """
    if n == 1:
        return 1
    else:
        return n + somme_r(n-1)
    
def somme_pairs(n):
    if n == 2:
        return 2
    if n%2 == 1:
        return somme_pairs(n)
    else:
        return n + somme_pairs(n-2)

def somme_suite(n):
    if n <= 2:
        return n
    else:
        return n + somme_suite(n-3)