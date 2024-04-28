"""Example Animation using mohawk_pygame.py

Sam Scott, Mohawk College, February, 2018"""

import mohawk_pygame as mpg
import random

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

def flash_intro():
  """ Flashes the intro message """
  count = 0
  mpg.set_font("monospace", 50)
  mpg.set_color("white")
  while count < NUM_FLASHES:
    mpg.draw_text("Fireworks!", round(WIDTH/2-150), round(HEIGHT/2-50))
    mpg.pause(0.5)
    mpg.clear()
    mpg.pause(0.5)
    count = count + 1

def rocket():
  """ Launches the rocket """
  y=HEIGHT
  mpg.set_color("blue")
  while y>EXPLODE_HEIGHT:
    mpg.draw_ellipse(round(WIDTH/2), y, 10, 30)
    mpg.pause(0.005)
    mpg.clear()
    y = y - 1

def explosion(x, y, red, green, blue):
  """ Animates an explosion centered at (x,y) using the given color """
  offSet = 0
  mpg.set_rgb(red, green, blue)
  while offSet < MAX_SIZE: 
    mpg.draw_ellipse(x+offSet, y+offSet, PARTICLE_SIZE, PARTICLE_SIZE)
    mpg.draw_ellipse(x+offSet, y-offSet, PARTICLE_SIZE, PARTICLE_SIZE)
    mpg.draw_ellipse(x-offSet, y+offSet, PARTICLE_SIZE, PARTICLE_SIZE)
    mpg.draw_ellipse(x-offSet, y-offSet, PARTICLE_SIZE, PARTICLE_SIZE)
    mpg.draw_ellipse(x, y+offSet, PARTICLE_SIZE, PARTICLE_SIZE)
    mpg.draw_ellipse(x, y-offSet, PARTICLE_SIZE, PARTICLE_SIZE)
    mpg.draw_ellipse(x+offSet, y, PARTICLE_SIZE, PARTICLE_SIZE)
    mpg.draw_ellipse(x-offSet, y, PARTICLE_SIZE, PARTICLE_SIZE)
    mpg.pause(0.005)
    mpg.clear()
    offSet = offSet + 1

# initialize the pygame code
mpg.start(WIDTH, HEIGHT)

# The animation
mpg.set_background("black")
mpg.clear()
flash_intro()
rocket()
explosion(round(WIDTH/2), EXPLODE_HEIGHT, 255, 0, 0)
mpg.pause(2)

count=0
while count < NUM_EXPLOSIONS:
  x = random.randint(0,WIDTH)
  y = random.randint(0,HEIGHT)
  red = random.randint(127, 255)
  green = random.randint(127, 255)
  blue = random.randint(127, 255)
  explosion(x, y, red, green, blue)
  count = count + 1
  mpg.pause(0.05)
  
mpg.pause(2)
mpg.exit()