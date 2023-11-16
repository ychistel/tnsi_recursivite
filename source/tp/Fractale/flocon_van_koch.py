import turtle as t

def courbe_van_koch(n,l):
    if n==0:
        t.forward(l)
    else:
        courbe_van_koch(n-1,l/3)
        t.left(60)
        courbe_van_koch(n-1,l/3)
        t.right(120)
        courbe_van_koch(n-1,l/3)
        t.left(60)
        courbe_van_koch(n-1,l/3)

def flocon(n,l):
    for _ in range(3):
        courbe_van_koch(n,l)
        t.right(120)


def dessine_flocon_van_koch(n,l):
    # On initialise les paramètres de la tortue
    t.setheading(0) # on oriente le tete de tortue vers la droite
    t.hideturtle() # on cache la tortue
    t.speed(0) # on accélère la tortue
    t.up()
    t.goto(-150,150)
    t.setheading(0)
    t.down()
    flocon(n,l)
    t.exitonclick() # garde la fenêtre ouverte et se ferme au click

n=int(input("Niveau de récursivité : "))
dessine_flocon_van_koch(n,300)