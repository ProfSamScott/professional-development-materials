""" A quick demonstration of how to load and display an image in pygame. 
Sam Scott, April 28, 2016"""

import pygame, time, random

# initialize the pygame code
pygame.init()
# change the numbers below to specify a window size
surface = pygame.display.set_mode([800,450]) 

# STEP 1: Load the image and store it in a variable
img = pygame.image.load("boy-sprite.png")
for i in range(100):
    # STEP 2: "Blit" the image onto the display
    surface.blit(img, [random.randint(-400,800),random.randint(-300,450)])
    time.sleep(0.01)
    if pygame.event.peek(pygame.QUIT): 
        pygame.display.quit()
        quit()
    # STEP 3: Flip the display
    pygame.display.flip()

# pause to get a look at what you've created
pausetime = 5
endtime = time.time() + pausetime
while time.time() < endtime: 
    if pygame.event.peek(pygame.QUIT): 
        pygame.display.quit()
        quit()
    time.sleep(0.5)

# you need this line to close the display window when the program is finished
pygame.display.quit()