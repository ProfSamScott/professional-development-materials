"""A template for your PyGame programs.

Sam Scott, January 7, 2015"""

import pygame, time

# initialize the pygame code
pygame.init()
# change the numbers below to specify a window size
surface = pygame.display.set_mode([800,450]) 

x = 1
while x <= 800:
    # draw the shape
    color = pygame.Color("white")
    rect = pygame.Rect(x, 100, 30, 30)
    pygame.draw.rect(surface, color, rect, 5)
    pygame.display.flip()
    
    # pause
    time.sleep(1/60)
    
    # erase the shape
    color = pygame.Color("black")
    pygame.draw.rect(surface, color, rect, 5)
    
    # update animation variables
    x = x + 1
    
    if pygame.event.peek(pygame.QUIT):
        pygame.display.quit()
        quit()

# pause to get a look at what you've created
time.sleep(5)

# you need this line to close the display window when the program is finished
pygame.display.quit()
