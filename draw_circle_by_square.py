import turtle

def draw_square(some_turtle):
    for turtle in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
     #create turtle brad - Draws the square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(4)
    for i in range(36):
        draw_square(brad)
        brad.right(10)

    #create turtle angie- Draws the circle
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.circle(100)
    #angie.color("blue")
    
    window.exitonclick()

draw_art()
