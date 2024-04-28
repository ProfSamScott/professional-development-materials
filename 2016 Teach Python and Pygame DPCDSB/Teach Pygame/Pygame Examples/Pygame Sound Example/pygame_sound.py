""" A quick demonstration of how to play a sound file in pygame. Note that
for this to work, the display has to be active.
Sam Scott, January 14, 2015"""
import pygame

# initialize the mixer and pygame
pygame.mixer.pre_init(44100, -16, 8, 512)
pygame.init()

# create a sound object (store it in a variable for later)
ping = pygame.mixer.Sound("pongblipgsharp5.wav")

# unless the display is open, you will not hear the sound
pygame.display.set_mode([100,100])

# play the sound
ping.play()

# exit the display
pygame.display.quit()