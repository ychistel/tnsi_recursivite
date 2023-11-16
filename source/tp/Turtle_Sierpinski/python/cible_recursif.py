import turtle

couleur=["red","white"]

def dessiner(n,ecart):
    if n > 0:
        rayon = n*ecart
        turtle.up()
        turtle.goto(0, -rayon)
        turtle.down()
        turtle.fillcolor(couleur[n % 2])
        turtle.begin_fill()
        turtle.circle(rayon)
        turtle.end_fill()
        dessiner(n-1,ecart)
    
if __name__ == '__main__':
    turtle.setup()
    dessiner(8,20)
    turtle.up()
    turtle.home()
    turtle.ht()
    turtle.exitonclick()