import turtle as t

t.tracer(10,1)

for i in range(360):
 t.forward(1)
 t.right(1)


t.update()

for i in range(360):
 t.forward(i)
 t.right(1)
 
for i in range(360):
 t.forward(i)
 t.right(20)
 
 # Quadrant 1

t1 = t.Turtle()
t1.penup()
t1.goto(125, 125)
t1.pendown()
t1.circle(100)

# Quadrant 2

t2 = t.Turtle()
t2.penup()
t2.goto(-125, 125)
t2.pendown()
t2.circle(100, 270)

# Quadrant 3

t2 = t.Turtle()
t2.penup()
t2.goto(-125, -125)
t2.pendown()
t2.circle(100, 180)

# Quadrant 4

t3 = t.Turtle()
t3.penup()
t3.goto(125, -125)
t3.pendown()
t3.circle(100, 90)

t.tracer(10,1)

for i in range(360):
 t.circle(i,20)

t.update()

t.tracer(10,1)

t1=t.Turtle()
t2=t.Turtle()
t1.setheading(0) # Looks to the right
t2.setheading(180) # Looks to the right

for x in range(360):
 radius = x
 angle = 1
 t1.circle(radius,angle)
 t2.circle(radius,angle)

t.update()

t.tracer(10,1)

N = 10
angle = 1

turtles = []
for position in range(N):
  look_at = 360/N*position
  new = t.Turtle()
  new.setheading(look_at)
  turtles.append(new)

for radius in range(360):
  for my in turtles:
    my.circle(radius, angle)


t.update()