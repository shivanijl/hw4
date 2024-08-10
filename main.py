# Import the Pygame Zero Library
import pgzrun
from random import randint

# Pygame Standard for deciding the title of your game window
TITLE = "Catch"
# Pygame Standard for deciding the width and height for your game window in pixels
WIDTH = 500
HEIGHT = 500

# variable to store the message displayed on your screen
message = ""

# Actor is built-in object in pgzero
# interacts with other actors, move around on screen
# Similar to Sprite in Scratch
ufo = Actor('ufo')
#alien.pos = 50,50

# Default function which will be called to update the screen
def draw():
  # screen is another built-in object
  screen.clear()
  screen.fill(color = (0, 0, 128))
#  place_alien()
  ufo.draw()
  screen.draw.text(message, center = (400, 10), fontsize= 30)

def place_alien():
    ufo.x = randint(50, WIDTH-50)
    ufo.y = randint(50, WIDTH-50)

def on_mouse_down(pos):
  #print("Hello World")
    global message
    if ufo.collidepoint(pos):
        message = "Catch"
        place_alien()
    else:
        message = "You missed"

# This method needs to be called to start processing
place_alien()
pgzrun.go()