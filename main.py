import turtle

screen=turtle.Screen()
screen.bgcolor("pink")

olympic_rings =turtle.Turtle()
olympic_rings.speed(5)

radius=35

olympic_rings.penup()
olympic_rings.goto(-80,15)
olympic_rings.pendown()
olympic_rings.pencolor("blue")
olympic_rings.circle(35)

olympic_rings.penup()
olympic_rings.goto(0,15)
olympic_rings.pendown()
olympic_rings.pencolor("yellow")
olympic_rings.circle(35)

olympic_rings.penup()
olympic_rings.goto(80,15)
olympic_rings.pendown()
olympic_rings.pencolor("black")
olympic_rings.circle(35)

olympic_rings.penup()
olympic_rings.goto(-40,-20)
olympic_rings.pendown()
olympic_rings.pencolor("green")
olympic_rings.circle(35)

olympic_rings.penup()
olympic_rings.goto(40,-20)
olympic_rings.pendown()
olympic_rings.pencolor("red")
olympic_rings.circle(35)
olympic_rings.pencolor("purple")
olympic_rings.write("Winter Olympics",font=("Ariel",24, "bold"),align="center")
olympic_rings.write("2026",font=("Ariel",24, "bold"),align="center")


turtle.done()