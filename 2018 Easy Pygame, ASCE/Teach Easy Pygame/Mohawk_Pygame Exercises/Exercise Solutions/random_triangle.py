"""Solution to the random triangle exercise

Sam Scott, Mohawk College, February, 2018"""

import mohawk_pygame as mpg
import random, math

# constants
RADIUS = 100

# initialize the pygame code
mpg.start(2*RADIUS,2*RADIUS) 

# ANGLES
angle1 = random.randint(0,359)
angle2 = random.randint(0,359)
angle3 = random.randint(0,359)

# POINTS
x1 = round(RADIUS*math.cos(angle1) + RADIUS)
y1 = round(RADIUS*math.sin(angle1) + RADIUS)
x2 = round(RADIUS*math.cos(angle2) + RADIUS)
y2 = round(RADIUS*math.sin(angle2) + RADIUS)
x3 = round(RADIUS*math.cos(angle3) + RADIUS)
y3 = round(RADIUS*math.sin(angle3) + RADIUS)

# DRAW
mpg.set_background("black")
mpg.clear()
mpg.set_color("yellow")
mpg.draw_circle(RADIUS, RADIUS, RADIUS, 2)

mpg.set_color("white")
mpg.draw_line(x1, y1, x2, y2, 2)
mpg.draw_line(x3, y3, x2, y2, 2)
mpg.draw_line(x1, y1, x3, y3, 2)
mpg.draw_circle(x1, y1, 4)
mpg.draw_circle(x2, y2, 4)
mpg.draw_circle(x3, y3, 4)

# pause to get a look at what you've created
mpg.pause(5)

# you need this line to close the display window when the program is finished
mpg.exit()