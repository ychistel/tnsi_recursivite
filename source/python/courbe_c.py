from turtle import *
from math import sqrt

# https://mathcurve.com/fractals/dragon/dragon.shtml

#speed("fastest")

def courbe_c(n,l):
    
    if n == 1:
        forward(l)
    else:
        left(45)
        courbe_c(n-1,l/sqrt(2))
        right(90)
        courbe_c(n-1,l/sqrt(2))
        """
        right(135)
        up()
        forward(l)
        left(180)
        down()
        """
courbe_c(3,200)