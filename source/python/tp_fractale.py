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
        t.forward(10)
    else:
        dragon(n-1,-1)
        t.right(s*90)
        dragon(n-1,1)

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
    t.exitonclick() # garde la fenêtre ouverte et se ferme au click

def arbre(n : int, longueur : int) :
    global cpt
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
    t.exitonclick() # garde la fenêtre ouverte et se ferme au click

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
        t.exitonclick() # garde la fenêtre ouverte et se ferme au click
    else:
        flocon_carre(n,300)
        t.exitonclick() # garde la fenêtre ouverte et se ferme au click
    
def dessine_arbre(n,l):
    t.setheading(90)
    #t.hideturtle() # on cache la tortue
    #t.speed(0) # on accélère la tortue
    t.up()
    t.goto(0,-250)
    t.down()
    arbre(n,l)
    t.exitonclick() # garde la fenêtre ouverte et se ferme au click

while True:
    print("Pour dessiner la fractale dragon, taper 1")
    print("Pour dessiner la fractale courbe de Van Koch, taper 2")
    print("Pour dessiner la fractale flocon de Van Koch, taper 3")
    print("Pour dessiner la fractale flocon carre de Van Koch, taper 4")
    print("Pour dessiner la fractale superposée des flocons carrés, taper 5")
    print("Pour dessiner la fractale arbre, taper 6")
    rep=input("Taper votre choix : ")
    if rep=="1":
        dragon(8,1)
    elif rep=="2":
        courbe_van_koch(2,60)
    elif rep=="3":
        dessine_flocon_van_koch(4,300)
    elif rep=="4":
        dessine_flocon_carre(3)
    elif rep=="5":
        dessine_flocon_carre()
    elif rep=="6":
        dessine_arbre(5,100)
    else:
        break

