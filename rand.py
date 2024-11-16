import turtle
import random
c = ['red', 'green', 'blue', 'yellow', 'violet', 'indigo', 'orange']
turtle.speed(10)
while True:
    turtle.color(c[random.randrange(0, len(c))])
    turtle.right(random.randrange(0,360))
    turtle.forward(random.randrange(10, 100))

