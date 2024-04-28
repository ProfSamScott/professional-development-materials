"""Solution to 3b: classify grade. This is not the 
only way to do it. How many other ways
can you think of? Sam Scott, January 2015"""
def classify_grade(score):
    if score >= 0 and score <= 100:
        if score >= 90:
            print("A+")
        elif score >= 80:
            print("A")
        elif score >= 70:
            print("B")
        elif score >= 60:
            print("C")
        elif score >= 50:
            print("D")
        else:
            print("F")
    else:
        print('ERROR: grade out of range')

mark = float(input('Enter your grade: '))
classify_grade(mark)