"""Solution to exception handling exercise on quadratic equations
Sam Scott, February 2015"""

def roots(a, b, c):
    """Displays the roots of a quadratic equation, given
    a, b and c, where ax**2+bx+c = 0
    Catches division by zero errors"""
    discriminant = (b**2-4*a*c)
    try:
        if discriminant > 0:
            r1 = (-b+discriminant**0.5)/(2*a)
            r2 = (-b-discriminant**0.5)/(2*a)
            print("The roots are:",r1,"and",r2)
        elif discriminant == 0:
            r = (-b+discriminant**0.5)/(2*a)
            print("The root is:",r)
        else:
            print("This equation has no roots")
    except:
        print("This is not a quadratic equation, because a is 0")

def main():
    """The user interface for roots(). Catches and handles user errors."""
    print("Enter a, b and c")
    
    ok = True # will be set to false if the user enters non-ints
    
    try:
        a = float(input())
    except:
        a = 0
        ok = False
        
    try:
        b = float(input())
    except:
        b = 0
        ok = False
        
    try:
        c = float(input())
    except:
        c = 0
        ok = False
        
    if not ok: # did something go wrong?
        print("WARNING: Non-numeric values converted to 0.")
        
    roots(a,b,c) # call the roots function

# call main
main()
