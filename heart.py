import turtle
screen = turtle.Screen()
screen.bgcolor("black")
heart = turtle.Turtle()
heart.fillcolor("maroon")
heart.pensize(2)
heart.pencolor("white")
heart.speed(100)
heart.penup()
heart.goto(0, -200)
heart.pendown()
heart.begin_fill()
heart.left(140)
heart.forward(224)
for _ in range(200):
    heart.right(1)
    heart.forward(2)
heart.left(120)
for _ in range(200):
    heart.right(1)
    heart.forward(2)
heart.forward(224)
heart.end_fill()
heart.hideturtle()
screen.exitonclick()
