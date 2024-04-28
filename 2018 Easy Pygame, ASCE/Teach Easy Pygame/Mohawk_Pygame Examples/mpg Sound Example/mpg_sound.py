""" A quick demonstration of how to play a sound file in mohawk_pygame. 
Sam Scott, February 21, 2018"""
import mohawk_pygame as mpg

# initialize the pygame code
mpg.start(100,100) 

# create a sound object (store it in a variable for later)
ping = mpg.load_sound("pongblipgsharp5.wav")

# play the sound
ping.play()

mpg.pause(5)
# exit the display
mpg.exit()