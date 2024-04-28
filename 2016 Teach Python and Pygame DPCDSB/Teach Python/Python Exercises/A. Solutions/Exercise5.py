"""Solution to exercise 5 from the chapter 2 handout
Sam Scott, January 2015"""

print("Enter the first point (x and then y)")
x1=float(input())
y1=float(input())
print("Enter the second point (x and then y)")
x2=float(input())
y2=float(input())

distance = ((x2-x1)**2 + (y2-y1)**2)**0.5

print("The distance between the two points is ",distance,"units.")