def isprime(n):
    if n <= 1:
        return False
    factor = 2
    while factor <= round(n**0.5):
        if n % factor == 0:
            return False
        factor += 1
    return True