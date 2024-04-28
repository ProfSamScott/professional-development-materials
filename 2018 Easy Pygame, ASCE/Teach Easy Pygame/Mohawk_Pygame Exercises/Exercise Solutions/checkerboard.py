"""
Sam Scott, Mohawk College, February, 2018"""

import mohawk_pygame as mpg

def gridrow(num, x, y, size, color):
    mpg.set_color(color)
    if num > 0:
        mpg.draw_rectangle(x, y, size, size, 1)
        gridrow(num-1, x+size, y, size, color)

def grid(numrows, numcols, x, y, size, color):
    if numrows > 0:
        gridrow(numcols, x, y, size, color)
        grid(numrows-1, numcols, x, y+size, size, color)

def checkerboardrow(num, x, y, size, color, filled):
    mpg.set_color(color)
    if num > 0:
        if filled:
            width = 1
        else:
            width = 0
        mpg.draw_rectangle(x, y, size, size, width)
        checkerboardrow(num-1, x+size, y, size, color, not filled)

def checkerboard(numrows, numcols, x, y, size, color, filled=True):
    if numrows > 0:
        checkerboardrow(numcols, x, y, size, color, filled)
        checkerboard(numrows-1, numcols, x, y+size, size, color, not filled)

# initialize the pygame code
mpg.start(800,450) 
mpg.set_background("black")
mpg.clear()

grid(8, 8, 50, 50, 30, "white")
checkerboard(8, 8, 350, 50, 30, "red")

# pause to get a look at what you've created
mpg.pause(5)

# you need this line to close the display window when the program is finished
mpg.exit()