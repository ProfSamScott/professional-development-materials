"""Solution to exercise 4.

Actually, it turns out you have to change the float
radius to an integer using int(). Sorry about that.

Sam Scott, January 7, 2015"""

print("please enter the x and y locations")
x = int(input())
y = int(input())
print("Please enter a color name")
colorname = input()
print("Now enter the area")
area = float(input())
radius = (area/3.14159)**0.5

import pygame, time

# initialize the pygame code
pygame.init()
# change the numbers below to specify a window size
surface = pygame.display.set_mode([400,400]) 

color = pygame.Color(colorname)
pygame.draw.circle(surface, color, [x,y], int(radius))
pygame.display.flip()

# pause to get a look at what you've created
time.sleep(5)

# you need this line to close the display window when the program is finished
pygame.display.quit()