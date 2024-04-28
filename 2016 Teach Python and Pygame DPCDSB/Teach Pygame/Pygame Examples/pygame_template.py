"""A template for your PyGame programs.

Sam Scott, January 7, 2015"""

import pygame, time

# initialize the pygame code
pygame.init()
# change the numbers below to specify a window size
surface = pygame.display.set_mode([800,450]) 

# -----------------------------




# your pygame program goes here




# -----------------------------

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