""" Solution to exercise 10 from the Extra Notes
for 6.1 to 6.4.
Sam Scott, Feb 2016"""

def format_int(n, length):
    result = str(n)
    if len(result) < length:
        result = '0'*(length-len(result))+result
    return result

for x in range(10000):
    print(format_int(x+1,5))