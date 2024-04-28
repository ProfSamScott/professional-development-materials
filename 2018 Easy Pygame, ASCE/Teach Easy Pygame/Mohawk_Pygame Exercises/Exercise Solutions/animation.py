"""
Sam Scott, Mohawk College, February, 2018"""

import mohawk_pygame as mpg

# initialize the pygame code
mpg.start(800,450) 

mpg.set_color("white")
mpg.set_background("black")
mpg.clear()

x = 1
while x <= 800:
    # draw the shape
    mpg.draw_rectangle(x, 100, 30, 30, 5, flip=False)
    mpg.flip()
    
    # pause
    mpg.pause(1/60)
    
    # erase the shape
    mpg.clear(flip=False)
    
    # update animation variables
    x = x + 1
    
# pause to get a look at what you've created
mpg.pause(5)

# you need this line to close the display window when the program is finished
mpg.exit()
