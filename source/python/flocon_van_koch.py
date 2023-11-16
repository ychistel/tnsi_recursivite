from turtle import *

def courbe_van_koch(n,l):
    if n==0:
        forward(l)
    else:
        courbe_van_koch(n-1,l/3)
        left(60)
        courbe_van_koch(n-1,l/3)
        right(120)
        courbe_van_koch(n-1,l/3)
        left(60)
        courbe_van_koch(n-1,l/3)

def flocon(n,l):
    for _ in range(3):
        courbe_van_koch(n,l)
        right(120)


def dessine_flocon_van_koch(n,l):
    # On initialise les paramètres de la tortue
    setheading(0) # on oriente le tete de tortue vers la droite
    hideturtle() # on cache la tortue
    speed(0) # on accélère la tortue
    up()
    goto(-150,150)
    setheading(0)
    down()
    flocon(n,l)
    exitonclick() # garde la fenêtre ouverte et se ferme au click

n=int(input("Niveau de récursivité : "))
dessine_flocon_van_koch(n,300)