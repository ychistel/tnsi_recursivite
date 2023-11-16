import turtle

couleur=["red","white"]

if __name__ == '__main__':
    turtle.setup()
    n = 7
    ecart = 20
    for i in range(n):
        rayon = (n-i)*ecart
        turtle.up()
        turtle.goto(0, -rayon)
        turtle.down()
        turtle.fillcolor(couleur[i % 2])
        turtle.begin_fill()
        turtle.circle(rayon)
        turtle.end_fill()
        rayon -= ecart  #Augmente la valeur de rayon
    turtle.up()
    turtle.home()
    turtle.ht()
    turtle.exitonclick()