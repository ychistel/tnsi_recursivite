import turtle
from random import randint

def vecteur(A,B):
    """
    Trace une ligne entre deux points A et B dont on donne les coordonnées.
    Paramètres : A et B sont 2 tuples de deux coordonnées A(x0,y0) et B(x1,y1)
    """
    x0,y0=A[0],A[1]
    x1,y1=B[0],B[1]
    # On lève le crayon avant de se déplacer
    turtle.up()
    # on place la tortue au premier point A
    turtle.goto(x0,y0)
    # on détermine la distance d à tracer entre A et B
    d=turtle.distance(x1,y1)
    # on détermine l'angle a avec l'horizontal vers l'est pour joindre A et B
    a=turtle.towards(x1,y1)
    # on pivote la tortue de l'angle pour rejoindre le point B
    turtle.left(a-turtle.heading())
    # on baisse la tortue pour tracer
    turtle.down()
    # on trace la ligne AB
    turtle.forward(d)
        
def polygone(*args):
    """
    Dessine un polygone en joignant les sommets adjacents de la liste
    
    Remarque : le paramètre *args permet de saisir autant de tuples que l'on veut !
    
    Paramètres : plusieurs points sous forme de tuples;
    Attention ! ce n'est pas une liste mais plusieurs tuples séparés par des virgules
        
    Utise la fonction vecteur qui trace une ligne entre 2 points soit 2 tuples.
    Exemple : polygone((0,0),(100,0),(50,100)) trace un triangle
    """
    for i in range(len(args)-1):
        vecteur(args[i],args[i+1])
    # on trace le dernier côté qui joint les points extrême de la liste
    vecteur(args[-1],args[0])


if __name__ == '__main__':
    """
    points=[(randint(-200,200),randint(-200,200)) for _ in range(20)]
    # si on crée une liste de points, on passe en arguments *points
    turtle.begin_fill()
    polygone(*points)
    turtle.end_fill()
    """
    # côté du carré initial (au centre de la figure)
    c=10
    # centre du carré et de la figure
    x=c//2
    y=c//2
    for i in range(6):
        # on trace les carrés 0, 2, 4, ... de numéros pairs
        polygone((x-c//2,y-c//2),
                 (x+c//2,y-c//2),
                 (x+c//2,y+c//2),
                 (x-c//2,y+c//2))
        # on trace les carrés 1, 3, 5, ... de numéros impairs
        polygone((x,y-c),
                 (x+c,y),
                 (x,y+c),
                 (x-c,y))
        # on agrandit la mesure du côté du carré
        c = 2*c
    