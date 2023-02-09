from turtle import *


# We want to draw a house

#step 1: draw a square

width(5)
color("green")
begin_fill()


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(60)
begin_fill()
color("grey")
left(90)
forward(100)
right(90)
forward(70)
right(90)
forward(100)
end_fill()

penup()
goto(200,200)
pendown()

color("purple")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of the roof

#drawing a left window
penup()
goto(10,120)
pendown()

color("yellow")
begin_fill()
left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#drawing a right window
penup()
goto(190,120)
pendown()

begin_fill()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
















exitonclick()

