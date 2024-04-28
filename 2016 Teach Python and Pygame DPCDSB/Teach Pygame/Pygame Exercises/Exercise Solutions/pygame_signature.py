"""Solution to exercise 5 from the chapter 2 handout
Now with a pygame signature function.

Sam Scott, January 2015"""

def pygame_sig():
    import pygame, time
    pygame.init()
    surface = pygame.display.set_mode([600,100]) 
    
    bcolor = pygame.Color("black")
    tcolor = pygame.Color("red")
    font = pygame.font.SysFont("sans-serif", 100)
    text = font.render("Sam Made This!!!", True, tcolor)    
    surface.blit(text, [0,20])    
    pygame.display.flip()
    time.sleep(0.5)
    surface.fill(bcolor)
    pygame.display.flip()
    time.sleep(0.5)
    surface.blit(text, [0,20])    
    pygame.display.flip()
    time.sleep(0.5)
    surface.fill(bcolor)
    pygame.display.flip()
    time.sleep(0.5)
    surface.blit(text, [0,20])    
    pygame.display.flip()
    time.sleep(2)
    
    # you need this line to close the display window when the program is finished
    pygame.display.quit()

# START OF PROGRAM
pygame_sig()
print("Enter the first point (x and then y)")
x1=float(input())
y1=float(input())
print("Enter the second point (x and then y)")
x2=float(input())
y2=float(input())

distance = ((x2-x1)**2 + (y2-y1)**2)**0.5

print("The distance between the two points is ",distance,"units.")

pygame_sig()