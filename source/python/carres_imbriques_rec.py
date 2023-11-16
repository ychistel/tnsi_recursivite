import turtle
from math import sqrt

def carre(cote):
    for _ in range(4):
        turtle.forward(cote)
        turtle.left(90)
        
def deplacer1(cote):
    x, y = turtle.position()
    turtle.up()
    turtle.goto(x-cote/2,y+cote/2)
    turtle.down()
    
def deplacer2(cote):
    x, y = turtle.position()
    turtle.up()
    turtle.goto(x,y-cote/2)
    turtle.down()

def affiche(n,cote):
    if n > 0:
        carre(cote)
        deplacer1(cote)
        cote = cote*sqrt(2)
        turtle.right(45)
        carre(cote)
        cote = cote*sqrt(2)
        deplacer2(cote)
        turtle.left(45)
        affiche(n-1,cote)
                        
if __name__ == '__main__':
    turtle.speed("fastest")
    affiche(10,2)
    turtle.up()
    turtle.home()
    turtle.ht()
