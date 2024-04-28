"""Solution to exercise 3.3 in 
Think Python by Allen B. Downey
http://thinkpython.com

Sam Scott, January 2015"""

def right_justify(string):
    """ string: the string to right justify
    prints: the string, right-justified to 70 characters"""
    print(' '*(70-len(string)),string,sep='')
    