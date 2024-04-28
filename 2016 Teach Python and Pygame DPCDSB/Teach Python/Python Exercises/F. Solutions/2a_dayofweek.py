"""Solution to 2a: day of week. Flow chart and test cases
not included. Sam Scott, 2015"""
def dayofweek(daystring, increment):
    daynum = -1
    if daystring == "Sunday":
        daynum = 0
    elif daystring == "Monday":
        daynum = 1
    elif daystring == "Tuesday":
        daynum = 2
    elif daystring == "Wednesday":
        daynum = 3   
    elif daystring == "Thursday":
        daynum = 4    
    elif daystring == "Friday":
        daynum = 5                
    elif daystring == "Saturday":
        daynum = 6 
    newday = (daynum + increment) % 7
    print ('Today is',daystring,'and the future day is ',end='')
    if newday == 0:
        print('Sunday')
    elif newday == 1:
        print('Monday')
    elif newday == 2:
        print('Tuesday')
    elif newday == 3:
        print('Wednesday')
    elif newday == 4:
        print('Thursday')
    elif newday == 5:
        print('Friday')
    elif newday == 6:
        print('Saturday')

d = input("Enter today's day: ")
n = int(input("Enter the number of days elapsed since today: "))
dayofweek(d,n)