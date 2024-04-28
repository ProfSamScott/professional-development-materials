"""An example of simple keyboard and mouse control using mohawk_pygame.

Notice the use of flip=False to reduce screen flicker and speed up the game.
    
Sam Scott, Mohawk College, February, 2018"""

import mohawk_pygame as mpg

mpg.start(400,400) 

# set up the colors
color2 = "royalblue"
color1 = color2
mpg.set_background("lightyellow")

# initial paddle positions
x1, y1 = 30, 180
x2, y2 = 360, 180

# game loop
while True:      
    # get mouse position to set paddle 1 y
    mx, my = mpg.get_mouse_pos()
    y1 = my
    
    # check keyboard to update paddle 2 y
    if mpg.is_key_down(mpg.UP):
        y2 = y2 - 10
    if mpg.is_key_down(mpg.DOWN):
        y2 = y2 + 10
        
    # check the mouse buttons to update paddle 1 color
    color1 = color2
    if mpg.is_button_down(1):
        color1 = "darkred"
    if mpg.is_button_down(2):
        color1 = "darkgreen"
    if mpg.is_button_down(3):
        color1 = "darkgrey"
        
    # draw the screen
    mpg.clear(flip=False)
    mpg.set_color(color1)
    mpg.draw_rectangle(x1, y1, 10, 40, flip=False)
    mpg.set_color(color2)
    mpg.draw_rectangle(x2, y2, 10, 40, flip=False)
    mpg.flip()
    
    # pause
    mpg.pause(1/60)

mpg.exit()