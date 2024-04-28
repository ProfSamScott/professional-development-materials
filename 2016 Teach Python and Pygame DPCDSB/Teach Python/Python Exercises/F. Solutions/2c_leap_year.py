"""Solution to 3c: leap year
Sam Scott, January 2015"""
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "was a leap year.")
    else:
        print(year, "was not a leap year.")

def main():
    year = int(input('Enter a year: '))
    is_leap_year(year)

main()