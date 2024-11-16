import turtle
import math

turtle.speed(10)

def set(x, y):
    turtle.home()
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    turtle.right(90)
def chx(x):
    turtle.home()
    turtle.forward(x)
def chy(y):
    turtle.home()
    turtle.left(90)
    turtle.forward(y)
    turtle.right(90)


n = 100
for k in range(100):
    set((k-50), math.comb(n,k))




