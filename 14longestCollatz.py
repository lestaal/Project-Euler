### Problem 14 ###

def longest_collatz(limit):
    """
    Inputs: limit - integer
    Outputs: starting number under limit that produces longest Collatz chain
    """
    max_count = 0
    max_start = 0
    for i in xrange(limit, 1, -1):
        n = i
        count = 0
        while n > 1:
            if n%2 == 0:
                n /= 2
            else:
                n  = 3*n + 1
            count += 1
        if count > max_count:
            max_count = count
            max_start = i
    return max_start

def test_longest_collatz():
    """ test function longestCollatz"""
    print longest_collatz(4), '= 3'
    print longest_collatz(6), '= 6'
    print longest_collatz(7), '= 7'

print longest_collatz(1000000)
