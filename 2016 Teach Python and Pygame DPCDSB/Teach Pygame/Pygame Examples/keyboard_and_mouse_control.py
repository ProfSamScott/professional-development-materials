"""An example of simple keyboard and mouse control.

Note that detecting key and mouse button presses using the method shown
below has limitations. There is a possibility of missing key and button
presses that happen too quickly, and it does not allow you to check 
separately for up and down events (triggered when a key or button is
pressed and release respectively). 

The best way to process button and key presses is to retrieve the
individual events from the event queue using pygame.event.get() and then 
use a for loop to check each event and respond appropriately. 

For complete documentation see:
    http://www.pygame.org/docs/ref/mouse.html   ...for the mouse
    http://www.pygame.org/docs/ref/key.html     ...for the keyboard
    http://www.pygame.org/docs/ref/event.html   ...for events in general
    
Sam Scott, April 29, 2016"""

import pygame, time

pygame.init()
surface = pygame.display.set_mode([400,400]) 

# set up the colors
color2 = pygame.Color("royalblue")
color1 = color2
bcolor = pygame.Color("lightyellow")

# initial paddle positions
x1, y1 = 30, 180
x2, y2 = 360, 180

# game loop
while True:
    # check for quit event - DO THIS FIRST
    if pygame.event.peek(pygame.QUIT): 
        pygame.display.quit()
        quit()
    
    # get mouse position to set paddle 1 y
    mx, my = pygame.mouse.get_pos()
    y1 = my
    
    # check keyboard to update paddle 2 y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y2 = y2 - 10
    if keys[pygame.K_DOWN]:
        y2 = y2 + 10
        
    # check the mouse buttons to update paddle 1 color
    b1, b2, b3 = pygame.mouse.get_pressed()
    color1 = color2
    if b1:
        color1 = pygame.Color("darkred")
    if b2:
        color1 = pygame.Color("darkgreen")
    if b3:
        color1 = pygame.Color("darkgrey")
        
    # draw the screen
    surface.fill(bcolor)
    rect = pygame.Rect(x1, y1, 10, 40)
    pygame.draw.rect(surface, color1, rect)
    rect = pygame.Rect(x2, y2, 10, 40)
    pygame.draw.rect(surface, color2, rect)
    pygame.display.flip()
    
    # pause
    time.sleep(1/60)

pygame.display.quit()