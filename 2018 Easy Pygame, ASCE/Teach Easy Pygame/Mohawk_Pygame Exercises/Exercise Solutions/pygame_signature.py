"""Solution to exercise 5 from the chapter 2 handout
Now with a pygame signature function.

Sam Scott, Mohawk College, February 2018"""

def pygame_sig():
    import mohawk_pygame as mpg
    mpg.start(600,100) 
    
    mpg.set_background("black")
    mpg.clear()
    mpg.set_color("red")
    mpg.set_font("sans-serif", 100)
    mpg.draw_text("Sam Made This!!!", 0, 20)    
    mpg.pause(0.5)
    mpg.clear()
    mpg.pause(0.5)
    mpg.draw_text("Sam Made This!!!", 0, 20)    
    mpg.pause(0.5)
    mpg.clear()
    mpg.pause(0.5)
    mpg.draw_text("Sam Made This!!!", 0, 20)    
    mpg.pause(2)
    
    # you need this line to close the display window when the program is finished
    mpg.pygame.display.quit()

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