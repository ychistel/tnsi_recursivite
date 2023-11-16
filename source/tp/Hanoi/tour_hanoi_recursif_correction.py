from pile import *

def dessus(pile):
    """
    cette fonction renvoie la valeur du disque du dessus de la pile si non vide
    sinon renvoie une valeur plus grande que tous les disques
    """
    if not pile.est_vide():
        x=pile.depiler()
        pile.empiler(x)
        return x
    else:
        return n+1
    
def transfert(p1,p2):
    """
    cette fonction passe un disque d'une pile vers une autre pile
    """
    d1 = dessus(p1)
    d2 = dessus(p2)
    if d1 <= n or d2 <= n:
        if d1 < d2:
            p1.depiler()
            p2.empiler(d1)
        else:
            p2.depiler()
            p1.empiler(d2)

def tour_hanoi(n,p1,p2,p3):
    # on résout le problème avec 2 disques
    if n == 2:   
        transfert(p1,p2)
        transfert(p1,p3)
        transfert(p2,p3)
    # sinon (n>2) on résout le problème avec n-1 disques en 5 étapes
    else:
        # on résout le problème des n-1 disques en les déplaçant de A vers C
        tour_hanoi(n-1,p1,p2,p3)
        # on déplace le disque n de A vers B
        transfert(p1,p2)
        # on résout le problème des n-1 disques en les déplaçant de C vers A
        tour_hanoi(n-1,p3,p2,p1)
        # on déplace le disque n de B vers C
        transfert(p2,p3)
        # on résout le problème des n-1 disques en les déplaçant de A vers C
        tour_hanoi(n-1,p1,p2,p3)
        

if __name__ == '__main__':
    
    # on définit le nombre de disques
    n = 4

    # on crée la pile A avec ces disques
    pileA = creer_pile()
    for i in range(n):
        pileA.empiler(n-i)
    # on crée les piles B et C vides
    pileB = creer_pile()
    pileC = creer_pile()
    
    # on affiche les piles avant le début du jeu
    print("Début du jeu")
    print("poteau 1:",pileA)
    print("poteau 2:",pileB)
    print("poteau 3:",pileC)
    
    # on lance la résolution du jeu des tours
    tour_hanoi(n,pileA,pileB,pileC)
    
    # on affiche les piles après la fin du jeu
    print("fin du jeu")
    print("poteau 1:",pileA)
    print("poteau 2:",pileB)
    print("poteau 3:",pileC)
