"""Example Animation

Sam Scott, February, 2015"""

import pygame, time, random

# -----------------------------
# Constants
# -----------------------------
NUM_FLASHES = 5      # number of times to flash the opening text
EXPLODE_HEIGHT = 100 # the y coordinate where the rocket explodes
PARTICLE_SIZE = 5    # size of the explosion particles
NUM_EXPLOSIONS = 20  # number of explosions after the first one
MAX_SIZE = 50        # size of the explosions
WIDTH = 500
HEIGHT = 300

def clear_screen():
  """ Clears the screen """
  surface.fill(pygame.Color("black"))
  pygame.display.flip()

def flash_intro():
  """ Flashes the intro message """
  count = 0
  font = pygame.font.SysFont("monospace", 50)
  color = pygame.Color("white")
  while count < NUM_FLASHES:
    text = font.render("Fireworks!", True, color)
    surface.blit(text, [round(WIDTH/2-150), round(HEIGHT/2-50)])
    pygame.display.flip()
    time.sleep(0.5)
    clear_screen()
    time.sleep(0.5)
    count = count + 1

def rocket():
  """ Launches the rocket """
  y=HEIGHT
  while y>EXPLODE_HEIGHT:
    color = pygame.Color("blue")
    rect = pygame.Rect(round(WIDTH/2), y, 10, 30)
    pygame.draw.ellipse(surface, color, rect)
    pygame.display.flip()
    time.sleep(0.005)
    color = pygame.Color("black")
    rect = pygame.Rect(round(WIDTH/2), y, 10, 30)
    pygame.draw.ellipse(surface, color, rect)
    pygame.display.flip()
    y = y - 1

def explosion(x, y, red, green, blue):
  """ Animates an explosion centered at (x,y) using the given color """
  offSet = 0
  while offSet < MAX_SIZE: 
    color = pygame.Color(red, green, blue)
    rect = pygame.Rect(x+offSet, y+offSet, PARTICLE_SIZE, PARTICLE_SIZE)
    pygame.draw.ellipse(surface, color, rect)
    rect = pygame.Rect(x+offSet, y-offSet, PARTICLE_SIZE, PARTICLE_SIZE)
    pygame.draw.ellipse(surface, color, rect)
    rect = pygame.Rect(x-offSet, y+offSet, PARTICLE_SIZE, PARTICLE_SIZE)
    pygame.draw.ellipse(surface, color, rect)
    rect = pygame.Rect(x-offSet, y-offSet, PARTICLE_SIZE, PARTICLE_SIZE)
    pygame.draw.ellipse(surface, color, rect)
    rect = pygame.Rect(x, y+offSet, PARTICLE_SIZE, PARTICLE_SIZE)
    pygame.draw.ellipse(surface, color, rect)
    rect = pygame.Rect(x, y-offSet, PARTICLE_SIZE, PARTICLE_SIZE)
    pygame.draw.ellipse(surface, color, rect)
    rect = pygame.Rect(x+offSet, y, PARTICLE_SIZE, PARTICLE_SIZE)
    pygame.draw.ellipse(surface, color, rect)
    rect = pygame.Rect(x-offSet, y, PARTICLE_SIZE, PARTICLE_SIZE)
    pygame.draw.ellipse(surface, color, rect)
    pygame.display.flip()
    time.sleep(0.005)
    color = pygame.Color("black")
    rect = pygame.Rect(x+offSet, y+offSet, PARTICLE_SIZE, PARTICLE_SIZE)
    pygame.draw.ellipse(surface, color, rect)
    rect = pygame.Rect(x+offSet, y-offSet, PARTICLE_SIZE, PARTICLE_SIZE)
    pygame.draw.ellipse(surface, color, rect)
    rect = pygame.Rect(x-offSet, y+offSet, PARTICLE_SIZE, PARTICLE_SIZE)
    pygame.draw.ellipse(surface, color, rect)
    rect = pygame.Rect(x-offSet, y-offSet, PARTICLE_SIZE, PARTICLE_SIZE)
    pygame.draw.ellipse(surface, color, rect)
    rect = pygame.Rect(x, y+offSet, PARTICLE_SIZE, PARTICLE_SIZE)
    pygame.draw.ellipse(surface, color, rect)
    rect = pygame.Rect(x, y-offSet, PARTICLE_SIZE, PARTICLE_SIZE)
    pygame.draw.ellipse(surface, color, rect)
    rect = pygame.Rect(x+offSet, y, PARTICLE_SIZE, PARTICLE_SIZE)
    pygame.draw.ellipse(surface, color, rect)
    rect = pygame.Rect(x-offSet, y, PARTICLE_SIZE, PARTICLE_SIZE)
    pygame.draw.ellipse(surface, color, rect)
    pygame.display.flip()
  
    offSet = offSet + 1

# initialize the pygame code
pygame.init()
surface = pygame.display.set_mode([WIDTH,HEIGHT]) 

# The animation
flash_intro()
rocket()
explosion(round(WIDTH/2), EXPLODE_HEIGHT, 255, 0, 0)
time.sleep(2)

count=0
while count < NUM_EXPLOSIONS:
  x = random.randint(0,WIDTH)
  y = random.randint(0,HEIGHT)
  red = random.randint(127, 255)
  green = random.randint(127, 255)
  blue = random.randint(127, 255)
  explosion(x, y, red, green, blue)
  count = count + 1
  time.sleep(0.05)
time.sleep(2)

pygame.display.quit()