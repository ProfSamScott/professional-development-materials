"""Solution to exercise 3

Sam Scott, January 7, 2015"""

print("please enter the x and y locations")
x = int(input())
y = int(input())
print("Please enter a color name")
colorname = input()
print("Now enter the radius")
radius = int(input())

import mohawk_pygame as mpg

# initialize the pygame code
mpg.start(400,400) 

mpg.set_color(colorname)
mpg.draw_circle(x, y, radius)

# pause to get a look at what you've created
mpg.pause(5)

# you need this line to close the display window when the program is finished
mpg.exit()