"""Solution to the random triangle exercise

Sam Scott, January 7, 2015"""

import pygame, time, random, math

# constants
RADIUS = 100

# initialize the pygame code
pygame.init()
# change the numbers below to specify a window size
surface = pygame.display.set_mode([2*RADIUS,2*RADIUS]) 

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
color = pygame.Color("yellow")
pygame.draw.circle(surface, color, [RADIUS,RADIUS], RADIUS, 2)

color = pygame.Color("white")
pygame.draw.line(surface, color, (x1, y1), (x2, y2), 2)
pygame.draw.line(surface, color, (x3, y3), (x2, y2), 2)
pygame.draw.line(surface, color, (x1, y1), (x3, y3), 2)
pygame.draw.circle(surface, color, (x1, y1), 4)
pygame.draw.circle(surface, color, (x2, y2), 4)
pygame.draw.circle(surface, color, (x3, y3), 4)

pygame.display.flip()

# pause to get a look at what you've created
time.sleep(5)

# you need this line to close the display window when the program is finished
pygame.display.quit()