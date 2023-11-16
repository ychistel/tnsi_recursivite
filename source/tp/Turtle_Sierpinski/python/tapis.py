import turtle

def carre(x,y,cote,color="black"):
    deplacer(x,y)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(cote)
        turtle.left(90)
    turtle.end_fill()
    
def deplacer(x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()

def motif_tapis(x,y,cote):
    carre(x,y,cote)
    carre(x+cote//3,y+cote//3,cote//3,"white")
    
def tapisser(n,x,y,cote):
    if n==1:
        motif_tapis(x,y,cote)
    else:
        tapisser(n-1,x,y,cote//3)
        tapisser(n-1,x+cote//3,y,cote//3)
        tapisser(n-1,x+2*cote//3,y,cote//3)
        tapisser(n-1,x,y+cote//3,cote//3)
        tapisser(n-1,x+2*cote//3,y+cote//3,cote//3)
        tapisser(n-1,x,y+2*cote//3,cote//3)
        tapisser(n-1,x+cote//3,y+2*cote//3,cote//3)
        tapisser(n-1,x+2*cote//3,y+2*cote//3,cote//3)
        
    
if __name__ == '__main__':
    #turtle.setup()
    turtle.setup(width=600,height=600,startx=0,starty=0)
    turtle.speed("fastest")
    tapisser(3,-200,-200,360)
    turtle.hideturtle()
    