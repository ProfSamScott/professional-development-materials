"""A template for your PyGame programs.

Sam Scott, January 7, 2015"""

import pygame, time

def gridrow(num, x, y, size, color):
    if num > 0:
        rect = pygame.Rect(x, y, size, size)
        pygame.draw.rect(surface, color, rect, 1)
        pygame.display.flip()
        gridrow(num-1, x+size, y, size, color)

def grid(numrows, numcols, x, y, size, color):
    if numrows > 0:
        gridrow(numcols, x, y, size, color)
        grid(numrows-1, numcols, x, y+size, size, color)

def checkerboardrow(num, x, y, size, color, filled):
    if num > 0:
        rect = pygame.Rect(x, y, size, size)
        if filled:
            width = 1
        else:
            width = 0
        pygame.draw.rect(surface, color, rect, width)
        pygame.display.flip()
        checkerboardrow(num-1, x+size, y, size, color, not filled)

def checkerboard(numrows, numcols, x, y, size, color, filled=True):
    if numrows > 0:
        checkerboardrow(numcols, x, y, size, color, filled)
        checkerboard(numrows-1, numcols, x, y+size, size, color, not filled)

# initialize the pygame code
pygame.init()
# change the numbers below to specify a window size
surface = pygame.display.set_mode([800,450]) 

grid(8, 8, 50, 50, 30, pygame.Color("white"))
checkerboard(8, 8, 350, 50, 30, pygame.Color("red"))

# pause to get a look at what you've created
time.sleep(5)

# you need this line to close the display window when the program is finished
pygame.display.quit()