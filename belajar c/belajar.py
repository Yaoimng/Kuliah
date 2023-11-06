import turtle

# Set the background color
turtle.bgcolor("White")

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's shape
t.shape("turtle")

# Set the turtle's speed
t.speed(10)

# Set the turtle's pen color and width
t.pencolor("purple")
t.pensize(5)

# Draw the petals of the flower
for i in range(36):
  t.circle(100, 90)
  t.left(110)

# Draw the center of the flower
t.pencolor("yellow")
t.circle(20)

# Hide the turtle
t.hideturtle()

# Keep the window open until it is closed
turtle.mainloop()
