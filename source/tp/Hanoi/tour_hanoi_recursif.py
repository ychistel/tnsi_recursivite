from pile import *
from interface_pyxel import *
from interface_console import *
    
def deplacer(n,p1,p2):
    """
    cette fonction passe un disque d'une pile vers une autre pile
    la fonction renvoie un tuple (i,j) désignant qui contient le poteau de départ et le poteau d'arrivée
    """
    # on dépile un poteau pour empiler le poteau de destination
    if not p1.est_vide():
        p2.empiler(p1.depiler())
    # on identifie les poteaux concernés et on crée un tuple de déplacement
    if p1 == poteau_depart:
        i = 1
    elif p1 == poteau_intermediaire:
        i = 2
    else:
        i = 3
    if p2 == poteau_depart:
        j = 1
    elif p2 == poteau_intermediaire:
        j = 2
    else:
        j = 3
    return (n,i,j)


def tour_hanoi(n,D,I,A):
    """
    D : poteau de départ
    I : poteau intermédiaires
    A : poteau d'arrivée
    n : nombre de disques et désigne le disque de taille n
    """
    if n == 1:
        # on déplace le disque n de D vers A
        i,j,k = deplacer(n,D,A)
        solution.append((i,j,k))
    else:
        # on résout le problème des n-1 disques en les déplaçant de D vers I
        tour_hanoi(n-1,D,A,I)
        
        # on déplace le disque n de D vers A
        i,j,k = deplacer(n,D,A)
        solution.append((i,j,k))
    
        # on résout le problème des n-1 disques en les déplaçant de I vers A
        tour_hanoi(n-1,I,D,A)
    return solution

"""
def tour_hanoi(n,D,I,A):
    """
"""
    D : poteau de départ
    I : poteau intermédiaires
    A : poteau d'arrivée
    n : nombre de disques et désigne le disque de taille n
    """
"""
    if n > 0:
        # on résout le problème des n-1 disques en les déplaçant de D vers I
        tour_hanoi(n-1,D,A,I)
        # on déplace le disque n de D vers A
        i,j,k = deplacer(n,D,A)
        solution.append((i,j,k))
        # on résout le problème des n-1 disques en les déplaçant de I vers A
        tour_hanoi(n-1,I,D,A)
    return solution
"""         
            
if __name__ == '__main__':
    
    # on définit le nombre de disques
    n = 4
    
    """
    la liste solution contient tous les déplacements de disques sur les poteaux.
    Ici les poteaux sont représentés par des entiers : 1 <- départ, 2 <- intermédiaire, 3 <- arrivée.
    Ce sont des tuples de 3 valeurs pour chaque déplacement:
    - valeur indice 0 : entier pour numéro de disque déplacé
    - valeur indice 1 : entier pour poteau de départ du disque soit 1, 2 ou 3
    - valeur indice 2 : entier pour poteau d'arrivée du disque soit 1, 2 ou 3
    """
    solution = []
    
    # Affichage en console par défaut
    console = False
    
    # on crée le poteau de départ avec avec ses disques de 1 à n
    poteau_depart = creer_pile()
    for i in range(n):
        poteau_depart.empiler(n-i)
    # on crée les poteaux intermédiaires et arrivée vides
    poteau_intermediaire = creer_pile()
    poteau_arrivee = creer_pile()
        
    # on lance la résolution du jeu des tours
    tour_hanoi(n,poteau_depart,poteau_intermediaire,poteau_arrivee)
    
    if console:
        # Affichage en console de la solution
        Tour_Hanoi_console(n,solution)
    else:
        # Affichage avec interface graphique pyxel de la solution
        Tour_Hanoi(n,solution)
