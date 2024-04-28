"""Solution to 1a: groovy. Flow chart and test cases
not included. Sam Scott, 2015"""
n = float(input('Gimme a number: '))
if n % 13 == 0 or (n % 2 == 0 and n > 10):
    print("That number is groovy")
else:
    print("That number is not groovy :-(")