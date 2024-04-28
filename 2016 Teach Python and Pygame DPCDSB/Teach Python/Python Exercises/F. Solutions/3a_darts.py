"""Solution to 3a: darts. Flow chart and test cases
not included. Sam Scott, 2015"""
def who_won(alice, harman, abdul):
    if alice > harman:
        if alice > abdul:
            print('Alice won')
        else:
            print('Abdul won')
    else:
        if harman > abdul:
            print('Harman won')
        else:
            print('Abdul won')

# What would it take to make this program handle the tie games as well?