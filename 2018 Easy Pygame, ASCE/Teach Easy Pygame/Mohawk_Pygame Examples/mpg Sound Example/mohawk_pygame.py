import pygame, time

"""MOHAWK PYGAME 1.0
Created by Sam Scott (Mohawk College), February 21, 2018

Introduced at ACSE 2018

The purpose of this module is to create an easier interface for beginner
programmers to create drawings, animations, and games in a purely imperative 
style (i.e. no event handling). 

To use the module, include it in the same folder as your pygame program, then 
use the following import line:

import mohawk_pygame as mpg

Then use mpg.start(width, height) to open the pygame window and mpg.exit() to 
quit.

See the handout for other commands
"""
def start(width, height):
    """ Creates the surface and initializes colors and fonts"""
    global surface
    pygame.mixer.pre_init(44100, -16, 8, 512)
    pygame.init()
    surface = pygame.display.set_mode([width,height], pygame.DOUBLEBUF) 
    set_color("black")
    set_font("monospace", 20)
    set_background("lightyellow")
    clear()
    
def set_color(colorname):
    """Sets the current drawing color."""
    global color
    color = pygame.Color(colorname)

def set_rgb(red, green, blue):
    global color
    color = pygame.Color(red, green, blue)
    
def set_background(colorname):
    """Sets the background color, used when the clear function is called"""
    global background
    background = pygame.Color(colorname)

def set_background_rgb(red, green ,blue):
    """Sets the background color, used when the clear function is called"""
    global background
    background = pygame.Color(red, green, blue)

def set_font(name, size, bold=False, italic=False):
    """Sets the current font"""
    global font
    font = pygame.font.SysFont(name, size, bold, italic)
    
def draw_rectangle(x, y, width, height, line=0, flip=True):
    """Draws a rectangle on the screen"""
    global color, surface
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(surface, color, rect, line)
    if flip:
        pygame.display.flip()
    
def draw_ellipse(x, y, width, height, line=0, flip=True):
    """Draws an ellipse on the screen inside the bounding box defined by
    x, y, width and height."""
    global color, surface
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.ellipse(surface, color, rect, line)
    if flip:
        pygame.display.flip()

def draw_circle(x, y, radius, line=0, flip=True):
    """Draws a circle on the screen. x and y specify the center of the circle"""
    global color, surface
    pygame.draw.circle(surface, color, [x,y], radius, line)
    if flip:
        pygame.display.flip()

def draw_line(x1, y1, x2, y2, line=1, flip=True):
    """Draws a line from x1, y1 to x2, y2"""
    global color, surface
    pygame.draw.line(surface, color, (x1,y1), (x2, y2), line)
    if flip:
        pygame.display.flip()

def clear(flip=True):
    """Clears the screen using the current background color"""
    global background, surface
    surface.fill(background)
    if flip:
        pygame.display.flip()

def draw_text(message, x, y, flip=True):
    """Draws a message on the screen"""
    global color, surface, font
    text = font.render(message, True, color)
    surface.blit(text, (x,y))
    if flip:
        pygame.display.flip()

def load_image(name):
    """Loads an image and returns it"""
    return pygame.image.load(name)

def draw_image(image, x, y, flip=True):
    """Draws an image on the screen. Don't forget to load it first!"""
    global surface
    surface.blit(image, (x,y))
    if flip:
        pygame.display.flip()

def load_sound(name):
    """Loads a sound and returns it"""
    return pygame.mixer.Sound(name)

def draw_image(image, x, y, flip=True):
    """Draws an image on the screen. Don't forget to load it first!"""
    global surface
    surface.blit(image, (x,y))
    if flip:
        pygame.display.flip()
        
def get_mouse_pos():
    """Returns the current x and y location of the mouse"""
    quit_check()
    return pygame.mouse.get_pos()

def is_button_down(buttonNum):
    """buttonNum must be 1, 2, or 3. Returns True or False to indicate whether
    the button is currently down or not"""
    quit_check()
    return pygame.mouse.get_pressed()[buttonNum-1]

LEFT = pygame.K_LEFT
RIGHT = pygame.K_RIGHT
UP = pygame.K_UP
DOWN = pygame.K_DOWN
RSHIFT = pygame.K_RSHIFT
LSHIFT = pygame.K_LSHIFT
RALT = pygame.K_RALT
LALT = pygame.K_LALT

def is_key_down(key):
    """Returns true or false to indicate whether or not the given key is pressed.
    key can be a string of length 1 or one of mpg.LEFT, mpg.RIGHT, mpg.UP,
    mpg.DOWN, mpg.RSHIFT, mpg.LSHIFT, mpg.RALT or mpg.LALT"""
    quit_check()
    if type(key) is str:
        key = ord(key[0].lower())
    return pygame.key.get_pressed()[key]
    
def flip():
    """Advanced. If you want to control when the screen is updated, to avoid
    flickering during an animation, use flip=False on all your drawing commands
    and call this flip() function only once for each iteration of your animation
    loop"""
    pygame.display.flip()
    
def quit_check():
    """Advanced. If you are not using the pause function for your animation,
    you should call this function once for each iteration of your animation 
    loop"""
    if pygame.event.peek(pygame.QUIT):
        exit()

def pause(numSeconds):
    """Pauses the action and keeps the window alive while it's paused."""
    endtime = time.time() + numSeconds
    if numSeconds > 0.1:
        while time.time() < endtime: 
            quit_check()
            time.sleep(0.1)
    else:
        quit_check()
        time.sleep(max(0.00001,endtime-time.time()))

def exit():
    """Call this to exit"""
    pygame.display.quit()
    quit()