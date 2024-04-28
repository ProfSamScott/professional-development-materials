"""Solutions to GCF exercises
Sam Scott, February 2015"""
def gcf(a, b):
    """ returns the greatest common factor of integers a and b"""
    gcf = 1
    f = 1
    while f <= min(a,b):
        if a % f == 0 and b % f == 0:
            gcf = f
        f += 1
    return gcf

def reduce(num, denom):
    """Given an integer numerator and denominator, prints a reduced version
    of the fraction"""
    f = gcf(num, denom)
    print(num,'/',denom,'=',num//f,'/',denom//f)

