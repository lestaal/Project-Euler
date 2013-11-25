import math

### Problem 2 ###

# Recursive solution
def sum_even_fib(limit, i=1, j=1, s=0):
    """ Recursively iterates through Fibonacci sequence and adds even numbers to sum
    Inputs: limit - integer
            i, j - previous two Fibonacci integers
            s - current sum (integer)
    Outputs: none, prints sum of all even Fibonacci numbers less than limit
    """
    if i + j > limit:
        print s
        return
    if (i + j)%2 == 0:
        s += i + j
    sum_even_fib(limit, j, i + j, s)

def test_sum_even_fib():
    """ test function sum_even_fib
    Inputs: none
    Outputs: none, prints results
    """
    sum_even_fib(10)
    print '=', 2+8
    sum_even_fib(50)
    print '=', 2+8+34

# Better solution
def fib(limit):
    """Sums every third Fibonacci number (the evens): _ _ 2 _ _ 8 _ _ 34 ...
    Inputs: limit - positive integer
    Output: integer sum of all even Fibonacci numbers less than limit
    """
    a = 1
    b = 1
    result = 0
    while a + b <= limit:
        result += a + b
        temp = a
        a = a + 2*b
        b = 2*temp + 3*b
    return result

def test_fib():
    """ test function fib
    Inputs: none
    Outputs: none, prints results
    """
    print fib(10), '=', 2+8
    print fib(50), '=', 2+8+34

print fib(4000000)
