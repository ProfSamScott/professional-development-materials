"""Solution to exercise 3.4 in
Think Python by Allen B. Downey
http://thinkpython.com

Sam Scott, January 2015"""

def do_twice(function, value):
    function(value)
    function(value)
    
def print_twice(value):
    print(value)
    print(value)

def do_four(function, value):
    do_twice(function, value)
    do_twice(function, value)
    
do_four(print_twice,'spam')
