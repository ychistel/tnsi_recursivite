import turtle as t

# Fonction avec angle +90:

def dragon90(n,c):
    if t==0:
        t.forward(10)
    else:
        dragon90(n-1)
        t.right(90)
        dragon90(n-1)

def dragon(n,s):
    if n==0:
        forward(10)
    else:
        dragon(n-1,-1)
        t.right(s*90)
        dragon(n-1,1)

def triangle(l):
    for _ in range(3):
        t.forward(l)
        t.right(120)

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


def carre_van_koch(n,l):
    if n==0:
        t.forward(l)
    else:
        carre_van_koch(n-1,l/3)
        t.left(90)
        carre_van_koch(n-1,l/3)
        t.right(90)
        carre_van_koch(n-1,l/3)
        t.right(90)
        carre_van_koch(n-1,l/3)
        t.left(90)
        carre_van_koch(n-1,l/3)

def flocon_carre(n,l):
    for _ in range(4):
        carre_van_koch(n,l)
        t.right(90)

def arbre(n : int, longueur : int) :
    # global cpt
    """
    cette procedure dessine un 'arbre' a d'ordre n
    """
    if n == 0:
        t.forward(longueur)
        t.backward(longueur)
    else :
        t.forward(longueur)
        t.left(30)
        #cpt += 1
        # print(cpt)
        arbre(n-1, longueur)
        t.right (60)
        #cpt += 1
        # print(cpt)
        arbre(n-1, longueur)
        t.left(30)
        t.backward(longueur)

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

def dessine_flocon_carre(n=0):
    # On initialise les paramètres de la tortue
    t.setheading(0) # on oriente le tete de tortue vers la droite
    t.hideturtle() # on cache la tortue
    t.speed(0) # on accélère la tortue
    t.up()
    t.goto(-150,150)
    t.setheading(0)
    t.down()
    if n==0:
        for i in range(5):
            flocon_carre(i,300)
    else:
        flocon_carre(n,300)

def dessine_arbre(n,l):
    t.setheading(90)
    #t.hideturtle() # on cache la tortue
    #t.speed(0) # on accélère la tortue
    t.up()
    t.goto(0,-250)
    t.down()
    arbre(n,l)

#dessine_flocon_van_koch(4,300)
#dessine_flocon_carre()
dessine_arbre(5,100)
t.exitonclick() # garde la fenêtre ouverte et se ferme au click