# on importe le module turtle
import turtle
# on grossit le trait
turtle.pensize(3)
# couleur de crayon en vert
turtle.pencolor("#00ff00")
turtle.fillcolor("red") # ou (255,0,0) ou #ff0000
# début du remplissage en couleur
turtle.begin_fill()
# dessin du carré
for _ in range(4):
    turtle.forward(100)
    turtle.left(90)
# fin de couleur de remplissage
turtle.end_fill()
