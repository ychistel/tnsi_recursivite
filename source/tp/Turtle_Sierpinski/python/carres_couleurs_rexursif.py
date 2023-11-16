import turtle
from random import randint

turtle.colormode(255)
turtle.speed("fastest")

def dessiner(n,ecart):
    if n > 0:
        couleur=(randint(0,255),randint(0,255),randint(0,255))
        turtle.fillcolor(couleur) # ou (255,0,0) ou #ff0000
        # début de couleur de remplissage
        turtle.begin_fill()
        # dessin du carré
        for _ in range(4):
            turtle.forward(n*ecart)
            turtle.left(90)
        # fin de couleur de remplissage
        turtle.end_fill()
        dessiner(n-1,ecart)
        
if __name__ == '__main__':
    dessiner(25,10)    
    turtle.ht()
