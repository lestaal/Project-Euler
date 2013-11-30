import math

### Problem 6 ###

def sum_square_diff(n):
    """
    Inputs: num - even integer
    Outputs: the difference bewtween the sum of the squares of the first n natural
             numbers and the square of the sum of the first n natural numbers
    """
    square_of_sum = ((n + 1)*(n/2))**2
    sum_of_squares = sum([i**2 for i in range(1, n+1)])
    return int(math.fabs(square_of_sum - sum_of_squares))

def test_sum_square_diff():
    """ test function sum_square_diff
    Inputs: none
    Outputs: none, prints results
    """
    print sum_square_diff(10), '= 2640'

print sum_square_diff(100)
