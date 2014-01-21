import math

### Problem 20 ###

def factorial_digit_sum(n):
    """
    Inputs: n - integer
    Outputs: sum of digits in n!
    """
    factorial = math.factorial(n)
    result = 0
    for i in str(factorial):
        result += int(i)
    return result

def test_factorial_digit_sum():
    """test factorial_digit_sum"""
    print factorial_digit_sum(10), '= 27'

print factorial_digit_sum(100)
