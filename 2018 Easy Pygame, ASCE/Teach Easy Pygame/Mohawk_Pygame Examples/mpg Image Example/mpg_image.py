""" A quick demonstration of how to load and display an image in mohawk_pygame. 
Sam Scott, Mohawk College, February 21, 2018"""

import mohawk_pygame as mpg
import random

# initialize the pygame code
mpg.start(800,450) 

# STEP 1: Load the image and store it in a variable
img = mpg.load_image("boy-sprite.png")
for i in range(100):
    mpg.draw_image(img, random.randint(-400,800),random.randint(-300,450))
    mpg.pause(0.01)

# pause to get a look at what you've created
mpg.pause(5)

# you need this line to close the display window when the program is finished
mpg.exit()