"""A test to see if pygame is working properly.
All will be explained in the fullness of time.

Sam Scott, January 7, 2015"""

import pygame, time

pygame.init()
surface = pygame.display.set_mode([500,100])
font = pygame.font.SysFont("monospace",40)   
color = pygame.Color("white")
text = font.render("Hello, World!",True,color)
surface.blit(text, [0,0])              
pygame.display.flip()
time.sleep(5)
pygame.display.quit()