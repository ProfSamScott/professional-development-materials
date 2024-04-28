def is_triangle(a,b,c):
    """a,b,c are triangle lengths sorted in ascending order.
    Prints "yes" if the three lengths could represent a triangle, or
    "no" if they could not"""
    if a+b > c:
        print("no")
    else:
        print("yes")

def check_triangle():
    print("Enter three side lengths (integers in ascending order).")
    side1 = int(input())
    side2 = int(input())
    side3 = int(input())
    print("Is it a triangle?")
    is_triangle(side1,side2,side3)