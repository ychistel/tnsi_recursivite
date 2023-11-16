from turtle import *
from math import sqrt

# https://mathcurve.com/fractals/dragon/dragon.shtml

speed("fastest")

def dragon(n,l):
    
    if n == 1:
        forward(l)
        backward(l)
    else:
        left(45)
        color('red')
        dragon(n-1,l/sqrt(2))
        right(45)
        up()
        forward(l)
        left(135)
        down()
        color('blue')
        dragon(n-1,l/sqrt(2))
        left(45)
        up()
        forward(l)
        left(180)
        down()

dragon(3,200)