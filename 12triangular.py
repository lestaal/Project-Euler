import math

### Problem 12 ###

def triangular(n):
    """
    Inputs: n - number of divisors the triangle number needs to reach
    Outputs: the first (lowest) triangle number with over n divisors
    """
    tri = 0
    for i in xrange(1, 1000000):
        tri += i
        divisors = 2 # 1 and itself
        for j in xrange(2, int(math.sqrt(tri))+1):
            if tri%j == 0:
                divisors += 2
        if divisors >= n:
            return tri

def test_triangular():
    """ test function triangular
    Inputs: none
    Outputs: none, prints results
    """
    print triangular(3), '= 6'
    print triangular(5), '= 28'

print triangular(500)
