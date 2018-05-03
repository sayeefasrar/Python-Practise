import turtle
def draw_square():
    window = turtle.Screen()
    window.bgcolor("green")
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(2)
    count=0
    while (count<=3):
        brad.forward(100)
        brad.right(90)
        
        count=count+1
        for i in range (1,37):
            draw_square(brad)
            brad.right(10)
    #anie= turtle.Turtle()
    #anie.shape("arrow")
    #anie.color("brown")
    #anie.circle(100)
    #window.exitonclick()

draw_square()
