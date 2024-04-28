""" Solution to exercises 11 and 12 from the Extra Notes for 6.1 to 6.4.
Sam Scott, Feb 2016"""

def test_prob(p):
    import random
    return random.randint(1,100) <= p*100

def test_random(p, n):
    count = 0
    for x in range(n):
        if test_prob(p):
            count = count + 1
    return count / n