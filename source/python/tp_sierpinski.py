from turtle import *

def arbre(n : int, longueur : int) :
    if n == 0:
        forward(longueur)
        backward(longueur)
    else :
        forward(longueur)
        left(30)
        arbre(n-1, 0.7*longueur)
        right (60)
        arbre(n-1, 0.7*longueur)
        left(30)
        backward(longueur)
        
def dessine_arbre(n,l):
    setheading(90)
    #t.hideturtle() # on cache la tortue
    speed(0) # on accélère la tortue
    up()
    goto(0,-250)
    down()
    arbre(n,l)
    hideturtle() # on cache la tortue

#dessine_flocon_van_koch(4,300)
#dessine_flocon_carre()
dessine_arbre(10,200)
exitonclick() # garde la fenêtre ouverte et se ferme au click